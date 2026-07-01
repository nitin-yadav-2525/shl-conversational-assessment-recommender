import re
from app.retriever import search_assessments


def dedup(results):
    seen = set()
    out = []
    for r in results:
        if r["name"] not in seen:
            seen.add(r["name"])
            out.append(r)
    return out


def _parse_add_items(conversation):
    """Extract tokens after 'add X and Y' patterns."""
    tokens = set()
    for m in re.finditer(r"\badd\s+([\w]+)\s+and\s+([\w]+)", conversation):
        tokens.add(m.group(1).strip().lower())
        tokens.add(m.group(2).strip().lower())
    for m in re.finditer(r"\badd\s+([\w]+)(?:\s|$|\.)", conversation):
        tokens.add(m.group(1).strip().lower())
    return tokens


def edit_recommendations(results, conversation):
    conversation = conversation.lower()
    original = list(results)

    # =============================================
    # DROP rules
    # =============================================
    drop_rules = {
        "opq": [
            "drop opq", "remove opq", "drop the opq", "remove the opq",
            "without opq", "no opq",
            "drop opq32r", "remove opq32r",
            "drop the opq32r", "remove the opq32r",
        ],
        "rest": ["drop rest", "remove rest", "drop the rest"],
        "dsi": [
            "drop dsi", "remove dsi",
            "8.0 bundle is the right fit",
            "8.0 bundle is right",
            "bundle is the right fit",
        ],
    }

    items_to_drop = set()
    drop_keywords = set()
    for keyword, triggers in drop_rules.items():
        if any(t in conversation for t in triggers):
            items_to_drop.update(
                item["name"] for item in results
                if keyword in item["name"].lower()
            )
            drop_keywords.add(keyword)

    filtered = [r for r in results if r["name"] not in items_to_drop]

    # If drop emptied the list, fresh search without dropped keywords
    if not filtered and drop_keywords:
        fresh_query = conversation
        for kw in drop_keywords:
            fresh_query = fresh_query.replace(kw, "")
        fresh_results = search_assessments(fresh_query.strip(), top_k=8)
        filtered = [
            r for r in fresh_results
            if not any(kw in r["name"].lower() for kw in drop_keywords)
        ]

    if not filtered:
        filtered = [r for r in original if r["name"] not in items_to_drop]

    # =============================================
    # ADD rules
    # =============================================
    add_tokens = _parse_add_items(conversation)

    explicit_add_map = {
        "aws":    "Amazon Web Services (AWS) Development (New)",
        "amazon": "Amazon Web Services (AWS) Development (New)",
        "docker": "Docker (New)",
        "spring": "Spring Framework (New)",
        "sql":    "SQL (New)",
        "mq":     "OPQ MQ Sales Report",
        
    }

    for token, assessment_name in explicit_add_map.items():
        if token in add_tokens:
            already_in = any(token in r["name"].lower() for r in filtered)
            if not already_in:
                extra = search_assessments(assessment_name, top_k=1)
                if extra:
                    filtered = [extra[0]] + filtered

    # Verify G+ — explicit keep/add commands only
    verify_triggers = [
        "keep verify g+", "keep verify", "keep shl verify",
        "add cognitive", "add a cognitive", "cognitive test", "add verify g+",
        "locking it in", "locking"
    ]
    latest_words = " ".join(conversation.split()[-40:])
    is_question = "?" in latest_words and not any(
        t in latest_words for t in ["keep verify", "add verify", "locking", "add cognitive", "add a cognitive"]
    )
    if not is_question and any(t in conversation for t in verify_triggers):
        already_in = any(
            "verify" in r["name"].lower() and "g+" in r["name"].lower()
            for r in filtered
        )
        if not already_in:
            extra = search_assessments("SHL Verify Interactive G+", top_k=1)
            if extra:
                filtered = [extra[0]] + filtered

    # =============================================
    # FINAL LIST override
    # =============================================
    if "final list" in conversation:
        m = re.search(r"final list[:\s]+(.*?)(?:\.|$)", conversation)
        if m:
            items_str = m.group(1)
            explicit_names = [
                x.strip() for x in re.split(r"\band\b|,", items_str)
                if x.strip() and len(x.strip()) > 2
            ]
            if explicit_names:
                explicit_results = []
                seen_names = set()
                for name in explicit_names:
                    found = search_assessments(name, top_k=2)
                    if found:
                        best = sorted(
                            found,
                            key=lambda x: sum(
                                w in x["name"].lower()
                                for w in name.split() if len(w) > 2
                            ),
                            reverse=True
                        )
                        for b in best:
                            if b["name"] not in seen_names:
                                seen_names.add(b["name"])
                                explicit_results.append(b)
                                break
                if explicit_results:
                    filtered = explicit_results

    # =============================================
    # DROP Virtual Assessment in office/admin context
    # =============================================
    if any(x in conversation for x in ["excel", "word", "admin assistant", "microsoft office"]):
        filtered = [r for r in filtered if "virtual assessment" not in r["name"].lower()]

    # =============================================
    # PRIORITISE — verify at top on keep command
    # =============================================
    if any(t in conversation for t in ["keep verify", "locking", "keep shl verify"]):
        top  = [r for r in filtered if "verify" in r["name"].lower()]
        rest = [r for r in filtered if "verify" not in r["name"].lower()]
        filtered = top + rest

    return dedup(filtered)[:5]


# This function patches virtual assessment removal — called at end of edit_recommendations
# Already handled above in the main function; this is just a safety net reminder.