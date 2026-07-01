# def edit_recommendations(results, conversation):

#     conversation = conversation.lower()

#     filtered = []

#     # -----------------------------------
#     # Drop OPQ
#     # -----------------------------------
#     drop_opq = (
#         "drop opq" in conversation or
#         "remove opq" in conversation
#     )

#     # -----------------------------------
#     # Drop REST
#     # -----------------------------------
#     drop_rest = (
#         "drop rest" in conversation or
#         "remove rest" in conversation
#     )

#     # -----------------------------------
#     # Keep Verify G+
#     # -----------------------------------
#     keep_verify = (
#         "keep verify" in conversation or
#         "verify g+" in conversation
#     )

#     # -----------------------------------
#     # Filter
#     # -----------------------------------
#     for item in results:

#         name = item["name"].lower()

#         if drop_opq and "opq" in name:
#             continue

#         if drop_rest and "rest" in name:
#             continue

#         filtered.append(item)

#     # -----------------------------------
#     # Move Verify to top
#     # -----------------------------------
#     if keep_verify:

#         verify = []
#         others = []

#         for item in filtered:

#             if "verify" in item["name"].lower():
#                 verify.append(item)
#             else:
#                 others.append(item)

#         filtered = verify + others

#     return filtered[:5]

#upper wala tha last time




# from app.retriever import search_assessments


# def edit_recommendations(results, conversation):
#     conversation = conversation.lower()

#     # =============================================
#     # DROP rules
#     # =============================================
#     drop_rules = {
#         "opq":    ["drop opq", "remove opq", "drop the opq",
#                    "remove the opq", "without opq", "no opq"],
#         "rest":   ["drop rest", "remove rest", "drop the rest"],
#         "verify": ["drop verify", "remove verify"],
#     }

#     items_to_drop = set()
#     for keyword, triggers in drop_rules.items():
#         if any(t in conversation for t in triggers):
#             for item in results:
#                 if keyword in item["name"].lower():
#                     items_to_drop.add(item["name"])

#     filtered = [r for r in results if r["name"] not in items_to_drop]

#     # =============================================
#     # ADD rules — inject specific assessments
#     # =============================================
#     add_rules = {
#         "Amazon Web Services (AWS) Development (New)": [
#             "add aws", "also aws", "include aws"
#         ],
#         "Docker (New)": [
#             "add docker", "also docker", "include docker"
#         ],
#         "Spring Framework (New)": [
#             "add spring", "also spring"
#         ],
#         "SHL Verify Interactive G+": [
#             "add cognitive", "add verify", "add verify g+",
#             "keep verify g+", "keep verify"
#         ],
#         "SQL (New)": [
#             "add sql", "also sql"
#         ],
#     }

#     for assessment_name, triggers in add_rules.items():
#         if any(t in conversation for t in triggers):
#             already_in = any(
#                 assessment_name.lower() in r["name"].lower()
#                 for r in filtered
#             )
#             if not already_in:
#                 extra = search_assessments(assessment_name, top_k=1)
#                 if extra:
#                     filtered = [extra[0]] + filtered

#     # =============================================
#     # FINAL LIST override
#     # (e.g. "Final list: Verify G+ and Graduate Scenarios")
#     # =============================================
#     if "final list" in conversation:
#         # Try to parse explicit names after "final list:"
#         import re
#         m = re.search(r"final list[:\s]+(.*)", conversation)
#         if m:
#             items_str = m.group(1)
#             explicit_names = [x.strip() for x in re.split(r" and |,", items_str) if x.strip()]
#             if explicit_names:
#                 explicit_results = []
#                 for name in explicit_names:
#                     found = search_assessments(name, top_k=1)
#                     if found:
#                         explicit_results.append(found[0])
#                 if explicit_results:
#                     filtered = explicit_results

#     # =============================================
#     # PRIORITISE — move matching items to top
#     # =============================================
#     prioritise_rules = {
#         "verify": ["keep verify", "verify g+", "locking", "keep shl verify"],
#     }

#     for keyword, triggers in prioritise_rules.items():
#         if any(t in conversation for t in triggers):
#             top = [r for r in filtered if keyword in r["name"].lower()]
#             rest = [r for r in filtered if keyword not in r["name"].lower()]
#             filtered = top + rest
#             break

