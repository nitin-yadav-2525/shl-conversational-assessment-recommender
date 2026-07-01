from app.retriever import search_assessments


def get_last_user_message(messages):

    for msg in reversed(messages):
        if msg.role == "user":
            return msg.content

    return ""


def count_user_turns(messages):

    count = 0

    for msg in messages:
        if msg.role == "user":
            count += 1

    return count


def dialogue_manager(messages):

    turns = count_user_turns(messages)

    latest = get_last_user_message(messages).lower()

    # -----------------------------
    # TURN 1
    # -----------------------------
    if turns == 1:

        return {
            "reply": "Happy to help. Could you tell me the role, seniority level, and whether this is for selection or development?",
            "recommendations": None,
            "end_of_conversation": False
        }

    # -----------------------------
    # TURN 2
    # -----------------------------
    if turns == 2:

        # Still not enough information

        if "selection" not in latest and "development" not in latest:

            return {
                "reply": "Thanks. Is this for selection or developmental feedback?",
                "recommendations": None,
                "end_of_conversation": False
            }

    # -----------------------------
    # Recommendation Stage
    # -----------------------------
    results = search_assessments(latest, top_k=5)

    recommendations = []

    for item in results:

        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": ", ".join(item["test_type"])
        })

    # -----------------------------
    # Conversation End
    # -----------------------------
    if turns >= 4:

        return {
            "reply": "These are the final recommended SHL assessments based on your requirements.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }

    return {
        "reply": "Based on the information provided, here are the most relevant SHL assessments.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }