# import json

# from app.llm import ask_llm
# from app.retriever import search_assessments


# SYSTEM_PROMPT = """
# You are an SHL Assessment Recommendation Agent.

# Your job is to recommend ONLY SHL assessments.

# Rules:

# 1. Read the complete conversation history.

# 2. Decide whether enough information exists.

# 3. If information is insufficient:
#    - Ask ONE clarification question.
#    - recommendations must be null.
#    - end_of_conversation=false

# 4. If information is sufficient:
#    - Return a short reply.
#    - Mention that recommendations follow.

# Never recommend anything outside SHL.
# """


# def process_chat(messages):

#     conversation = ""

#     for msg in messages:

#         conversation += f"{msg.role}: {msg.content}\n"

#     decision_prompt = f"""
# {SYSTEM_PROMPT}

# Conversation:

# {conversation}

# Should you ask another clarification question
# or recommend assessments?

# Return ONLY the assistant reply.
# """

#     assistant_reply = ask_llm(decision_prompt)

#     recommendation_needed = True

#     clarification_words = [
#         "what",
#         "which",
#         "could you",
#         "please specify",
#         "experience",
#         "seniority",
#         "role",
#         "selection",
#         "development"
#     ]

#     for word in clarification_words:

#         if word.lower() in assistant_reply.lower():

#             recommendation_needed = False
#             break

#     if not recommendation_needed:

#         return {
#             "reply": assistant_reply,
#             "recommendations": None,
#             "end_of_conversation": False
#         }

#     latest_user_message = ""

#     for msg in reversed(messages):

#         if msg.role == "user":
#             latest_user_message = msg.content
#             break

#     results = search_assessments(
#         latest_user_message,
#         top_k=5
#     )

#     recommendations = []

#     for item in results:

#         recommendations.append({

#             "name": item["name"],

#             "url": item["url"],

#             "test_type": ", ".join(item["test_type"])

#         })

#     return {

#         "reply": assistant_reply,

#         "recommendations": recommendations,

#         "end_of_conversation": True

#     }



# from app.llm import ask_llm
# from app.retriever import search_assessments
# from app.rules import detect_intent
# from app.compare import compare_assessments
# from app.refine import refine_query
# from app.recommendation_engine import recommend
# from app.response_builder import build_response


# SYSTEM_PROMPT = """
# You are an SHL Assessment Recommendation Agent.

# Rules:
# 1. Recommend ONLY SHL assessments.
# 2. Never invent assessment names or URLs.
# 3. Ask clarification questions if information is insufficient.
# 4. Refuse requests outside SHL assessments.
# 5. Keep responses concise and professional.
# """


# def build_recommendations(results):

#     recommendations = []

#     for item in results:

#         recommendations.append({

#             "name": item["name"],

#             "url": item["url"],

#             "test_type": ", ".join(item["test_type"])

#         })

#     return recommendations


# def process_chat(messages):

#     # -----------------------------
#     # Latest user message
#     # -----------------------------

#     latest_user_message = ""

#     for msg in reversed(messages):

#         if msg.role == "user":

#             latest_user_message = msg.content

#             break

#     # -----------------------------
#     # Full conversation
#     # -----------------------------

#     conversation = " ".join(
#         [msg.content.lower() for msg in messages if msg.role == "user"]
#     )

#     # -----------------------------
#     # Intent
#     # -----------------------------

#     intent = detect_intent(messages)

#     # ==================================================
#     # Clarification
#     # ==================================================

#     if intent == "clarify":

#         if (
#             any(x in conversation for x in [
#                 "cxo",
#                 "director",
#                 "leadership",
#                 "executive"
#             ])
#             and "selection" not in conversation
#             and "development" not in conversation
#             and "developmental" not in conversation
#         ):

#             reply = "Thanks. Is this for selection or developmental feedback?"

#         else:

#             reply = (
#                 "Could you please tell me the role, seniority level, "
#                 "required skills, and whether this is for selection or development?"
#             )