#     return filtered[:5]




# import re
# from app.retriever import search_assessments


# def dedup(results):
#     """Remove duplicate assessment names."""
#     seen = set()
#     out = []
#     for r in results:
#         if r["name"] not in seen:
#             seen.add(r["name"])
#             out.append(r)
#     return out


# def edit_recommendations(results, conversation):
#     conversation = conversation.lower()
#     original = list(results)  # keep backup

#     # =============================================
#     # DROP rules
#     # =============================================
#     drop_rules = {
#         "opq":  ["drop opq", "remove opq", "drop the opq",
#                  "remove the opq", "without opq", "no opq"],
#         "rest": ["drop rest", "remove rest", "drop the rest"],
#     }

#     items_to_drop = set()
#     for keyword, triggers in drop_rules.items():
#         if any(t in conversation for t in triggers):
#             for item in results:
#                 if keyword in item["name"].lower():
#                     items_to_drop.add(item["name"])

#     filtered = [r for r in results if r["name"] not in items_to_drop]

#     # If dropping emptied the list, fall back to original minus dropped
#     if not filtered and items_to_drop:
#         filtered = [r for r in original if r["name"] not in items_to_drop]
#         # If still empty, use original
#         if not filtered:
#             filtered = original

#     # =============================================
#     # ADD rules
#     # =============================================
#     add_rules = {
#         "Amazon Web Services (AWS) Development (New)": [
#             "add aws", "also aws", "include aws"
#         ],
#         "Docker (New)": [
#             "add docker", "also docker", "include docker"
#         ],
#         "Spring Framework (New)": [
#             "add spring", "also spring"
#         ],
#         "SHL Verify Interactive G+": [
#             "add cognitive", "add verify", "add verify g+",
#             "keep verify g+", "keep verify", "keep shl verify"
#         ],
#         "SQL (New)": [
#             "add sql", "also sql"
#         ],
#     }

#     for assessment_name, triggers in add_rules.items():
#         if any(t in conversation for t in triggers):
#             already_in = any(
#                 assessment_name.lower() in r["name"].lower()
#                 for r in filtered
#             )
#             if not already_in:
#                 extra = search_assessments(assessment_name, top_k=1)
#                 if extra:
#                     filtered = [extra[0]] + filtered

#     # =============================================
#     # FINAL LIST override
#     # =============================================
#     if "final list" in conversation:
#         m = re.search(r"final list[:\s]+(.*?)(?:\.|$)", conversation)
#         if m:
#             items_str = m.group(1)
#             explicit_names = [
#                 x.strip() for x in re.split(r"\band\b|,", items_str)
#                 if x.strip() and len(x.strip()) > 2
#             ]
#             if explicit_names:
#                 explicit_results = []
#                 seen_names = set()
#                 for name in explicit_names:
#                     found = search_assessments(name, top_k=2)
#                     if found:
#                         best = sorted(
#                             found,
#                             key=lambda x: sum(
#                                 w in x["name"].lower()
#                                 for w in name.split()
#                                 if len(w) > 2
#                             ),
#                             reverse=True
#                         )
#                         for b in best:
#                             if b["name"] not in seen_names:
#                                 seen_names.add(b["name"])
#                                 explicit_results.append(b)
#                                 break
#                 if explicit_results:
#                     filtered = explicit_results

#     # =============================================
#     # PRIORITISE — keep verify at top
#     # =============================================
#     prioritise_triggers = ["keep verify", "verify g+", "locking", "keep shl verify"]
#     if any(t in conversation for t in prioritise_triggers):
#         top  = [r for r in filtered if "verify" in r["name"].lower()]
#         rest = [r for r in filtered if "verify" not in r["name"].lower()]
#         filtered = top + rest

#     return dedup(filtered)[:5]




# import re
# from app.retriever import search_assessments


# def dedup(results):
#     seen = set()
#     out = []
#     for r in results:
#         if r["name"] not in seen:
#             seen.add(r["name"])
#             out.append(r)
#     return out


# def edit_recommendations(results, conversation):
#     conversation = conversation.lower()
#     original = list(results)

