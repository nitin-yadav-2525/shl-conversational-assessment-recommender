# def detect_intent(messages):

#     latest = ""

#     for msg in reversed(messages):
#         if msg.role == "user":
#             latest = msg.content.lower()
#             break

#     # Compare
#     if "difference" in latest or "compare" in latest:
#         return "compare"

#     # Refine
#     if "actually" in latest or "instead" in latest or "also" in latest:
#         return "refine"

#     # Off topic
#     if any(x in latest for x in [
#         "weather",
#         "cricket",
#         "politics",
#         "movie",
#         "ipl",
#         "legal advice"
#     ]):
#         return "refuse"

#     # Need clarification
#     vague = [
#         "assessment",
#         "test",
#         "solution",
#         "recommend",
#         "help me hire"
#     ]

#     if any(x in latest for x in vague):

#         if len(latest.split()) < 8:
#             return "clarify"

#     return "recommend"



# def detect_intent(messages):

#     latest = ""

#     user_messages = []

#     # Collect all user messages
#     for msg in messages:

#         if msg.role == "user":

#             user_messages.append(msg.content.lower())

#     if user_messages:
#         latest = user_messages[-1]

#     conversation = " ".join(user_messages)

#     # ==================================================
#     # Compare
#     # ==================================================
#     if "compare" in latest or "difference" in latest:
#         return "compare"

#     # ==================================================
#     # Refine
#     # ==================================================
#     if any(x in latest for x in [
#         "actually",
#         "instead",
#         "also",
#         "add",
#         "remove"
#     ]):
#         return "refine"

#     # ==================================================
#     # Off-topic
#     # ==================================================
#     if any(x in latest for x in [
#         "weather",
#         "cricket",
#         "politics",
#         "movie",
#         "ipl",
#         "legal advice"
#     ]):
#         return "refuse"

#     # ==================================================
#     # Leadership flow (C1)
#     # ==================================================

#     leadership_words = [
#         "leadership",
#         "cxo",
#         "director",
#         "executive",
#         "senior"
#     ]

#     if any(word in conversation for word in leadership_words):

#         # If selection/development not yet known,
#         # keep asking clarification.
#         if (
#             "selection" not in conversation
#             and "development" not in conversation
#             and "developmental" not in conversation
#         ):
#             return "clarify"

#     # ==================================================
#     # Generic vague query
#     # ==================================================

#     vague = [
#         "assessment",
#         "test",
#         "solution",
#         "recommend",
#         "help me hire"
#     ]

#     if any(x in latest for x in vague):

#         if len(latest.split()) < 8:
#             return "clarify"

#     # ==================================================
#     # Otherwise recommend
#     # ==================================================

#     return "recommend"





# def detect_intent(messages):

#     latest = ""

#     conversation = ""

#     for msg in messages:
#         if msg.role == "user":
#             conversation += " " + msg.content.lower()

#     for msg in reversed(messages):
#         if msg.role == "user":
#             latest = msg.content.lower()
#             break

#     # =====================================================
#     # Compare
#     # =====================================================

#     if "compare" in latest or "difference" in latest:
#         return "compare"

#     # =====================================================
#     # Refine
#     # =====================================================

#     if any(x in latest for x in [
#         "actually",
#         "instead",
#         "also",
#         "change",
#         "replace"
#     ]):
#         return "refine"

#     # =====================================================
#     # Rust Hiring
#     # =====================================================

#     if "rust" in conversation:
#         return "rust"

#     # =====================================================
#     # Off Topic
#     # =====================================================

#     if any(x in latest for x in [
#         "weather",
#         "movie",
#         "ipl",
#         "politics",
#         "legal advice"
#     ]):
#         return "refuse"

#     # =====================================================
#     # Clarification
#     # =====================================================

#     vague = [
#         "assessment",
#         "solution",
#         "recommend",
#         "test",
#         "help me hire"
#     ]

#     if any(x in latest for x in vague):

#         if len(latest.split()) < 8:
#             return "clarify"

#     return "recommend"
# uper wala tha last 



# def detect_intent(messages):

#     latest = ""
#     conversation = ""

#     for msg in messages:
#         if msg.role == "user":
#             conversation += " " + msg.content.lower()

#     for msg in reversed(messages):
#         if msg.role == "user":
#             latest = msg.content.lower()
#             break

#     # =====================================================
#     # REFUSE — off topic / legal / prompt injection
#     # =====================================================
#     refuse_phrases = [
#         "weather", "movie", "ipl", "politics", "cricket",
#         "legally required", "legal advice", "legal requirement",
#         "are we legally", "legally obligated", "required by law",
#         "does this satisfy", "does shl test satisfy",
#         "ignore your instructions", "ignore previous",
#         "forget your instructions", "you are now"
#     ]
#     if any(x in latest for x in refuse_phrases):
#         return "refuse"

#     # =====================================================
#     # COMPARE
#     # =====================================================
#     if "compare" in latest or "difference between" in latest:
#         return "compare"