#         return {

#             "reply": reply,

#             "recommendations": None,

#             "end_of_conversation": False

#         }

#     # ==================================================
#     # Refuse
#     # ==================================================

#     if intent == "refuse":

#         return {

#             "reply": "I can only help with SHL assessment recommendations.",

#             "recommendations": None,

#             "end_of_conversation": True

#         }

#     # ==================================================
#     # Compare
#     # ==================================================

#     if intent == "compare":

#         comparison = compare_assessments(latest_user_message)

#         return {

#             "reply": comparison,

#             "recommendations": None,

#             "end_of_conversation": False

#         }

#     # ==================================================
#     # Refine
#     # ==================================================

#     if intent == "refine":

#         results = refine_query(messages)

#         return {

#             "reply": "I've updated the recommendations based on your latest requirements.",

#             "recommendations": build_recommendations(results),

#             "end_of_conversation": False

#         }

#     # ==================================================
#     # Recommendation
#     # ==================================================

#     results = search_assessments(
#         latest_user_message,
#         top_k=5
#     )
#     results = recommend(
#     results,
#     latest_user_message
#     )

#     prompt = f"""
# {SYSTEM_PROMPT}

# User Requirement:

# {latest_user_message}

# Top Matching SHL Assessments:

# {results}

# Write a professional response in 2 short sentences.
# Do NOT change assessment names.
# """

#     assistant_reply = ask_llm(prompt)

#     if assistant_reply.startswith("LLM Error"):

#         assistant_reply = (
#             "Based on your requirements, here are the most relevant SHL assessments from the SHL catalog."
#         )

#     return {

#         "reply": assistant_reply,

#         "recommendations": build_recommendations(results),

#         "end_of_conversation": False

#     }




# from app.llm import ask_llm
# from app.retriever import search_assessments
# from app.rules import detect_intent
# from app.compare import compare_assessments
# from app.refine import refine_query
# from app.recommendation_engine import recommend
# from app.response_builder import build_response
# from app.conversation_state import get_conversation_state
# from app.edit_recommendations import edit_recommendations


# SYSTEM_PROMPT = """
# You are an SHL Assessment Recommendation Agent.

# Rules:
# 1. Recommend ONLY SHL assessments.
# 2. Never invent assessment names or URLs.
# 3. Ask clarification questions whenever information is insufficient.
# 4. Refuse requests outside SHL assessments.
# 5. Keep responses short and professional.
# """


# # ==========================================================
# # Convert Retriever Output -> API Response
# # ==========================================================

# def build_recommendations(results):

#     recommendations = []

#     for item in results:

#         recommendations.append({

#             "name": item["name"],

#             "url": item["url"],

#             "test_type": ", ".join(item["test_type"])

#         })

#     return recommendations


# # ==========================================================
# # Main Chat Function
# # ==========================================================

# def process_chat(messages):

#     # ------------------------------------------------------
#     # Latest User Message
#     # ------------------------------------------------------

#     latest_user_message = ""

#     for msg in reversed(messages):

#         if msg.role == "user":

#             latest_user_message = msg.content

#             break

#     # ------------------------------------------------------
#     # Complete Conversation
#     # ------------------------------------------------------

#     conversation = " ".join(

#         msg.content.lower()

#         for msg in messages

#         if msg.role == "user"

#     )

#     # ------------------------------------------------------
#     # Conversation State
#     # ------------------------------------------------------

#     state = get_conversation_state(messages)

#     # ------------------------------------------------------
#     # Intent Detection
#     # ------------------------------------------------------

#     intent = detect_intent(messages)

#     # ======================================================
#     # Clarification
#     # ======================================================

#     if intent == "clarify":

#         if (
#             any(word in conversation for word in [
#                 "leadership",
#                 "director",
#                 "executive",
#                 "cxo"
#             ])
#             and "selection" not in conversation
#             and "development" not in conversation
#             and "developmental" not in conversation
#         ):

