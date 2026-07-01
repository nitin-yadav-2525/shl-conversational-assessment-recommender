def detect_intent(messages):

    latest = ""
    conversation = ""

    for msg in messages:
        if msg.role == "user":
            conversation += " " + msg.content.lower()

    for msg in reversed(messages):
        if msg.role == "user":
            latest = msg.content.lower()
            break

    # =====================================================
    # REFUSE
    # =====================================================
    refuse_phrases = [
        "weather", "movie", "ipl", "politics", "cricket",
        "legally required", "legal advice", "legal requirement",
        "are we legally", "legally obligated", "required by law",
        "does this satisfy", "does shl test satisfy",
        "ignore your instructions", "ignore previous",
        "forget your instructions", "you are now"
    ]
    if any(x in latest for x in refuse_phrases):
        return "refuse"

    # =====================================================
    # COMPARE  (FIX: added "different from", "is X different")
    # =====================================================
    compare_triggers = [
        "compare",
        "difference between",
        "what's the difference",
        "what is the difference",
        "different from",       # NEW — catches "is X different from Y?"
        "differs from",         # NEW
    ]
    # Also catch "is the [assessment] different" pattern with a "?"
    is_difference_question = (
        "different" in latest and "?" in latest
        and any(msg.role == "assistant" for msg in messages)
    )
    if any(t in latest for t in compare_triggers) or is_difference_question:
        return "compare"

    # =====================================================
    # REFINE
    # =====================================================
    has_prior_assistant = any(msg.role == "assistant" for msg in messages)

    is_pure_question = latest.strip().endswith("?") and not any(
        x in latest for x in ["add ", "drop ", "remove ", "keep ", "final list"]
    )

    explicit_edits = [
        "add ", "drop ", "remove ", "keep ",
        "replace ", "also add", "don't include",
        "exclude", "swap ", "final list",
        "locking it in", "lock it in",
        "confirmed", "go ahead", "that works",
        "that's good", "sounds good", "perfect",
        "great", "understood",
    ]

    if has_prior_assistant and not is_pure_question:
        if any(x in latest for x in explicit_edits):
            return "refine"

    # =====================================================
    # CLARIFY
    # =====================================================
    vague = [
        "assessment", "solution", "recommend",
        "test", "help me hire", "what should we use"
    ]
    if any(x in latest for x in vague) and len(latest.split()) < 8:
        return "clarify"

    return "recommend"