#     # =============================================
#     # DROP rules
#     # =============================================
#     drop_rules = {
#         "opq": [
#             "drop opq", "remove opq", "drop the opq", "remove the opq",
#             "without opq", "no opq", "remove opq32r", "drop opq32r",
#             "remove the opq32r", "drop the opq32r"
#         ],
#         "rest": ["drop rest", "remove rest", "drop the rest"],
#         "dsi":  ["drop dsi", "remove dsi"],
#     }

#     items_to_drop = set()
#     for keyword, triggers in drop_rules.items():
#         if any(t in conversation for t in triggers):
#             for item in results:
#                 if keyword in item["name"].lower():
#                     items_to_drop.add(item["name"])

#     filtered = [r for r in results if r["name"] not in items_to_drop]

#     # fallback if drop emptied list
#     if not filtered and items_to_drop:
#         filtered = [r for r in original if r["name"] not in items_to_drop]
#     if not filtered:
#         filtered = original

#     # =============================================
#     # ADD rules
#     # =============================================
#     # Detect "add X and Y" patterns too (not just "add X")
#     add_rules = {
#         "Amazon Web Services (AWS) Development (New)": [
#             "add aws", "also aws", "include aws", "aws development"
#         ],
#         "Docker (New)": [
#             "add docker", "also docker", "include docker",
#             "and docker", "docker (new)"
#         ],
#         "Spring Framework (New)": [
#             "add spring", "also spring"
#         ],
#         "SHL Verify Interactive G+": [
#             "add cognitive", "add verify g+", "keep verify g+",
#             "keep verify", "keep shl verify", "locking it in"
#         ],
#         "SQL (New)": [
#             "add sql", "also sql"
#         ],
#     }

#     # Only add Verify if it's a command, not a question
#     is_question = "?" in conversation.split()[-20:]  # last ~20 chars

#     for assessment_name, triggers in add_rules.items():
#         # Skip Verify add if it's just a question about it
#         if "verify" in assessment_name.lower() and is_question:
#             # Only add if explicitly "keep" or "locking"
#             if not any(t in conversation for t in ["keep verify", "locking"]):
#                 continue

#         if any(t in conversation for t in triggers):
#             already_in = any(
#                 assessment_name.lower() in r["name"].lower()
#                 for r in filtered
#             )
#             if not already_in:
#                 extra = search_assessments(assessment_name, top_k=1)
#                 if extra:
#                     filtered = [extra[0]] + filtered

#     # =============================================
#     # FINAL LIST override
#     # =============================================
#     if "final list" in conversation:
#         m = re.search(r"final list[:\s]+(.*?)(?:\.|$)", conversation)
#         if m:
#             items_str = m.group(1)
#             explicit_names = [
#                 x.strip() for x in re.split(r"\band\b|,", items_str)
#                 if x.strip() and len(x.strip()) > 2
#             ]
#             if explicit_names:
#                 explicit_results = []
#                 seen_names = set()
#                 for name in explicit_names:
#                     found = search_assessments(name, top_k=2)
#                     if found:
#                         best = sorted(
#                             found,
#                             key=lambda x: sum(
#                                 w in x["name"].lower()
#                                 for w in name.split()
#                                 if len(w) > 2
#                             ),
#                             reverse=True
#                         )
#                         for b in best:
#                             if b["name"] not in seen_names:
#                                 seen_names.add(b["name"])
#                                 explicit_results.append(b)
#                                 break
#                 if explicit_results:
#                     filtered = explicit_results

#     # =============================================
#     # PRIORITISE
#     # =============================================
#     if any(t in conversation for t in ["keep verify", "locking", "keep shl verify"]):
#         top  = [r for r in filtered if "verify" in r["name"].lower()]
#         rest = [r for r in filtered if "verify" not in r["name"].lower()]
#         filtered = top + rest

#     return dedup(filtered)[:5]






# import re
# from app.retriever import search_assessments


# def dedup(results):
#     seen = set()
#     out = []
#     for r in results:
#         if r["name"] not in seen:
#             seen.add(r["name"])
#             out.append(r)
#     return out


# def edit_recommendations(results, conversation):
#     conversation = conversation.lower()
#     original = list(results)