#             reply = (
#                 "Thanks. Is this for selection or developmental feedback?"
#             )

#         else:

#             reply = (
#                 "Could you please tell me the role, seniority level, "
#                 "required skills, and whether this is for selection or development?"
#             )

#         return build_response(

#             reply=reply,

#             recommendations=None,

#             end=False

#         )

#     # ======================================================
#     # Refuse
#     # ======================================================

#     if intent == "refuse":

#         return build_response(

#             reply="I can only help with SHL assessment recommendations.",

#             recommendations=None,

#             end=True

#         )

#     # ======================================================
#     # Compare
#     # ======================================================

#     if intent == "compare":

#         comparison = compare_assessments(

#             latest_user_message

#         )

#         return build_response(

#             reply=comparison,

#             recommendations=None,

#             end=(state == "end")

#         )

#     # ======================================================
#     # Refine Existing Recommendation
#     # ======================================================

#     if intent == "refine":

#         results = refine_query(messages)

#         results = recommend(

#             results,

#             conversation

#         )

#         results = edit_recommendations(

#             results,

#             conversation

#         )

#         return build_response(

#             reply="I've updated the recommendations based on your latest requirements.",

#             recommendations=build_recommendations(results),

#             end=(state == "end")

#         )

#     # ======================================================
#     # Recommendation Flow
#     # ======================================================

#     # ======================================================
# # Recommendation Flow
# # ======================================================

#     follow_up_words = [

#     "add",

#     "drop",

#     "remove",

#     "replace",

#     "keep",

#     "also",

#     "instead",

#     "final",

#     "lock",

#     "thanks",

#     "perfect",

#     "that works"

# ]

#     is_follow_up = any(

#     word in latest_user_message.lower()

#     for word in follow_up_words

# )

#     if is_follow_up:
 
#      results = search_assessments(

#         conversation,

#         top_k=5

#     )

#     else:

#      results = search_assessments(

#         latest_user_message,

#         top_k=5

#     )

# results = recommend(

#     results,

#     conversation

# )

# results = edit_recommendations(

#     results,

#     conversation

# )

#     # ======================================================
#     # Ask LLM for Short Summary
#     # ======================================================

# prompt = f"""
# {SYSTEM_PROMPT}

# Conversation:

# {conversation}

# Top Matching SHL Assessments:

# {results}

# Write a short professional reply in 2 sentences.

# Do NOT modify assessment names.
# """

#     assistant_reply = ask_llm(prompt)

#     # ======================================================
#     # Gemini Fallback
#     # ======================================================

#     if assistant_reply.startswith("LLM Error"):

#         assistant_reply = (
#             "Based on your requirements, here are the most relevant SHL assessments from the SHL catalog."
#         )

#     # ======================================================
#     # Final Response
#     # ======================================================

#     return build_response(

#         reply=assistant_reply,

#         recommendations=build_recommendations(results),

#         end=(state == "end")

#     )



# from app.llm import ask_llm
# from app.retriever import search_assessments
# from app.rules import detect_intent
# from app.compare import compare_assessments
# from app.refine import refine_query
# from app.recommendation_engine import recommend
# from app.response_builder import build_response
# from app.conversation_state import get_conversation_state
# from app.edit_recommendations import edit_recommendations


# SYSTEM_PROMPT = """
# You are an SHL Assessment Recommendation Agent.

# Rules:
# 1. Recommend ONLY SHL assessments.
# 2. Never invent assessment names or URLs.
# 3. Ask clarification questions whenever information is insufficient.
# 4. Refuse requests outside SHL assessments.
# 5. Keep responses short and professional.
# """


# # ==========================================================
# # Convert Retriever Output -> API Response
# # ==========================================================

# def build_recommendations(results):

#     recommendations = []

#     for item in results:

#         recommendations.append({

#             "name": item["name"],

#             "url": item["url"],

#             "test_type": ", ".join(item["test_type"])

#         })

