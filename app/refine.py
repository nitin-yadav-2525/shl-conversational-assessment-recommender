from app.retriever import search_assessments
from app.edit_recommendations import edit_recommendations, dedup


def refine_query(messages):
    """
    Search using FULL conversation context,
    then apply add/drop/keep edits.
    """
    user_msgs = [m.content for m in messages if m.role == "user"]
    if not user_msgs:
        return []

    # Weight recent messages more by repeating last message
    combined = " ".join(user_msgs) + " " + user_msgs[-1]
    conv_lower = combined.lower()

    results = search_assessments(combined.strip(), top_k=10)
    results = edit_recommendations(results, conv_lower)

    return dedup(results)[:5]