#     # =============================================
#     # DROP rules
#     # =============================================
#     drop_rules = {
#         "opq": [
#             "drop opq", "remove opq", "drop the opq", "remove the opq",
#             "without opq", "no opq",
#             "drop opq32r", "remove opq32r",
#             "drop the opq32r", "remove the opq32r",
#             "drop opq 32r", "remove opq 32r",
#         ],
#         "rest": ["drop rest", "remove rest", "drop the rest"],
#         # Drop DSI if user explicitly said the 8.0 bundle is right fit
#         "dsi": [
#             "drop dsi", "remove dsi",
#             "8.0 bundle is the right fit",
#             "8.0 bundle is right",
#             "bundle is the right fit",
#         ],
#     }

#     items_to_drop = set()
#     for keyword, triggers in drop_rules.items():
#         if any(t in conversation for t in triggers):
#             for item in results:
#                 if keyword in item["name"].lower():
#                     items_to_drop.add(item["name"])

#     filtered = [r for r in results if r["name"] not in items_to_drop]

#     # fallback if drop emptied list
#     if not filtered and items_to_drop:
#         filtered = [r for r in original if r["name"] not in items_to_drop]
#     if not filtered:
#         filtered = original

#     # =============================================
#     # ADD rules — only on EXPLICIT user commands
#     # NOT triggered by JD text or comparison mentions
#     # =============================================
#     add_rules = {
#         "Amazon Web Services (AWS) Development (New)": [
#             "add aws", "also add aws", "include aws", "add amazon web services"
#         ],
#         "Docker (New)": [
#             "add docker", "also add docker", "include docker", "add docker (new)"
#         ],
#         "Spring Framework (New)": [
#             "add spring", "also add spring"
#         ],
#         "SHL Verify Interactive G+": [
#             "add cognitive", "add verify g+",
#             "keep verify g+", "keep verify", "keep shl verify",
#             "locking it in"
#         ],
#         "SQL (New)": [
#             "add sql", "also add sql"
#         ],
#     }

#     # Only add Verify on explicit keep/add command, not if it's a question
#     latest_part = conversation.split()[-30:]  # last ~30 words
#     is_question_context = "?" in " ".join(latest_part) and not any(
#         x in " ".join(latest_part) for x in ["keep verify", "add verify", "locking"]
#     )

#     for assessment_name, triggers in add_rules.items():
#         if "verify" in assessment_name.lower() and is_question_context:
#             continue

#         if any(t in conversation for t in triggers):
#             already_in = any(
#                 assessment_name.lower() in r["name"].lower()
#                 for r in filtered
#             )
#             if not already_in:
#                 extra = search_assessments(assessment_name, top_k=1)
#                 if extra:
#                     filtered = [extra[0]] + filtered

#     # =============================================
#     # FINAL LIST override
#     # =============================================
#     if "final list" in conversation:
#         m = re.search(r"final list[:\s]+(.*?)(?:\.|$)", conversation)
#         if m:
#             items_str = m.group(1)
#             explicit_names = [
#                 x.strip() for x in re.split(r"\band\b|,", items_str)
#                 if x.strip() and len(x.strip()) > 2
#             ]
#             if explicit_names:
#                 explicit_results = []
#                 seen_names = set()
#                 for name in explicit_names:
#                     found = search_assessments(name, top_k=2)
#                     if found:
#                         best = sorted(
#                             found,
#                             key=lambda x: sum(
#                                 w in x["name"].lower()
#                                 for w in name.split()
#                                 if len(w) > 2
#                             ),
#                             reverse=True
#                         )
#                         for b in best:
#                             if b["name"] not in seen_names:
#                                 seen_names.add(b["name"])
#                                 explicit_results.append(b)
#                                 break
#                 if explicit_results:
#                     filtered = explicit_results

#     # =============================================
#     # PRIORITISE — keep verify at top
#     # =============================================
#     if any(t in conversation for t in ["keep verify", "locking", "keep shl verify"]):
#         top  = [r for r in filtered if "verify" in r["name"].lower()]
#         rest = [r for r in filtered if "verify" not in r["name"].lower()]
#         filtered = top + rest

#     return dedup(filtered)[:5]


#sabse best abhi tak uper wala 


# import re
# from app.retriever import search_assessments


# def dedup(results):
#     seen = set()
#     out = []
#     for r in results:
#         if r["name"] not in seen:
#             seen.add(r["name"])
#             out.append(r)
#     return out


