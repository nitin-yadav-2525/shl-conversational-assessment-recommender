# from app.retriever import search_assessments


# def compare_assessments(query: str):

#     results = search_assessments(query, top_k=2)

#     if len(results) < 2:
#         return "I couldn't find two matching SHL assessments to compare."

#     first = results[0]
#     second = results[1]

#     comparison = f"""
# Comparison of SHL Assessments

# 1. {first['name']}
#    • Test Type : {', '.join(first['test_type'])}
#    • Duration : {first['duration']}
#    • URL : {first['url']}

# 2. {second['name']}
#    • Test Type : {', '.join(second['test_type'])}
#    • Duration : {second['duration']}
#    • URL : {second['url']}
# """

#     return comparison

#last time upper wala tha 

# import re
# from app.retriever import search_assessments


# def _extract_names(query: str):
#     """
#     Try to extract two assessment names from a query like:
#     'difference between OPQ and MQ Sales Report'
#     'compare DSI and Safety & Dependability 8.0'
#     """

#     q = query.lower()

#     # Remove filler phrases
#     for phrase in ["what's the difference between", "difference between",
#                    "compare", "what is the difference between",
#                    "how does", "differ from", "vs", "versus"]:
#         q = q.replace(phrase, "|")

#     # Split on "and" or "|"
#     parts = re.split(r"\band\b|\|", q)
#     parts = [p.strip() for p in parts if p.strip()]

#     return parts if len(parts) >= 2 else []


# def compare_assessments(query: str) -> str:

#     names = _extract_names(query)

#     if len(names) >= 2:
#         r1 = search_assessments(names[0], top_k=1)
#         r2 = search_assessments(names[1], top_k=1)
#         results = []
#         if r1:
#             results.append(r1[0])
#         if r2:
#             results.append(r2[0])
#     else:
#         results = search_assessments(query, top_k=2)

#     if len(results) < 2:
#         return "I couldn't find two matching SHL assessments to compare."

#     first  = results[0]
#     second = results[1]

#     def fmt_types(item):
#         types = item.get("test_type", [])
#         if isinstance(types, list):
#             return ", ".join(types) if types else "N/A"
#         return str(types)

#     def fmt_levels(item):
#         levels = item.get("job_levels", [])
#         if isinstance(levels, list):
#             return ", ".join(levels[:4]) if levels else "N/A"
#         return str(levels)

#     comparison = f"""Comparison of SHL Assessments

# 1. {first['name']}
#    • Test Type  : {fmt_types(first)}
#    • Job Levels : {fmt_levels(first)}
#    • Duration   : {first.get('duration', 'N/A') or 'N/A'}
#    • URL        : {first['url']}

# 2. {second['name']}
#    • Test Type  : {fmt_types(second)}
#    • Job Levels : {fmt_levels(second)}
#    • Duration   : {second.get('duration', 'N/A') or 'N/A'}
#    • URL        : {second['url']}
# """

#     return comparison


# import re
# from app.retriever import search_assessments


# def _extract_names(query: str):
#     q = query.lower()

#     # "difference between X and Y"
#     m = re.search(r"difference between (.+?) and (.+?)(?:\?|$)", q)
#     if m:
#         return [m.group(1).strip(), m.group(2).strip()]

#     # "compare X and Y"
#     m = re.search(r"compare (.+?) and (.+?)(?:\?|$)", q)
#     if m:
#         return [m.group(1).strip(), m.group(2).strip()]

#     # "X vs Y"
#     m = re.search(r"(.+?) vs\.? (.+?)(?:\?|$)", q)
#     if m:
#         return [m.group(1).strip(), m.group(2).strip()]

#     return []


# def compare_assessments(query: str) -> str:

#     names = _extract_names(query)

#     results = []

#     if len(names) >= 2:
#         # Search each name separately to get the most relevant match
#         for name in names[:2]:
#             found = search_assessments(name, top_k=3)
#             # Pick the one whose name best matches
#             if found:
#                 best = sorted(
#                     found,
#                     key=lambda x: sum(
#                         w in x["name"].lower()
#                         for w in name.split()
#                         if len(w) > 2
#                     ),
#                     reverse=True
#                 )
#                 results.append(best[0])
#     else:
#         results = search_assessments(query, top_k=2)