#     return recommendations


# # ==========================================================
# # Main Chat Function
# # ==========================================================

# def process_chat(messages):

#     # ------------------------------------------------------
#     # Latest User Message
#     # ------------------------------------------------------

#     latest_user_message = ""

#     for msg in reversed(messages):

#         if msg.role == "user":

#             latest_user_message = msg.content

#             break

#     # ------------------------------------------------------
#     # Complete Conversation
#     # ------------------------------------------------------

#     conversation = " ".join(

#         msg.content.lower()

#         for msg in messages

#         if msg.role == "user"

#     )

#     # ------------------------------------------------------
#     # Conversation State
#     # ------------------------------------------------------

#     state = get_conversation_state(messages)

#     # ------------------------------------------------------
#     # Intent Detection
#     # ------------------------------------------------------

#     intent = detect_intent(messages)

#     # ======================================================
#     # Clarification
#     # ======================================================

#     if intent == "clarify":

#         if (
#             any(word in conversation for word in [
#                 "leadership",
#                 "director",
#                 "executive",
#                 "cxo"
#             ])
#             and "selection" not in conversation
#             and "development" not in conversation
#             and "developmental" not in conversation
#         ):

#             reply = (
#                 "Thanks. Is this for selection or developmental feedback?"
#             )

#         else:

#             reply = (
#                 "Could you please tell me the role, seniority level, "
#                 "required skills, and whether this is for selection or development?"
#             )

#         return build_response(

#             reply=reply,

#             recommendations=None,

#             end=False

#         )

#     # ======================================================
#     # Refuse
#     # ======================================================

#     if intent == "refuse":

#         return build_response(

#             reply="I can only help with SHL assessment recommendations.",

#             recommendations=None,

#             end=True

#         )

#     # ======================================================
#     # Compare
#     # ======================================================

#     if intent == "compare":

#         comparison = compare_assessments(

#             latest_user_message

#         )

#         return build_response(

#             reply=comparison,

#             recommendations=None,

#             end=(state == "end")

#         )

#     # ======================================================
#     # Refine Existing Recommendation
#     # ======================================================

#     if intent == "refine":

#         results = refine_query(messages)

#         results = recommend(

#             results,

#             conversation

#         )

#         results = edit_recommendations(

#             results,

#             conversation

#         )

#         return build_response(

#             reply="I've updated the recommendations based on your latest requirements.",

#             recommendations=build_recommendations(results),

#             end=(state == "end")

#         )

#     # ======================================================
#     # Recommendation Flow
#     # ======================================================

#     follow_up_words = [

#         "add",

#         "drop",

#         "remove",

#         "replace",

#         "keep",

#         "also",

#         "instead",

#         "final",

#         "lock",

#         "thanks",

#         "perfect",

#         "that works"

#     ]

#     is_follow_up = any(

#         word in latest_user_message.lower()

#         for word in follow_up_words

#     )

#     if is_follow_up:

#         results = search_assessments(

#             conversation,

#             top_k=5

#         )

#     else:

#         results = search_assessments(

#             latest_user_message,

#             top_k=5

#         )

#     results = recommend(

#         results,

#         conversation

#     )

#     results = edit_recommendations(

#         results,

#         conversation

#     )

#     # ======================================================
#     # Ask LLM for Short Summary
#     # ======================================================

#     prompt = f"""
# {SYSTEM_PROMPT}

# Conversation:

# {conversation}

# Top Matching SHL Assessments:

# {results}

# Write a short professional reply in 2 sentences.

# Do NOT modify assessment names.
# """

#     assistant_reply = ask_llm(prompt)

#     # ======================================================
#     # Gemini Fallback
#     # ======================================================

#     if assistant_reply.startswith("LLM Error"):

#         assistant_reply = (
#             "Based on your requirements, here are the most relevant SHL assessments from the SHL catalog."
#         )

#     # ======================================================
#     # Final Response
#     # ======================================================

#     return build_response(