# def _parse_add_items(conversation):
#     """
#     Extract items to add from patterns like:
#     - "add aws and docker"
#     - "add docker"
#     - "also add spring"
#     Returns set of lowercase tokens to add.
#     """
#     tokens = set()
#     # "add X and Y and Z"
#     for m in re.finditer(r"\badd\s+([\w\s]+?)(?:\.|,|$|\band\b(?!\s+\w+\s+and))", conversation):
#         chunk = m.group(1)
#         for part in re.split(r"\band\b|,", chunk):
#             t = part.strip().lower()
#             if t:
#                 tokens.add(t)

#     # Also handle "add X and Y" at end of sentence
#     for m in re.finditer(r"\badd\s+([\w]+)\s+and\s+([\w]+)", conversation):
#         tokens.add(m.group(1).strip().lower())
#         tokens.add(m.group(2).strip().lower())

#     return tokens


# def edit_recommendations(results, conversation):
#     conversation = conversation.lower()
#     original = list(results)

#     # =============================================
#     # DROP rules
#     # =============================================
#     drop_rules = {
#         "opq": [
#             "drop opq", "remove opq", "drop the opq", "remove the opq",
#             "without opq", "no opq",
#             "drop opq32r", "remove opq32r",
#             "drop the opq32r", "remove the opq32r",
#         ],
#         "rest": ["drop rest", "remove rest", "drop the rest"],
#         "dsi": [
#             "drop dsi", "remove dsi",
#             "8.0 bundle is the right fit",
#             "8.0 bundle is right",
#             "bundle is the right fit",
#         ],
#     }

#     items_to_drop = set()
#     drop_keywords = set()
#     for keyword, triggers in drop_rules.items():
#         if any(t in conversation for t in triggers):
#             items_to_drop.update(
#                 item["name"] for item in results
#                 if keyword in item["name"].lower()
#             )
#             drop_keywords.add(keyword)

#     filtered = [r for r in results if r["name"] not in items_to_drop]

#     # If drop emptied the list, do a FRESH search avoiding dropped keywords
#     if not filtered and drop_keywords:
#         # Build a query from conversation minus the drop keyword terms
#         fresh_query = conversation
#         for kw in drop_keywords:
#             fresh_query = fresh_query.replace(kw, "")
#         fresh_results = search_assessments(fresh_query.strip(), top_k=8)
#         filtered = [
#             r for r in fresh_results
#             if not any(kw in r["name"].lower() for kw in drop_keywords)
#         ]

#     if not filtered:
#         filtered = [r for r in original if r["name"] not in items_to_drop]

#     # =============================================
#     # ADD rules — parse "add X and Y" patterns
#     # =============================================
#     add_tokens = _parse_add_items(conversation)

#     # Also check explicit keyword triggers
#     explicit_add_map = {
#         "aws":     "Amazon Web Services (AWS) Development (New)",
#         "amazon":  "Amazon Web Services (AWS) Development (New)",
#         "docker":  "Docker (New)",
#         "spring":  "Spring Framework (New)",
#         "sql":     "SQL (New)",
#     }

#     for token, assessment_name in explicit_add_map.items():
#         if token in add_tokens:
#             already_in = any(
#                 token in r["name"].lower() for r in filtered
#             )
#             if not already_in:
#                 extra = search_assessments(assessment_name, top_k=1)
#                 if extra:
#                     filtered = [extra[0]] + filtered

#     # Verify G+ — only on explicit keep/add commands, not questions
#     verify_triggers = [
#         "keep verify g+", "keep verify", "keep shl verify",
#         "add cognitive", "add verify g+", "locking it in", "locking"
#     ]
#     latest_words = conversation.split()[-40:]
#     is_question = "?" in " ".join(latest_words) and not any(
#         t in " ".join(latest_words) for t in ["keep verify", "add verify", "locking"]
#     )
#     if not is_question and any(t in conversation for t in verify_triggers):
#         already_in = any("verify" in r["name"].lower() and "g+" in r["name"].lower() for r in filtered)
#         if not already_in:
#             extra = search_assessments("SHL Verify Interactive G+", top_k=1)
#             if extra:
#                 filtered = [extra[0]] + filtered