#     # Deduplicate
#     seen = set()
#     unique = []
#     for r in results:
#         if r["name"] not in seen:
#             seen.add(r["name"])
#             unique.append(r)

#     if len(unique) < 2:
#         return "I couldn't find two distinct SHL assessments to compare based on your query."

#     first  = unique[0]
#     second = unique[1]

#     def fmt(val):
#         if isinstance(val, list):
#             return ", ".join(val[:4]) if val else "N/A"
#         return str(val) if val else "N/A"

#     return f"""Comparison of SHL Assessments

# 1. {first['name']}
#    • Test Type  : {fmt(first.get('test_type'))}
#    • Job Levels : {fmt(first.get('job_levels'))}
#    • Duration   : {first.get('duration') or 'N/A'}
#    • URL        : {first['url']}

# 2. {second['name']}
#    • Test Type  : {fmt(second.get('test_type'))}
#    • Job Levels : {fmt(second.get('job_levels'))}
#    • Duration   : {second.get('duration') or 'N/A'}
#    • URL        : {second['url']}
# """

#upper wala last tha 


# import re
# from app.retriever import search_assessments

# # Map short aliases to full search terms
# ALIASES = {
#     "opq":           "Occupational Personality Questionnaire OPQ32r",
#     "opq32":         "Occupational Personality Questionnaire OPQ32r",
#     "opq32r":        "Occupational Personality Questionnaire OPQ32r",
#     "verify g+":     "SHL Verify Interactive G+",
#     "verify":        "SHL Verify Interactive G+",
#     "dsi":           "Dependability and Safety Instrument DSI",
#     "mq":            "Motivation Questionnaire MQ",
#     "gsma":          "Graduate Scenarios",
# }


# def _resolve(name: str) -> str:
#     """Expand short alias to full search term."""
#     n = name.strip().lower()
#     return ALIASES.get(n, name.strip())


# def _extract_names(query: str):
#     q = query.lower()

#     # "difference between X and Y"
#     m = re.search(r"difference between (.+?) and (.+?)(?:\?|$)", q)
#     if m:
#         return [m.group(1).strip(), m.group(2).strip()]

#     # "compare X and Y"
#     m = re.search(r"compare (.+?) and (.+?)(?:\?|$)", q)
#     if m:
#         return [m.group(1).strip(), m.group(2).strip()]

#     # "X vs Y"
#     m = re.search(r"(.+?) vs\.? (.+?)(?:\?|$)", q)
#     if m:
#         return [m.group(1).strip(), m.group(2).strip()]

#     return []


# def _best_match(name: str):
#     """Search and pick the result whose name best matches the query."""
#     resolved = _resolve(name)
#     found = search_assessments(resolved, top_k=5)
#     if not found:
#         return None

#     query_words = [w for w in resolved.lower().split() if len(w) > 2]

#     best = sorted(
#         found,
#         key=lambda x: sum(w in x["name"].lower() for w in query_words),
#         reverse=True
#     )
#     return best[0]


# def compare_assessments(query: str) -> str:
#     names = _extract_names(query)

#     results = []
#     if len(names) >= 2:
#         for name in names[:2]:
#             match = _best_match(name)
#             if match:
#                 results.append(match)
#     else:
#         results = search_assessments(query, top_k=2)

#     # Deduplicate
#     seen = set()
#     unique = []
#     for r in results:
#         if r["name"] not in seen:
#             seen.add(r["name"])
#             unique.append(r)

#     if len(unique) < 2:
#         return "I couldn't find two distinct SHL assessments to compare."

#     def fmt(val):
#         if isinstance(val, list):
#             return ", ".join(val[:4]) if val else "N/A"
#         return str(val) if val else "N/A"

#     a, b = unique[0], unique[1]
#     return f"""Comparison of SHL Assessments

# 1. {a['name']}
#    • Test Type  : {fmt(a.get('test_type'))}
#    • Job Levels : {fmt(a.get('job_levels'))}
#    • Duration   : {a.get('duration') or 'N/A'}
#    • URL        : {a['url']}

# 2. {b['name']}
#    • Test Type  : {fmt(b.get('test_type'))}
#    • Job Levels : {fmt(b.get('job_levels'))}
#    • Duration   : {b.get('duration') or 'N/A'}
#    • URL        : {b['url']}
# """





# abhi tak ka best uper wala 





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