#         reply=assistant_reply,

#         recommendations=build_recommendations(results),

#         end=(state == "end")

#     )

# ye tha last time sahi uper wala 

# from app.llm import ask_llm
# from app.retriever import search_assessments
# from app.rules import detect_intent
# from app.compare import compare_assessments
# from app.refine import refine_query
# from app.recommendation_engine import recommend
# from app.response_builder import build_response
# from app.conversation_state import get_conversation_state
# from app.edit_recommendations import edit_recommendations


# SYSTEM_PROMPT = """
# You are an SHL Assessment Recommendation Agent.
# Rules:
# 1. Recommend ONLY SHL assessments from the catalog.
# 2. Never invent assessment names or URLs.
# 3. Ask clarification questions when information is insufficient.
# 4. Refuse requests outside SHL assessments (legal advice, off-topic).
# 5. Keep responses short and professional (2 sentences max).
# """


# def build_recommendations(results):
#     return [
#         {
#             "name": item["name"],
#             "url": item["url"],
#             "test_type": (
#                 ", ".join(item["test_type"])
#                 if isinstance(item.get("test_type"), list)
#                 else str(item.get("test_type", ""))
#             )
#         }
#         for item in results
#     ]


# def build_search_query(messages):
#     """
#     Combine ALL user messages into one query so context
#     persists across turns (e.g. 'English' remembers 'contact centre').
#     Give more weight to recent messages by repeating them.
#     """
#     user_msgs = [m.content for m in messages if m.role == "user"]
#     if not user_msgs:
#         return ""
#     # repeat the last message to boost its weight
#     combined = " ".join(user_msgs) + " " + user_msgs[-1]
#     return combined.strip()


# def process_chat(messages):

#     latest_user_message = ""
#     for msg in reversed(messages):
#         if msg.role == "user":
#             latest_user_message = msg.content
#             break

#     conversation = " ".join(
#         msg.content for msg in messages if msg.role == "user"
#     )
#     conv_lower = conversation.lower()

#     state  = get_conversation_state(messages)
#     intent = detect_intent(messages)

#     # ======================================================
#     # REFUSE — off-topic / legal / prompt injection
#     # ======================================================
#     if intent == "refuse":
#         return build_response(
#             reply=(
#                 "I can only help with SHL assessment recommendations. "
#                 "For legal or compliance questions, please consult your HR or legal team."
#             ),
#             recommendations=None,
#             end=False
#         )

#     # ======================================================
#     # CLARIFY
#     # ======================================================
#     if intent == "clarify":
#         if any(w in conv_lower for w in ["leadership", "director", "executive", "cxo"]):
#             if "selection" not in conv_lower and "development" not in conv_lower:
#                 reply = "Thanks. Is this for selection or developmental feedback?"
#             else:
#                 reply = (
#                     "Could you share the seniority level and required skills "
#                     "so I can narrow down the right assessments?"
#                 )
#         else:
#             reply = (
#                 "Could you tell me the role, seniority level, required skills, "
#                 "and whether this is for selection or development?"
#             )
#         return build_response(reply=reply, recommendations=None, end=False)

#     # ======================================================
#     # COMPARE
#     # ======================================================
#     if intent == "compare":
#         comparison = compare_assessments(latest_user_message)
#         return build_response(
#             reply=comparison,
#             recommendations=None,
#             end=(state == "end")
#         )

#     # ======================================================
#     # REFINE — add / drop / keep / replace
#     # ======================================================
#     if intent == "refine":
#         results = refine_query(messages)
#         results = recommend(results, conv_lower)
#         return build_response(
#             reply="I've updated the recommendations based on your latest requirements.",
#             recommendations=build_recommendations(results),
#             end=(state == "end")
#         )

#     # ======================================================
#     # RECOMMEND — use FULL conversation for context
#     # ======================================================
#     search_query = build_search_query(messages)
#     results = search_assessments(search_query, top_k=8)
#     results = recommend(results, conv_lower)
#     results = edit_recommendations(results, conv_lower)