#     # =============================================
#     # FINAL LIST override
#     # =============================================
#     if "final list" in conversation:
#         m = re.search(r"final list[:\s]+(.*?)(?:\.|$)", conversation)
#         if m:
#             items_str = m.group(1)
#             explicit_names = [
#                 x.strip() for x in re.split(r"\band\b|,", items_str)
#                 if x.strip() and len(x.strip()) > 2
#             ]
#             if explicit_names:
#                 explicit_results = []
#                 seen_names = set()
#                 for name in explicit_names:
#                     found = search_assessments(name, top_k=2)
#                     if found:
#                         best = sorted(
#                             found,
#                             key=lambda x: sum(
#                                 w in x["name"].lower()
#                                 for w in name.split() if len(w) > 2
#                             ),
#                             reverse=True
#                         )
#                         for b in best:
#                             if b["name"] not in seen_names:
#                                 seen_names.add(b["name"])
#                                 explicit_results.append(b)
#                                 break
#                 if explicit_results:
#                     filtered = explicit_results

#     # =============================================
#     # PRIORITISE — verify at top on keep command
#     # =============================================
#     if any(t in conversation for t in ["keep verify", "locking", "keep shl verify"]):
#         top  = [r for r in filtered if "verify" in r["name"].lower()]
#         rest = [r for r in filtered if "verify" not in r["name"].lower()]
#         filtered = top + rest

#     return dedup(filtered)[:5]



# uper wala sabse best hai 


# import re
# from app.retriever import search_assessments


# def dedup(results):
#     seen = set()
#     out = []
#     for r in results:
#         if r["name"] not in seen:
#             seen.add(r["name"])
#             out.append(r)
#     return out


# def _parse_add_items(conversation):
#     """Extract tokens after 'add X and Y' patterns."""
#     tokens = set()
#     for m in re.finditer(r"\badd\s+([\w]+)\s+and\s+([\w]+)", conversation):
#         tokens.add(m.group(1).strip().lower())
#         tokens.add(m.group(2).strip().lower())
#     for m in re.finditer(r"\badd\s+([\w]+)(?:\s|$|\.)", conversation):
#         tokens.add(m.group(1).strip().lower())
#     return tokens


# def edit_recommendations(results, conversation):
#     conversation = conversation.lower()
#     original = list(results)

#     # =============================================
#     # DROP rules
#     # =============================================
#     drop_rules = {
#         "opq": [
#             "drop opq", "remove opq", "drop the opq", "remove the opq",
#             "without opq", "no opq",
#             "drop opq32r", "remove opq32r",
#             "drop the opq32r", "remove the opq32r",
#         ],
#         "rest": ["drop rest", "remove rest", "drop the rest"],
#         "dsi": [
#             "drop dsi", "remove dsi",
#             "8.0 bundle is the right fit",
#             "8.0 bundle is right",
#             "bundle is the right fit",
#         ],
#     }

#     items_to_drop = set()
#     drop_keywords = set()
#     for keyword, triggers in drop_rules.items():
#         if any(t in conversation for t in triggers):
#             items_to_drop.update(
#                 item["name"] for item in results
#                 if keyword in item["name"].lower()
#             )
#             drop_keywords.add(keyword)

#     filtered = [r for r in results if r["name"] not in items_to_drop]

#     # If drop emptied the list, fresh search without dropped keywords
#     if not filtered and drop_keywords:
#         fresh_query = conversation
#         for kw in drop_keywords:
#             fresh_query = fresh_query.replace(kw, "")
#         fresh_results = search_assessments(fresh_query.strip(), top_k=8)
#         filtered = [
#             r for r in fresh_results
#             if not any(kw in r["name"].lower() for kw in drop_keywords)
#         ]

#     if not filtered:
#         filtered = [r for r in original if r["name"] not in items_to_drop]

#     # =============================================
#     # ADD rules
#     # =============================================
#     add_tokens = _parse_add_items(conversation)

#     explicit_add_map = {
#         "aws":    "Amazon Web Services (AWS) Development (New)",
#         "amazon": "Amazon Web Services (AWS) Development (New)",
#         "docker": "Docker (New)",
#         "spring": "Spring Framework (New)",
#         "sql":    "SQL (New)",
#         "mq":     "OPQ MQ Sales Report",
#     }

