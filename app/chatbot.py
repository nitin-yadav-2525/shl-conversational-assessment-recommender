from app.llm import ask_llm
from app.retriever import search_assessments
from app.rules import detect_intent
from app.compare import compare_assessments
from app.refine import refine_query
from app.recommendation_engine import recommend
from app.response_builder import build_response
from app.conversation_state import get_conversation_state
from app.edit_recommendations import edit_recommendations, dedup


SYSTEM_PROMPT = """
You are an SHL Assessment Recommendation Agent.
Rules:
1. Recommend ONLY SHL assessments from the catalog.
2. Never invent assessment names or URLs.
3. Ask clarification questions when information is insufficient.
4. Refuse requests outside SHL assessments.
5. Keep responses short and professional (2 sentences max).
"""

KEEP_AS_IS_PHRASES = [
    "keep the shortlist as-is",
    "keep shortlist as-is",
    "keep the list as-is",
    "keep as-is",
    "keep it as is",
    "keep the shortlist",
    "no changes",
    "leave it as is",
    "that's all",
    "that is all",
]


def build_recommendations(results):
    return [
        {
            "name": item["name"],
            "url": item["url"],
            "test_type": (
                ", ".join(item["test_type"])
                if isinstance(item.get("test_type"), list)
                else str(item.get("test_type", ""))
            )
        }
        for item in results
    ]


def get_last_recommendations(messages):
    """Extract previous assistant recommendations from conversation history."""
    for msg in reversed(messages):
        if msg.role == "assistant" and hasattr(msg, "recommendations") and msg.recommendations:
            return msg.recommendations
    return None


def build_search_query(messages):
    user_msgs = [m.content for m in messages if m.role == "user"]
    if not user_msgs:
        return ""
    return (" ".join(user_msgs) + " " + user_msgs[-1]).strip()


def process_chat(messages):

    latest_user_message = ""
    for msg in reversed(messages):
        if msg.role == "user":
            latest_user_message = msg.content
            break

    conversation = " ".join(m.content for m in messages if m.role == "user")
    conv_lower   = conversation.lower()
    latest_lower = latest_user_message.lower()

    state  = get_conversation_state(messages)
    intent = detect_intent(messages)

    # ======================================================
    # REFUSE
    # ======================================================
    if intent == "refuse":
        return build_response(
            reply=(
                "I can only help with SHL assessment recommendations. "
                "For legal or compliance questions, please consult your HR or legal team."
            ),
            recommendations=None,
            end=False
        )

    # ======================================================
    # CLARIFY
    # ======================================================
    if intent == "clarify":
        if any(w in conv_lower for w in ["leadership", "director", "executive", "cxo"]):
            if "selection" not in conv_lower and "development" not in conv_lower:
                reply = "Thanks. Is this for selection or developmental feedback?"
            else:
                reply = (
                    "Could you share the seniority level and required skills "
                    "so I can narrow down the right assessments?"
                )
        else:
            reply = (
                "Could you tell me the role, seniority level, required skills, "
                "and whether this is for selection or development?"
            )
        return build_response(reply=reply, recommendations=None, end=False)

    # ======================================================
    # COMPARE
    # ======================================================
    if intent == "compare":
        comparison = compare_assessments(latest_user_message)
        return build_response(
            reply=comparison,
            recommendations=None,
            end=(state == "end")
        )

    # ======================================================
    # REFINE
    # ======================================================
    if intent == "refine":

        # Special case: "keep as-is" — return previous recs unchanged
        if any(p in latest_lower for p in KEEP_AS_IS_PHRASES):
            # Look for previous recommendations in the _request_ objects
            # We'll re-run refine on the pre-latest context instead
            prior_messages = [m for m in messages[:-2]]  # exclude last user + this
            if prior_messages:
                prior_conv = " ".join(m.content for m in prior_messages if m.role == "user").lower()
                results = search_assessments(build_search_query(prior_messages), top_k=8)
                results = recommend(results, prior_conv)
                results = edit_recommendations(results, prior_conv)
                results = dedup(results)[:5]
            else:
                results = []
            return build_response(
                reply="I've kept the shortlist as requested.",
                recommendations=build_recommendations(results),
                end=(state == "end")
            )

        # Normal refine
        results = refine_query(messages)

        # Use latest message for recommend() — avoids stale pattern overrides
        # But for "keep verify / locking" — use conv_lower to detect
        if any(t in latest_lower for t in ["keep verify", "locking", "verify g+"]):
            # Add Verify G+ without replacing everything
            from app.retriever import search_assessments as sa
            verify = sa("SHL Verify Interactive G+", top_k=1)
            if verify:
                names_in = {r["name"] for r in results}
                if verify[0]["name"] not in names_in:
                    results = [verify[0]] + results
            results = edit_recommendations(results, conv_lower)
            results = dedup(results)[:5]
        else:
            results = recommend(results, latest_lower)
            results = edit_recommendations(results, conv_lower)
            results = dedup(results)[:5]

        return build_response(
            reply="I've updated the recommendations based on your latest requirements.",
            recommendations=build_recommendations(results),
            end=(state == "end")
        )

    # ======================================================
    # RECOMMEND
    # ======================================================
    search_query = build_search_query(messages)
    results = search_assessments(search_query, top_k=8)
    results = recommend(results, conv_lower)
    results = edit_recommendations(results, conv_lower)
    results = dedup(results)[:5]

    prompt = f"""
{SYSTEM_PROMPT}
User requirement: {latest_user_message}
Top matching SHL assessments: {[r['name'] for r in results]}
Write a professional 2-sentence response. Do NOT modify assessment names.
"""
    assistant_reply = ask_llm(prompt)
    if assistant_reply.startswith("LLM Error"):
        assistant_reply = "Based on your requirements, here are the most relevant SHL assessments."

    return build_response(
        reply=assistant_reply,
        recommendations=build_recommendations(results),
        end=(state == "end")
    )