#     # LLM summary
#     prompt = f"""
# {SYSTEM_PROMPT}

# User requirement: {latest_user_message}

# Top matching SHL assessments:
# {[r['name'] for r in results]}

# Write a professional 2-sentence response.
# Do NOT modify assessment names.
# """
#     assistant_reply = ask_llm(prompt)

#     if assistant_reply.startswith("LLM Error"):
#         assistant_reply = (
#             "Based on your requirements, here are the most relevant SHL assessments."
#         )

#     return build_response(
#         reply=assistant_reply,
#         recommendations=build_recommendations(results),
#         end=(state == "end")
#     )


#abhi tak uper wala best




# from app.llm import ask_llm
# from app.retriever import search_assessments
# from app.rules import detect_intent
# from app.compare import compare_assessments
# from app.refine import refine_query
# from app.recommendation_engine import recommend
# from app.response_builder import build_response
# from app.conversation_state import get_conversation_state
# from app.edit_recommendations import edit_recommendations, dedup


# SYSTEM_PROMPT = """
# You are an SHL Assessment Recommendation Agent.
# Rules:
# 1. Recommend ONLY SHL assessments from the catalog.
# 2. Never invent assessment names or URLs.
# 3. Ask clarification questions when information is insufficient.
# 4. Refuse requests outside SHL assessments (legal advice, off-topic).
# 5. Keep responses short and professional (2 sentences max).
# """


# def build_recommendations(results):
#     return [
#         {
#             "name": item["name"],
#             "url": item["url"],
#             "test_type": (
#                 ", ".join(item["test_type"])
#                 if isinstance(item.get("test_type"), list)
#                 else str(item.get("test_type", ""))
#             )
#         }
#         for item in results
#     ]


# def build_search_query(messages):
#     """Combine all user messages; repeat last message for recency weight."""
#     user_msgs = [m.content for m in messages if m.role == "user"]
#     if not user_msgs:
#         return ""
#     return (" ".join(user_msgs) + " " + user_msgs[-1]).strip()


# def process_chat(messages):

#     latest_user_message = ""
#     for msg in reversed(messages):
#         if msg.role == "user":
#             latest_user_message = msg.content
#             break

#     conversation = " ".join(m.content for m in messages if m.role == "user")
#     conv_lower   = conversation.lower()
#     latest_lower = latest_user_message.lower()

#     state  = get_conversation_state(messages)
#     intent = detect_intent(messages)

#     # ======================================================
#     # REFUSE
#     # ======================================================
#     if intent == "refuse":
#         return build_response(
#             reply=(
#                 "I can only help with SHL assessment recommendations. "
#                 "For legal or compliance questions, please consult your HR or legal team."
#             ),
#             recommendations=None,
#             end=False
#         )

#     # ======================================================
#     # CLARIFY
#     # ======================================================
#     if intent == "clarify":
#         if any(w in conv_lower for w in ["leadership", "director", "executive", "cxo"]):
#             if "selection" not in conv_lower and "development" not in conv_lower:
#                 reply = "Thanks. Is this for selection or developmental feedback?"
#             else:
#                 reply = (
#                     "Could you share the seniority level and required skills "
#                     "so I can narrow down the right assessments?"
#                 )
#         else:
#             reply = (
#                 "Could you tell me the role, seniority level, required skills, "
#                 "and whether this is for selection or development?"
#             )
#         return build_response(reply=reply, recommendations=None, end=False)

#     # ======================================================
#     # COMPARE
#     # ======================================================
#     if intent == "compare":
#         comparison = compare_assessments(latest_user_message)
#         return build_response(
#             reply=comparison,
#             recommendations=None,
#             end=(state == "end")
#         )