#     for token, assessment_name in explicit_add_map.items():
#         if token in add_tokens:
#             already_in = any(token in r["name"].lower() for r in filtered)
#             if not already_in:
#                 extra = search_assessments(assessment_name, top_k=1)
#                 if extra:
#                     filtered = [extra[0]] + filtered

#     # Verify G+ — explicit keep/add commands only
#     verify_triggers = [
#         "keep verify g+", "keep verify", "keep shl verify",
#         "add cognitive", "add verify g+", "locking it in", "locking"
#     ]
#     latest_words = " ".join(conversation.split()[-40:])
#     is_question = "?" in latest_words and not any(
#         t in latest_words for t in ["keep verify", "add verify", "locking"]
#     )
#     if not is_question and any(t in conversation for t in verify_triggers):
#         already_in = any(
#             "verify" in r["name"].lower() and "g+" in r["name"].lower()
#             for r in filtered
#         )
#         if not already_in:
#             extra = search_assessments("SHL Verify Interactive G+", top_k=1)
#             if extra:
#                 filtered = [extra[0]] + filtered

#     # =============================================
#     # FINAL LIST override
#     # =============================================
#     if "final list" in conversation:
#         m = re.search(r"final list[:\s]+(.*?)(?:\.|$)", conversation)
#         if m:
#             items_str = m.group(1)
#             explicit_names = [
#                 x.strip() for x in re.split(r"\band\b|,", items_str)
#                 if x.strip() and len(x.strip()) > 2
#             ]
#             if explicit_names:
#                 explicit_results = []
#                 seen_names = set()
#                 for name in explicit_names:
#                     found = search_assessments(name, top_k=2)
#                     if found:
#                         best = sorted(
#                             found,
#                             key=lambda x: sum(
#                                 w in x["name"].lower()
#                                 for w in name.split() if len(w) > 2
#                             ),
#                             reverse=True
#                         )
#                         for b in best:
#                             if b["name"] not in seen_names:
#                                 seen_names.add(b["name"])
#                                 explicit_results.append(b)
#                                 break
#                 if explicit_results:
#                     filtered = explicit_results

#     # =============================================
#     # PRIORITISE — verify at top on keep command
#     # =============================================
#     if any(t in conversation for t in ["keep verify", "locking", "keep shl verify"]):
#         top  = [r for r in filtered if "verify" in r["name"].lower()]
#         rest = [r for r in filtered if "verify" not in r["name"].lower()]
#         filtered = top + rest

#     return dedup(filtered)[:5]


# abhi tak ka sabse best uper wala 


# import re
# from app.retriever import search_assessments


# def dedup(results):
#     seen = set()
#     out = []
#     for r in results:
#         if r["name"] not in seen:
#             seen.add(r["name"])
#             out.append(r)
#     return out


# def _parse_add_items(conversation):
#     """Extract tokens after 'add X and Y' patterns."""
#     tokens = set()
#     for m in re.finditer(r"\badd\s+([\w]+)\s+and\s+([\w]+)", conversation):
#         tokens.add(m.group(1).strip().lower())
#         tokens.add(m.group(2).strip().lower())
#     for m in re.finditer(r"\badd\s+([\w]+)(?:\s|$|\.)", conversation):
#         tokens.add(m.group(1).strip().lower())
#     return tokens


# def edit_recommendations(results, conversation):
#     conversation = conversation.lower()
#     original = list(results)

#     # =============================================
#     # DROP rules
#     # =============================================
#     drop_rules = {
#         "opq": [
#             "drop opq", "remove opq", "drop the opq", "remove the opq",
#             "without opq", "no opq",
#             "drop opq32r", "remove opq32r",
#             "drop the opq32r", "remove the opq32r",
#         ],
#         "rest": ["drop rest", "remove rest", "drop the rest"],
#         "dsi": [
#             "drop dsi", "remove dsi",
#             "8.0 bundle is the right fit",
#             "8.0 bundle is right",
#             "bundle is the right fit",
#         ],
#     }