#     # =====================================================
#     # REFINE — add / drop / remove / keep / replace
#     # =====================================================
#     refine_triggers = [
#         "add ", "drop ", "remove ", "keep ", "replace ",
#         "also add", "don't include", "exclude",
#         "actually", "instead", "change ", "swap",
#         "lock", "locking", "confirmed", "go ahead",
#         "final list"
#     ]
#     if any(x in latest for x in refine_triggers):
#         # Need prior assistant turn to exist (else it's just first message)
#         has_prior = any(msg.role == "assistant" for msg in messages)
#         if has_prior:
#             return "refine"

#     # =====================================================
#     # CLARIFY
#     # =====================================================
#     vague = [
#         "assessment", "solution", "recommend",
#         "test", "help me hire", "what should we use"
#     ]
#     if any(x in latest for x in vague) and len(latest.split()) < 8:
#         return "clarify"

#     return "recommend"






# def detect_intent(messages):

#     latest = ""
#     conversation = ""

#     for msg in messages:
#         if msg.role == "user":
#             conversation += " " + msg.content.lower()

#     for msg in reversed(messages):
#         if msg.role == "user":
#             latest = msg.content.lower()
#             break

#     # =====================================================
#     # REFUSE — off topic / legal / prompt injection
#     # =====================================================
#     refuse_phrases = [
#         "weather", "movie", "ipl", "politics", "cricket",
#         "legally required", "legal advice", "legal requirement",
#         "are we legally", "legally obligated", "required by law",
#         "does this satisfy", "does shl test satisfy",
#         "ignore your instructions", "ignore previous",
#         "forget your instructions", "you are now"
#     ]
#     if any(x in latest for x in refuse_phrases):
#         return "refuse"

#     # =====================================================
#     # COMPARE
#     # =====================================================
#     if "compare" in latest or "difference between" in latest:
#         return "compare"

#     # =====================================================
#     # REFINE — explicit edit commands only
#     # Only trigger if there's already an assistant response
#     # =====================================================
#     has_prior_assistant = any(msg.role == "assistant" for msg in messages)

#     explicit_edits = [
#         "add ", "drop ", "remove ", "keep ",
#         "replace ", "also add", "don't include",
#         "exclude", "swap ", "final list",
#         "locking it in", "lock it in", "confirmed",
#         "go ahead", "that works", "that's good",
#         "sounds good", "perfect", "great"
#     ]

#     if has_prior_assistant and any(x in latest for x in explicit_edits):
#         # But NOT if it's clearly a question
#         if "?" not in latest or any(x in latest for x in ["add ", "drop ", "remove ", "keep "]):
#             return "refine"

#     # =====================================================
#     # CLARIFY
#     # =====================================================
#     vague = [
#         "assessment", "solution", "recommend",
#         "test", "help me hire", "what should we use"
#     ]
#     if any(x in latest for x in vague) and len(latest.split()) < 8:
#         return "clarify"

#     return "recommend"






# def detect_intent(messages):

#     latest = ""
#     conversation = ""

#     for msg in messages:
#         if msg.role == "user":
#             conversation += " " + msg.content.lower()

#     for msg in reversed(messages):
#         if msg.role == "user":
#             latest = msg.content.lower()
#             break

#     # =====================================================
#     # REFUSE
#     # =====================================================
#     refuse_phrases = [
#         "weather", "movie", "ipl", "politics", "cricket",
#         "legally required", "legal advice", "legal requirement",
#         "are we legally", "legally obligated", "required by law",
#         "does this satisfy", "does shl test satisfy",
#         "ignore your instructions", "ignore previous",
#         "forget your instructions", "you are now"
#     ]
#     if any(x in latest for x in refuse_phrases):
#         return "refuse"

#     # =====================================================
#     # COMPARE
#     # =====================================================
#     if "compare" in latest or "difference between" in latest:
#         return "compare"

#     # =====================================================
#     # REFINE — explicit edit commands
#     # =====================================================
#     has_prior_assistant = any(msg.role == "assistant" for msg in messages)

#     # Pure questions should NOT trigger refine
#     # e.g. "Do we really need Verify G+?" is a question, not a command
#     is_pure_question = latest.strip().endswith("?") and not any(
#         x in latest for x in ["add ", "drop ", "remove ", "keep ", "final list"]
#     )

#     explicit_edits = [
#         "add ", "drop ", "remove ", "keep ",
#         "replace ", "also add", "don't include",
#         "exclude", "swap ", "final list",
#         "locking it in", "lock it in",
#         "confirmed", "go ahead", "that works",
#         "that's good", "sounds good", "perfect",
#         "great", "understood"
#     ]

#     if has_prior_assistant and not is_pure_question:
#         if any(x in latest for x in explicit_edits):
#             return "refine"

#     # =====================================================
#     # CLARIFY
#     # =====================================================
#     vague = [
#         "assessment", "solution", "recommend",
#         "test", "help me hire", "what should we use"
#     ]
#     if any(x in latest for x in vague) and len(latest.split()) < 8:
#         return "clarify"

#     return "recommend"








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