#     # ======================================================
#     # REFINE
#     # Uses LATEST message for recommend() pattern matching
#     # so old conversation patterns don't override new edits.
#     # Then re-applies edit_recommendations to enforce drops/adds.
#     # ======================================================
#     if intent == "refine":
#         results = refine_query(messages)
#         # Use latest message for pattern matching to avoid stale overrides
#         results = recommend(results, latest_lower)
#         # Re-apply edits (recommend may have re-injected dropped items)
#         results = edit_recommendations(results, conv_lower)
#         results = dedup(results)[:5]

#         return build_response(
#             reply="I've updated the recommendations based on your latest requirements.",
#             recommendations=build_recommendations(results),
#             end=(state == "end")
#         )

#     # ======================================================
#     # RECOMMEND
#     # ======================================================
#     search_query = build_search_query(messages)
#     results = search_assessments(search_query, top_k=8)
#     results = recommend(results, conv_lower)
#     results = edit_recommendations(results, conv_lower)
#     results = dedup(results)[:5]

#     prompt = f"""
# {SYSTEM_PROMPT}

# User requirement: {latest_user_message}

# Top matching SHL assessments:
# {[r['name'] for r in results]}

# Write a professional 2-sentence response.
# Do NOT modify assessment names.
# """
#     assistant_reply = ask_llm(prompt)

#     if assistant_reply.startswith("LLM Error"):
#         assistant_reply = (
#             "Based on your requirements, here are the most relevant SHL assessments."
#         )

#     return build_response(
#         reply=assistant_reply,
#         recommendations=build_recommendations(results),
#         end=(state == "end")
#     )





# from app.llm import ask_llm
# from app.retriever import search_assessments
# from app.rules import detect_intent
# from app.compare import compare_assessments
# from app.refine import refine_query
# from app.recommendation_engine import recommend
# from app.response_builder import build_response
# from app.conversation_state import get_conversation_state
# from app.edit_recommendations import edit_recommendations, dedup


# SYSTEM_PROMPT = """
# You are an SHL Assessment Recommendation Agent.
# Rules:
# 1. Recommend ONLY SHL assessments from the catalog.
# 2. Never invent assessment names or URLs.
# 3. Ask clarification questions when information is insufficient.
# 4. Refuse requests outside SHL assessments (legal advice, off-topic).
# 5. Keep responses short and professional (2 sentences max).
# """


# # -------------------------------------------------------
# # Pure-confirmation detection
# # When the user says "confirmed / that's good / understood"
# # with NO new instructions, we freeze the existing list
# # instead of re-searching (prevents shortlist corruption).
# # -------------------------------------------------------
# _PURE_CONFIRM_WORDS = [
#     "thanks", "thank you", "perfect", "that works", "looks good",
#     "all good", "sounds good", "agreed", "confirmed", "understood",
#     "that covers it", "that's good", "great", "done",
#     "keep the shortlist", "keep the list", "keep as-is", "keep it as",
# ]
# _NEW_INSTRUCTION_WORDS = [
#     "add ", "drop ", "remove ", "replace ", "also add",
#     "don't include", "exclude", "swap ", "final list", "change ",
# ]


# def _is_pure_confirmation(latest: str) -> bool:
#     """True when message is only an acknowledgement with no new instructions."""
#     l = latest.lower().strip()
#     has_new = any(w in l for w in _NEW_INSTRUCTION_WORDS)
#     # "keep X" is an instruction only when X is a specific assessment, not the shortlist
#     if "keep " in l:
#         keep_confirm = any(x in l for x in [
#             "keep the shortlist", "keep the list", "keep as-is", "keep it as"
#         ])
#         keep_instruct = any(x in l for x in [
#             "keep verify", "keep shl", "keep opq", "keep aws", "keep docker"
#         ])
#         if keep_instruct and not keep_confirm:
#             has_new = True
#     has_confirm = any(w in l for w in _PURE_CONFIRM_WORDS)
#     return has_confirm and not has_new