#     items_to_drop = set()
#     drop_keywords = set()
#     for keyword, triggers in drop_rules.items():
#         if any(t in conversation for t in triggers):
#             items_to_drop.update(
#                 item["name"] for item in results
#                 if keyword in item["name"].lower()
#             )
#             drop_keywords.add(keyword)

#     filtered = [r for r in results if r["name"] not in items_to_drop]

#     # If drop emptied the list, fresh search without dropped keywords
#     if not filtered and drop_keywords:
#         fresh_query = conversation
#         for kw in drop_keywords:
#             fresh_query = fresh_query.replace(kw, "")
#         fresh_results = search_assessments(fresh_query.strip(), top_k=8)
#         filtered = [
#             r for r in fresh_results
#             if not any(kw in r["name"].lower() for kw in drop_keywords)
#         ]

#     if not filtered:
#         filtered = [r for r in original if r["name"] not in items_to_drop]

#     # =============================================
#     # ADD rules
#     # =============================================
#     add_tokens = _parse_add_items(conversation)

#     explicit_add_map = {
#         "aws":    "Amazon Web Services (AWS) Development (New)",
#         "amazon": "Amazon Web Services (AWS) Development (New)",
#         "docker": "Docker (New)",
#         "spring": "Spring Framework (New)",
#         "sql":    "SQL (New)",
#         "mq":     "OPQ MQ Sales Report",
#     }

#     for token, assessment_name in explicit_add_map.items():
#         if token in add_tokens:
#             already_in = any(token in r["name"].lower() for r in filtered)
#             if not already_in:
#                 extra = search_assessments(assessment_name, top_k=1)
#                 if extra:
#                     filtered = [extra[0]] + filtered

#     # Verify G+ — explicit keep/add commands only
#     verify_triggers = [
#         "keep verify g+", "keep verify", "keep shl verify",
#         "add cognitive", "add verify g+", "locking it in", "locking"
#     ]
#     latest_words = " ".join(conversation.split()[-40:])
#     is_question = "?" in latest_words and not any(
#         t in latest_words for t in ["keep verify", "add verify", "locking"]
#     )
#     if not is_question and any(t in conversation for t in verify_triggers):
#         already_in = any(
#             "verify" in r["name"].lower() and "g+" in r["name"].lower()
#             for r in filtered
#         )
#         if not already_in:
#             extra = search_assessments("SHL Verify Interactive G+", top_k=1)
#             if extra:
#                 filtered = [extra[0]] + filtered

#     # =============================================
#     # FINAL LIST override
#     # =============================================
#     if "final list" in conversation:
#         m = re.search(r"final list[:\s]+(.*?)(?:\.|$)", conversation)
#         if m:
#             items_str = m.group(1)
#             explicit_names = [
#                 x.strip() for x in re.split(r"\band\b|,", items_str)
#                 if x.strip() and len(x.strip()) > 2
#             ]
#             if explicit_names:
#                 explicit_results = []
#                 seen_names = set()
#                 for name in explicit_names:
#                     found = search_assessments(name, top_k=2)
#                     if found:
#                         best = sorted(
#                             found,
#                             key=lambda x: sum(
#                                 w in x["name"].lower()
#                                 for w in name.split() if len(w) > 2
#                             ),
#                             reverse=True
#                         )
#                         for b in best:
#                             if b["name"] not in seen_names:
#                                 seen_names.add(b["name"])
#                                 explicit_results.append(b)
#                                 break
#                 if explicit_results:
#                     filtered = explicit_results

#     # =============================================
#     # DROP Virtual Assessment in office/admin context
#     # =============================================
#     if any(x in conversation for x in ["excel", "word", "admin assistant", "microsoft office"]):
#         filtered = [r for r in filtered if "virtual assessment" not in r["name"].lower()]

#     # =============================================
#     # PRIORITISE — verify at top on keep command
#     # =============================================
#     if any(t in conversation for t in ["keep verify", "locking", "keep shl verify"]):
#         top  = [r for r in filtered if "verify" in r["name"].lower()]
#         rest = [r for r in filtered if "verify" not in r["name"].lower()]
#         filtered = top + rest

#     return dedup(filtered)[:5]


# # This function patches virtual assessment removal — called at end of edit_recommendations
# # Already handled above in the main function; this is just a safety net reminder.





#abhi tak ka sabse best ye hai ye uper wala 

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