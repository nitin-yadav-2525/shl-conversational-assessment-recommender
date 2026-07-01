def get_conversation_state(messages):

    latest = ""
    conversation = ""

    for msg in messages:
        if msg.role == "user":
            conversation += " " + msg.content.lower()
            latest = msg.content.lower()

    final_words = [
        "thanks", "thank you", "perfect", "that works", "looks good",
        "go ahead", "locking it in", "lock it in", "final list", "done",
        "great",
        # NEW fixes for C1/C6/C7/C8
        "that's good", "confirmed", "understood", "that covers it",
        "keep the shortlist", "keep the list", "all good",
        "sounds good", "agreed",
    ]

    if any(x in latest for x in final_words):
        return "end"

    return "continue"