# def build_recommendations(results):
#     return [
#         {
#             "name": item["name"],
#             "url": item["url"],
#             "test_type": (
#                 ", ".join(item["test_type"])
#                 if isinstance(item.get("test_type"), list)
#                 else str(item.get("test_type", ""))
#             )
#         }
#         for item in results
#     ]


# def build_search_query(messages):
#     user_msgs = [m.content for m in messages if m.role == "user"]
#     if not user_msgs:
#         return ""
#     return (" ".join(user_msgs) + " " + user_msgs[-1]).strip()


# def process_chat(messages):

#     latest_user_message = ""
#     for msg in reversed(messages):
#         if msg.role == "user":
#             latest_user_message = msg.content
#             break

#     conversation = " ".join(m.content for m in messages if m.role == "user")
#     conv_lower   = conversation.lower()
#     latest_lower = latest_user_message.lower()

#     state  = get_conversation_state(messages)
#     intent = detect_intent(messages)

#     # ======================================================
#     # REFUSE
#     # ======================================================
#     if intent == "refuse":
#         return build_response(
#             reply=(
#                 "I can only help with SHL assessment recommendations. "
#                 "For legal or compliance questions, please consult your HR or legal team."
#             ),
#             recommendations=None,
#             end=False
#         )

#     # ======================================================
#     # CLARIFY
#     # ======================================================
#     if intent == "clarify":
#         if any(w in conv_lower for w in ["leadership", "director", "executive", "cxo"]):
#             if "selection" not in conv_lower and "development" not in conv_lower:
#                 reply = "Thanks. Is this for selection or developmental feedback?"
#             else:
#                 reply = (
#                     "Could you share the seniority level and required skills "
#                     "so I can narrow down the right assessments?"
#                 )
#         else:
#             reply = (
#                 "Could you tell me the role, seniority level, required skills, "
#                 "and whether this is for selection or development?"
#             )
#         return build_response(reply=reply, recommendations=None, end=False)

#     # ======================================================
#     # COMPARE — FIX: always returns None recs, never ends conv
#     # ======================================================
#     if intent == "compare":
#         comparison = compare_assessments(latest_user_message)
#         return build_response(
#             reply=comparison,
#             recommendations=None,   # compare never modifies the shortlist
#             end=False               # compare is never the final turn
#         )

#     # ======================================================
#     # REFINE
#     # ======================================================
#     if intent == "refine":

#         # FIX: pure confirmation → freeze list, set end=True
#         if _is_pure_confirmation(latest_lower):
#             results = refine_query(messages)
#             results = dedup(results)[:5]
#             return build_response(
#                 reply="Perfect. I've locked in your assessment shortlist.",
#                 recommendations=build_recommendations(results),
#                 end=True
#             )

#         # Normal refine — apply edits
#         results = refine_query(messages)
#         results = recommend(results, latest_lower)
#         results = edit_recommendations(results, conv_lower)
#         results = dedup(results)[:5]

#         return build_response(
#             reply="I've updated the recommendations based on your latest requirements.",
#             recommendations=build_recommendations(results),
#             end=(state == "end")
#         )

#     # ======================================================
#     # RECOMMEND
#     # ======================================================
#     search_query = build_search_query(messages)
#     results = search_assessments(search_query, top_k=8)
#     results = recommend(results, conv_lower)
#     results = edit_recommendations(results, conv_lower)
#     results = dedup(results)[:5]

#     prompt = f"""
# {SYSTEM_PROMPT}

# User requirement: {latest_user_message}

# Top matching SHL assessments:
# {[r['name'] for r in results]}

# Write a professional 2-sentence response.
# Do NOT modify assessment names.
# """
#     assistant_reply = ask_llm(prompt)

#     if assistant_reply.startswith("LLM Error"):
#         assistant_reply = (
#             "Based on your requirements, here are the most relevant SHL assessments."
#         )

#     return build_response(
#         reply=assistant_reply,
#         recommendations=build_recommendations(results),
#         end=(state == "end")
#     )


# abhi tak ka sabse best uper wala 



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