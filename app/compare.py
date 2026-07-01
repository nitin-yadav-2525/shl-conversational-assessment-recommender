import re
from app.retriever import search_assessments

ALIASES = {
    "opq":       "Occupational Personality Questionnaire OPQ32r",
    "opq32":     "Occupational Personality Questionnaire OPQ32r",
    "opq32r":    "Occupational Personality Questionnaire OPQ32r",
    "verify g+": "SHL Verify Interactive G+",
    "verify":    "SHL Verify Interactive G+",
    "dsi":       "Dependability and Safety Instrument DSI",
    "mq":        "Motivation Questionnaire MQ",
}

# Map common short names to full catalog names
FULL_NAMES = {
    "contact center call simulation": "Contact Center Call Simulation (New)",
    "customer service phone simulation": "Customer Service Phone Simulation",
    "safety & dependability 8.0": "Manufac. & Indust. - Safety & Dependability 8.0",
    "safety and dependability 8.0": "Manufac. & Indust. - Safety & Dependability 8.0",
}


def _resolve(name: str) -> str:
    n = name.strip().lower()
    return ALIASES.get(n, FULL_NAMES.get(n, name.strip()))


def _extract_names(query: str):
    q = query.lower()
    for phrase in ["what's the difference between", "difference between",
                   "compare", "how does", "differ from", "different from",
                   "different to"]:
        q = q.replace(phrase, "|||")

    m = re.search(r"\|\|\|\s*(.+?)\s+and\s+(.+?)(?:\?|$)", q)
    if m:
        return [m.group(1).strip(), m.group(2).strip()]

    m = re.search(r"(.+?)\s+vs\.?\s+(.+?)(?:\?|$)", q)
    if m:
        return [m.group(1).strip(), m.group(2).strip()]

    return []


def _best_match(name: str):
    resolved = _resolve(name)
    found = search_assessments(resolved, top_k=5)
    if not found:
        return None
    query_words = [w for w in resolved.lower().split() if len(w) > 2]
    best = sorted(
        found,
        key=lambda x: sum(w in x["name"].lower() for w in query_words),
        reverse=True
    )
    return best[0]


def compare_assessments(query: str) -> str:
    names = _extract_names(query)
    results = []
    if len(names) >= 2:
        for name in names[:2]:
            match = _best_match(name)
            if match:
                results.append(match)
    else:
        results = search_assessments(query, top_k=2)

    seen = set()
    unique = []
    for r in results:
        if r["name"] not in seen:
            seen.add(r["name"])
            unique.append(r)

    if len(unique) < 2:
        return "I couldn't find two distinct SHL assessments to compare."

    def fmt(val):
        if isinstance(val, list):
            return ", ".join(val[:4]) if val else "N/A"
        return str(val) if val else "N/A"

    a, b = unique[0], unique[1]
    return f"""Comparison of SHL Assessments

1. {a['name']}
   • Test Type  : {fmt(a.get('test_type'))}
   • Job Levels : {fmt(a.get('job_levels'))}
   • Duration   : {a.get('duration') or 'N/A'}
   • URL        : {a['url']}

2. {b['name']}
   • Test Type  : {fmt(b.get('test_type'))}
   • Job Levels : {fmt(b.get('job_levels'))}
   • Duration   : {b.get('duration') or 'N/A'}
   • URL        : {b['url']}
"""