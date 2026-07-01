# from app.retriever import search_assessments


# def refine_query(messages):

#     query = ""

#     # Saare user messages combine karo
#     for msg in messages:
#         if msg.role == "user":
#             query += msg.content + " "

#     return search_assessments(query, top_k=5)



# from app.retriever import search_assessments


# def refine_query(messages):

#     # Complete conversation
#     conversation = ""

#     for msg in messages:
#         if msg.role == "user":
#             conversation += " " + msg.content

#     query = conversation.lower()

#     # --------------------------------------------------
#     # ADD
#     # --------------------------------------------------

#     if "add aws" in query:
#         conversation += " Amazon Web Services AWS"

#     if "add docker" in query:
#         conversation += " Docker"

#     if "add spring" in query:
#         conversation += " Spring Framework"

#     if "add cognitive" in query:
#         conversation += " Verify G+"

#     # --------------------------------------------------
#     # KEEP
#     # --------------------------------------------------

#     if "keep verify" in query:
#         conversation += " Verify G+"

#     if "keep graduate scenarios" in query:
#         conversation += " Graduate Scenarios"

#     # --------------------------------------------------
#     # REPLACE
#     # --------------------------------------------------

#     if "replace opq" in query:
#         conversation = conversation.replace("OPQ", "")

#     # --------------------------------------------------
#     # DROP
#     # --------------------------------------------------

#     if "drop rest" in query:
#         conversation = conversation.replace("REST", "")

#     if "drop opq" in query:
#         conversation = conversation.replace("OPQ", "")

#     # --------------------------------------------------
#     # Search Again
#     # --------------------------------------------------

#     return search_assessments(
#         conversation,
#         top_k=5
#     )

# ye tha last time uper wala 




# from app.retriever import search_assessments
# from app.edit_recommendations import edit_recommendations


# def refine_query(messages):
#     """
#     Search using FULL conversation (so context stays),
#     then apply add/drop/keep edits from edit_recommendations.
#     """
#     user_msgs = [m.content for m in messages if m.role == "user"]
#     if not user_msgs:
#         return []

#     # Weight recent messages more
#     combined = " ".join(user_msgs) + " " + user_msgs[-1]
#     conv_lower = combined.lower()

#     results = search_assessments(combined.strip(), top_k=10)
#     results = edit_recommendations(results, conv_lower)

#     return results




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