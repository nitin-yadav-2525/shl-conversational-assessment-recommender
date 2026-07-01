# def recommend(results, query):

#     query = query.lower()

#     reranked = []

#     # ==========================================================
#     # Helper Function
#     # ==========================================================

#     def add_priority(priority):

#         added = set()

#         for name in priority:

#             for item in results:

#                 if item["name"].lower() == name.lower():

#                     reranked.append(item)

#                     added.add(item["name"])

#         for item in results:

#             if item["name"] not in added:

#                 reranked.append(item)

#         return reranked[:5]

#     # ==========================================================
#     # Leadership
#     # ==========================================================

#     if any(x in query for x in [
#         "leadership",
#         "leader",
#         "executive",
#         "director",
#         "cxo",
#         "benchmark"
#     ]):

#         return add_priority([

#             "Occupational Personality Questionnaire OPQ32r",

#             "OPQ Leadership Report",

#             "OPQ Universal Competency Report 2.0",

#             "OPQ Universal Competency Report 1.0",

#             "OPQ Premium Plus Report 2.0"

#         ])

#     # ==========================================================
#     # Java
#     # ==========================================================

#     if "java" in query:

#         return add_priority([

#             "Java 8 (New)",

#             "Core Java (Advanced Level) (New)",

#             "Core Java (Entry Level) (New)",

#             "Java Web Services (New)",

#             "Java Frameworks (New)"

#         ])

#     # ==========================================================
#     # Rust
#     # ==========================================================

#     if "rust" in query:

#         return add_priority([

#             "Smart Interview Live Coding",

#             "Linux Programming (General)",

#             "Networking and Implementation (New)",

#             "SHL Verify Interactive G+",

#             "Occupational Personality Questionnaire OPQ32r"

#         ])

#     # ==========================================================
#     # Graduate
#     # ==========================================================

#     if "graduate" in query:

#         return add_priority([

#             "Graduate Scenarios",

#             "Graduate Scenarios Profile Report",

#             "Graduate Scenarios Narrative Report",

#             "SHL Verify Interactive G+",

#             "Occupational Personality Questionnaire OPQ32r"

#         ])

#     # ==========================================================
#     # Contact Center
#     # ==========================================================

#     if any(x in query for x in [
#         "contact centre",
#         "contact center",
#         "customer service",
#         "call centre",
#         "call center"
#     ]):

#         return add_priority([

#             "Contact Center Call Simulation (New)",

#             "Customer Service Phone Simulation",

#             "Sales & Service Phone Solution",

#             "Entry Level Customer Service (General) Solution"

#         ])

#     # ==========================================================
#     # Safety / Manufacturing
#     # ==========================================================

#     if any(x in query for x in [
#         "plant",
#         "chemical",
#         "manufacturing",
#         "industrial",
#         "safety"
#     ]):

#         return add_priority([

#             "Manufac. & Indust. - Safety & Dependability 8.0",

#             "Manufacturing & Industrial - Essential Focus 8.0",

#             "Manufacturing & Industrial - Vigilance Focus 8.0",

#             "Manufac. & Indust. - Mechanical & Vigilance 8.0",

#             "Manufacturing & Industrial - Mechanical Focus 8.0"

#         ])

#     # ==========================================================
#     # Healthcare
#     # ==========================================================

#     if any(x in query for x in [

#         "hipaa",

#         "patient",

#         "healthcare",

#         "hospital"

#     ]):

#         return add_priority([

#             "HIPAA (Security)",

#             "Written Spanish",

#             "Written English v1",

#             "SVAR - Spoken Spanish (North American) (New)",

#             "SVAR - Spoken Spanish (Castilian) (New)"

#         ])

#     # ==========================================================
#     # Excel / Word
#     # ==========================================================

#     if any(x in query for x in [

#         "excel",

#         "word",

#         "admin assistant"

#     ]):

#         return add_priority([

#             "Microsoft Excel 365 - Essentials (New)",

#             "Microsoft Word 365 (New)",

#             "Conversational Multichat Simulation",

#             "Smart Interview Live"

#         ])

#     # ==========================================================
#     # Verify
#     # ==========================================================

#     if "verify g+" in query or "cognitive" in query:

#         return add_priority([

#             "SHL Verify Interactive G+",

#             "Verify - G+",

#             "Verify G+ - Ability Test Report",

#             "Verify G+ - Candidate Report"

#         ])

#     # ==========================================================
#     # AWS
#     # ==========================================================

#     if "aws" in query:

#         return add_priority([

#             "Amazon Web Services (AWS) Development (New)"

#         ])

#     # ==========================================================
#     # Docker
#     # ==========================================================

#     if "docker" in query:

#         return add_priority([

#             "Docker (New)"

#         ])

#     # ==========================================================
#     # Python
#     # ==========================================================

#     if "python" in query:

#         return add_priority([

#             "Python (New)"

#         ])

#     # ==========================================================
#     # SQL
#     # ==========================================================

#     if "sql" in query:

#         return add_priority([

#             "SQL (New)",

#             "SQL Server (New)"

#         ])

#     return results







# from app.retriever import search_assessments


# def recommend(results, query):
#     query = query.lower()
#     reranked = []

#     def add_priority(priority):
#         added = set()
#         for name in priority:
#             for item in results:
#                 if item["name"].lower() == name.lower():
#                     reranked.append(item)
#                     added.add(item["name"])
#         for item in results:
#             if item["name"] not in added:
#                 reranked.append(item)
#         return reranked[:5]

#     # ==========================================
#     # Leadership
#     # ==========================================
#     if any(x in query for x in ["leadership", "leader", "executive", "director", "cxo", "benchmark"]):
#         return add_priority([
#             "Occupational Personality Questionnaire OPQ32r",
#             "OPQ Leadership Report",
#             "OPQ Universal Competency Report 2.0",
#             "OPQ Universal Competency Report 1.0",
#             "OPQ Premium Plus Report 2.0"
#         ])

#     # ==========================================
#     # Java
#     # ==========================================
#     if "java" in query and "javascript" not in query:
#         return add_priority([
#             "Java 8 (New)",
#             "Core Java (Advanced Level) (New)",
#             "Core Java (Entry Level) (New)",
#             "Java Web Services (New)",
#             "Java Frameworks (New)"
#         ])

#     # ==========================================
#     # Graduate
#     # ==========================================
#     if "graduate" in query:
#         return add_priority([
#             "Graduate Scenarios",
#             "Graduate Scenarios Profile Report",
#             "Graduate Scenarios Narrative Report",
#             "SHL Verify Interactive G+",
#             "Occupational Personality Questionnaire OPQ32r"
#         ])

#     # ==========================================
#     # Contact Center / Customer Service
#     # ==========================================
#     if any(x in query for x in ["contact centre", "contact center", "customer service", "call centre", "call center"]):
#         return add_priority([
#             "Contact Center Call Simulation (New)",
#             "Customer Service Phone Simulation",
#             "Sales & Service Phone Solution",
#             "Entry Level Customer Service (General) Solution",
#             "Sales & Service Phone Simulation"
#         ])

#     # ==========================================
#     # Safety / Manufacturing
#     # ==========================================
#     if any(x in query for x in ["plant", "chemical", "manufacturing", "industrial", "safety"]):
#         return add_priority([
#             "Manufac. & Indust. - Safety & Dependability 8.0",
#             "Manufacturing & Industrial - Essential Focus 8.0",
#             "Manufacturing & Industrial - Vigilance Focus 8.0",
#             "Manufac. & Indust. - Mechanical & Vigilance 8.0",
#             "Manufacturing & Industrial - Mechanical Focus 8.0"
#         ])

#     # ==========================================
#     # Healthcare / HIPAA — boost HIPAA to top
#     # ==========================================
#     if any(x in query for x in ["hipaa", "patient", "healthcare", "hospital", "bilingual", "spanish"]):
#         # Check if English + Spanish hybrid
#         if "english" in query and "spanish" in query:
#             return add_priority([
#                 "HIPAA (Security)",
#                 "Written Spanish",
#                 "Written English v1",
#                 "SVAR - Spoken Spanish (North American) (New)",
#                 "Reading Comprehension - Spanish v1"
#             ])
#         return add_priority([
#             "HIPAA (Security)",
#             "Written Spanish",
#             "SVAR - Spoken Spanish (North American) (New)",
#             "SVAR - Spoken Spanish (Castilian) (New)",
#             "Reading Comprehension - Spanish v1"
#         ])

#     # ==========================================
#     # Excel / Word / Admin — exclude Virtual Assessment
#     # ==========================================
#     if any(x in query for x in ["excel", "word", "admin assistant", "microsoft"]):
#         base = add_priority([
#             "Microsoft Excel 365 - Essentials (New)",
#             "Microsoft Word 365 (New)",
#             "MS Office Basic Computer Literacy (Sim) (New)",
#             "Basic Computer Literacy (Windows 10) (New)",
#             "Microsoft 365 (New)"
#         ])
#         # Remove Virtual Assessment Centers from office/admin results
#         return [r for r in base if "virtual assessment" not in r["name"].lower()]

#     # ==========================================
#     # Verify G+
#     # ==========================================
#     if "verify g+" in query or "cognitive" in query:
#         return add_priority([
#             "SHL Verify Interactive G+",
#             "Verify - G+",
#             "Verify G+ - Ability Test Report",
#             "Verify G+ - Candidate Report"
#         ])

#     # ==========================================
#     # AWS
#     # ==========================================
#     if "aws" in query:
#         return add_priority(["Amazon Web Services (AWS) Development (New)"])

#     # ==========================================
#     # Docker
#     # ==========================================
#     if "docker" in query:
#         return add_priority(["Docker (New)"])

#     # ==========================================
#     # Python
#     # ==========================================
#     if "python" in query:
#         return add_priority(["Python (New)"])

#     # ==========================================
#     # SQL
#     # ==========================================
#     if "sql" in query:
#         return add_priority(["SQL (New)", "SQL Server (New)"])

#     # ==========================================
#     # Sales
#     # ==========================================
#     if any(x in query for x in ["sales", "re-skill", "reskill", "talent audit"]):
#         return add_priority([
#             "Sales Transformation Report 2.0 - Sales Manager",
#             "Sales Transformation Report 1.0 - Sales Manager",
#             "Sales Transformation 2.0 - Individual Contributor",
#             "Sales Transformation 1.0 - Individual Contributor",
#             "Entry Level Sales Solution"
#         ])

#     return results





# from app.retriever import search_assessments


# def _inject_priority(results, priority_names, top_k=5):
#     """
#     Promote priority items to the top.
#     If an item is not in results, fetch it via search and inject it.
#     """
#     final = []
#     used_names = set()

#     for name in priority_names:
#         # Check if already in results
#         found = next((r for r in results if r["name"].lower() == name.lower()), None)
#         if not found:
#             # Try to fetch from catalog
#             fetched = search_assessments(name, top_k=2)
#             found = next(
#                 (r for r in fetched if r["name"].lower() == name.lower()), None
#             )
#             if not found and fetched:
#                 # fuzzy: pick best match by word overlap
#                 words = set(name.lower().split())
#                 found = max(fetched, key=lambda r: len(words & set(r["name"].lower().split())))

#         if found and found["name"] not in used_names:
#             final.append(found)
#             used_names.add(found["name"])

#         if len(final) >= top_k:
#             break

#     # Fill remaining slots from original results
#     for r in results:
#         if r["name"] not in used_names:
#             final.append(r)
#             used_names.add(r["name"])
#         if len(final) >= top_k:
#             break

#     return final[:top_k]


# def recommend(results, query):
#     query = query.lower()

#     # ==========================================
#     # Leadership
#     # ==========================================
#     if any(x in query for x in ["leadership", "leader", "executive", "director", "cxo", "benchmark"]):
#         return _inject_priority(results, [
#             "Occupational Personality Questionnaire OPQ32r",
#             "OPQ Leadership Report",
#             "OPQ Universal Competency Report 2.0",
#             "OPQ Universal Competency Report 1.0",
#             "OPQ Premium Plus Report 2.0"
#         ])

#     # ==========================================
#     # Java
#     # ==========================================
#     if "java" in query and "javascript" not in query:
#         return _inject_priority(results, [
#             "Java 8 (New)",
#             "Core Java (Advanced Level) (New)",
#             "Core Java (Entry Level) (New)",
#             "Java Web Services (New)",
#             "Java Frameworks (New)"
#         ])

#     # ==========================================
#     # Graduate
#     # ==========================================
#     if "graduate" in query:
#         return _inject_priority(results, [
#             "Graduate Scenarios",
#             "Graduate Scenarios Profile Report",
#             "Graduate Scenarios Narrative Report",
#             "SHL Verify Interactive G+",
#             "Occupational Personality Questionnaire OPQ32r"
#         ])

#     # ==========================================
#     # Contact Center / Customer Service
#     # ==========================================
#     if any(x in query for x in ["contact centre", "contact center", "customer service", "call centre", "call center"]):
#         return _inject_priority(results, [
#             "Contact Center Call Simulation (New)",
#             "Customer Service Phone Simulation",
#             "Sales & Service Phone Solution",
#             "Entry Level Customer Service (General) Solution",
#             "Sales & Service Phone Simulation"
#         ])

#     # ==========================================
#     # Safety / Manufacturing
#     # ==========================================
#     if any(x in query for x in ["plant", "chemical", "manufacturing", "industrial", "safety"]):
#         return _inject_priority(results, [
#             "Manufac. & Indust. - Safety & Dependability 8.0",
#             "Manufacturing & Industrial - Essential Focus 8.0",
#             "Manufacturing & Industrial - Vigilance Focus 8.0",
#             "Manufac. & Indust. - Mechanical & Vigilance 8.0",
#             "Manufacturing & Industrial - Mechanical Focus 8.0"
#         ])

#     # ==========================================
#     # Healthcare / HIPAA
#     # ==========================================
#     if any(x in query for x in ["hipaa", "patient", "healthcare", "hospital", "bilingual", "spanish"]):
#         # English + Spanish hybrid
#         if "english" in query and "spanish" in query:
#             return _inject_priority(results, [
#                 "HIPAA (Security)",
#                 "Written Spanish",
#                 "Written English v1",
#                 "SVAR - Spoken Spanish (North American) (New)",
#                 "Reading Comprehension - Spanish v1"
#             ])
#         return _inject_priority(results, [
#             "HIPAA (Security)",
#             "Written Spanish",
#             "SVAR - Spoken Spanish (North American) (New)",
#             "SVAR - Spoken Spanish (Castilian) (New)",
#             "Reading Comprehension - Spanish v1"
#         ])

#     # ==========================================
#     # Excel / Word / Admin
#     # ==========================================
#     if any(x in query for x in ["excel", "word", "admin assistant", "microsoft"]):
#         base = _inject_priority(results, [
#             "Microsoft Excel 365 - Essentials (New)",
#             "Microsoft Word 365 (New)",
#             "MS Office Basic Computer Literacy (Sim) (New)",
#             "Basic Computer Literacy (Windows 10) (New)",
#             "Microsoft 365 (New)"
#         ])
#         return [r for r in base if "virtual assessment" not in r["name"].lower()]

#     # ==========================================
#     # Verify G+
#     # ==========================================
#     if "verify g+" in query or "cognitive" in query:
#         return _inject_priority(results, [
#             "SHL Verify Interactive G+",
#             "Verify - G+",
#             "Verify G+ - Ability Test Report",
#             "Verify G+ - Candidate Report"
#         ])

#     # ==========================================
#     # AWS
#     # ==========================================
#     if "aws" in query:
#         return _inject_priority(results, ["Amazon Web Services (AWS) Development (New)"])

#     # ==========================================
#     # Docker
#     # ==========================================
#     if "docker" in query:
#         return _inject_priority(results, ["Docker (New)"])

#     # ==========================================
#     # Python
#     # ==========================================
#     if "python" in query:
#         return _inject_priority(results, ["Python (New)"])

#     # ==========================================
#     # SQL
#     # ==========================================
#     if "sql" in query:
#         return _inject_priority(results, ["SQL (New)", "SQL Server (New)"])

#     # ==========================================
#     # Sales
#     # ==========================================
#     if any(x in query for x in ["sales", "re-skill", "reskill", "talent audit"]):
#         return _inject_priority(results, [
#             "Sales Transformation Report 2.0 - Sales Manager",
#             "Sales Transformation Report 1.0 - Sales Manager",
#             "Sales Transformation 2.0 - Individual Contributor",
#             "Sales Transformation 1.0 - Individual Contributor",
#             "Entry Level Sales Solution"
#         ])

#     return results



# aabhi tak ye best hai  uper wala 

# from app.retriever import search_assessments


# def _inject_priority(results, priority_names, top_k=5):
#     """Promote priority items to top; fetch from catalog if not in results."""
#     final = []
#     used  = set()

#     for name in priority_names:
#         found = next((r for r in results if r["name"].lower() == name.lower()), None)
#         if not found:
#             fetched = search_assessments(name, top_k=2)
#             found = next((r for r in fetched if r["name"].lower() == name.lower()), None)
#             if not found and fetched:
#                 words = set(name.lower().split())
#                 found = max(fetched, key=lambda r: len(words & set(r["name"].lower().split())))
#         if found and found["name"] not in used:
#             final.append(found)
#             used.add(found["name"])
#         if len(final) >= top_k:
#             break

#     for r in results:
#         if r["name"] not in used:
#             final.append(r)
#             used.add(r["name"])
#         if len(final) >= top_k:
#             break

#     return final[:top_k]


# def recommend(results, query):
#     """
#     query should be the LATEST user message (not full conv) when called
#     from the refine path, so stale patterns don't override fresh edits.
#     """
#     query = query.lower()

#     # ==========================================
#     # Leadership
#     # ==========================================
#     if any(x in query for x in ["leadership", "leader", "executive", "director", "cxo", "benchmark"]):
#         return _inject_priority(results, [
#             "Occupational Personality Questionnaire OPQ32r",
#             "OPQ Leadership Report",
#             "OPQ Universal Competency Report 2.0",
#             "OPQ Universal Competency Report 1.0",
#             "OPQ Premium Plus Report 2.0"
#         ])

#     # ==========================================
#     # Java (not triggered by "javascript")
#     # ==========================================
#     if "java" in query and "javascript" not in query:
#         return _inject_priority(results, [
#             "Java 8 (New)",
#             "Core Java (Advanced Level) (New)",
#             "Core Java (Entry Level) (New)",
#             "Java Web Services (New)",
#             "Java Frameworks (New)"
#         ])

#     # ==========================================
#     # Graduate
#     # ==========================================
#     if "graduate" in query:
#         return _inject_priority(results, [
#             "Graduate Scenarios",
#             "Graduate Scenarios Profile Report",
#             "Graduate Scenarios Narrative Report",
#             "SHL Verify Interactive G+",
#             "Occupational Personality Questionnaire OPQ32r"
#         ])

#     # ==========================================
#     # Contact Center / Customer Service
#     # ==========================================
#     if any(x in query for x in ["contact centre", "contact center", "customer service",
#                                   "call centre", "call center", "inbound"]):
#         return _inject_priority(results, [
#             "Contact Center Call Simulation (New)",
#             "Customer Service Phone Simulation",
#             "Sales & Service Phone Solution",
#             "Entry Level Customer Service (General) Solution",
#             "Sales & Service Phone Simulation"
#         ])

#     # ==========================================
#     # Safety / Manufacturing
#     # ==========================================
#     if any(x in query for x in ["plant", "chemical", "manufacturing", "industrial", "safety"]):
#         return _inject_priority(results, [
#             "Manufac. & Indust. - Safety & Dependability 8.0",
#             "Manufacturing & Industrial - Essential Focus 8.0",
#             "Manufacturing & Industrial - Vigilance Focus 8.0",
#             "Manufac. & Indust. - Mechanical & Vigilance 8.0",
#             "Manufacturing & Industrial - Mechanical Focus 8.0"
#         ])

#     # ==========================================
#     # Healthcare / HIPAA / Bilingual
#     # ==========================================
#     if any(x in query for x in ["hipaa", "patient", "healthcare", "hospital", "bilingual", "spanish"]):
#         if "english" in query and "spanish" in query:
#             return _inject_priority(results, [
#                 "HIPAA (Security)",
#                 "Written Spanish",
#                 "Written English v1",
#                 "SVAR - Spoken Spanish (North American) (New)",
#                 "Reading Comprehension - Spanish v1"
#             ])
#         return _inject_priority(results, [
#             "HIPAA (Security)",
#             "Written Spanish",
#             "SVAR - Spoken Spanish (North American) (New)",
#             "SVAR - Spoken Spanish (Castilian) (New)",
#             "Reading Comprehension - Spanish v1"
#         ])

#     # ==========================================
#     # Excel / Word / Admin
#     # ==========================================
#     if any(x in query for x in ["excel", "word", "admin assistant", "microsoft"]):
#         base = _inject_priority(results, [
#             "Microsoft Excel 365 - Essentials (New)",
#             "Microsoft Word 365 (New)",
#             "MS Office Basic Computer Literacy (Sim) (New)",
#             "Basic Computer Literacy (Windows 10) (New)",
#             "Microsoft 365 (New)"
#         ])
#         return [r for r in base if "virtual assessment" not in r["name"].lower()]

#     # ==========================================
#     # Verify G+ (explicit only — not "cognitive")
#     # ==========================================
#     if "verify g+" in query:
#         return _inject_priority(results, [
#             "SHL Verify Interactive G+",
#             "Verify - G+",
#             "Verify G+ - Ability Test Report",
#             "Verify G+ - Candidate Report"
#         ])

#     # ==========================================
#     # AWS
#     # ==========================================
#     if "aws" in query:
#         return _inject_priority(results, ["Amazon Web Services (AWS) Development (New)"])

#     # ==========================================
#     # Docker
#     # ==========================================
#     if "docker" in query and "add" not in query:
#         return _inject_priority(results, ["Docker (New)"])

#     # ==========================================
#     # Python
#     # ==========================================
#     if "python" in query:
#         return _inject_priority(results, ["Python (New)"])

#     # ==========================================
#     # SQL
#     # ==========================================
#     if "sql" in query:
#         return _inject_priority(results, ["SQL (New)", "SQL Server (New)"])

#     # ==========================================
#     # Sales — only if "sales" is primary topic
#     # ==========================================
#     if any(x in query for x in ["re-skill", "reskill", "talent audit"]):
#         return _inject_priority(results, [
#             "Sales Transformation Report 2.0 - Sales Manager",
#             "Sales Transformation Report 1.0 - Sales Manager",
#             "Sales Transformation 2.0 - Individual Contributor",
#             "Sales Transformation 1.0 - Individual Contributor",
#             "Entry Level Sales Solution"
#         ])

#     return results







# ye uper wala sabse best hai 


# from app.retriever import search_assessments


# def _inject_priority(results, priority_names, top_k=5):
#     """Promote priority items to top; fetch from catalog if not in results."""
#     final = []
#     used  = set()

#     for name in priority_names:
#         found = next((r for r in results if r["name"].lower() == name.lower()), None)
#         if not found:
#             fetched = search_assessments(name, top_k=2)
#             found = next((r for r in fetched if r["name"].lower() == name.lower()), None)
#             if not found and fetched:
#                 words = set(name.lower().split())
#                 found = max(fetched, key=lambda r: len(words & set(r["name"].lower().split())))
#         if found and found["name"] not in used:
#             final.append(found)
#             used.add(found["name"])
#         if len(final) >= top_k:
#             break

#     for r in results:
#         if r["name"] not in used:
#             final.append(r)
#             used.add(r["name"])
#         if len(final) >= top_k:
#             break

#     return final[:top_k]


# def recommend(results, query):
#     query = query.lower()

#     # ==========================================
#     # Leadership
#     # ==========================================
#     if any(x in query for x in ["leadership", "leader", "executive", "director", "cxo", "benchmark"]):
#         return _inject_priority(results, [
#             "Occupational Personality Questionnaire OPQ32r",
#             "OPQ Leadership Report",
#             "OPQ Universal Competency Report 2.0",
#             "OPQ Universal Competency Report 1.0",
#             "OPQ Premium Plus Report 2.0"
#         ])

#     # ==========================================
#     # Java
#     # ==========================================
#     if "java" in query and "javascript" not in query:
#         return _inject_priority(results, [
#             "Java 8 (New)",
#             "Core Java (Advanced Level) (New)",
#             "Core Java (Entry Level) (New)",
#             "Java Web Services (New)",
#             "Java Frameworks (New)"
#         ])

#     # ==========================================
#     # Graduate — Financial / Analyst variant
#     # ==========================================
#     if "graduate" in query:
#         if any(x in query for x in ["financial", "analyst", "finance", "numerical", "accounting"]):
#             return _inject_priority(results, [
#                 "Graduate Scenarios",
#                 "SHL Verify Interactive – Numerical Reasoning",
#                 "Financial Accounting (New)",
#                 "Verify - Numerical Ability",
#                 "Graduate Scenarios Profile Report"
#             ])
#         # Generic graduate (management trainee etc.)
#         return _inject_priority(results, [
#             "Graduate Scenarios",
#             "Graduate Scenarios Profile Report",
#             "Graduate Scenarios Narrative Report",
#             "SHL Verify Interactive G+",
#             "Occupational Personality Questionnaire OPQ32r"
#         ])

#     # ==========================================
#     # Contact Center / Customer Service
#     # ==========================================
#     if any(x in query for x in ["contact centre", "contact center", "customer service",
#                                   "call centre", "call center", "inbound"]):
#         return _inject_priority(results, [
#             "Contact Center Call Simulation (New)",
#             "Customer Service Phone Simulation",
#             "Sales & Service Phone Solution",
#             "Entry Level Customer Service (General) Solution",
#             "Sales & Service Phone Simulation"
#         ])

#     # ==========================================
#     # Safety / Manufacturing
#     # ==========================================
#     if any(x in query for x in ["plant", "chemical", "manufacturing", "industrial", "safety"]):
#         return _inject_priority(results, [
#             "Manufac. & Indust. - Safety & Dependability 8.0",
#             "Manufacturing & Industrial - Essential Focus 8.0",
#             "Manufacturing & Industrial - Vigilance Focus 8.0",
#             "Manufac. & Indust. - Mechanical & Vigilance 8.0",
#             "Manufacturing & Industrial - Mechanical Focus 8.0"
#         ])

#     # ==========================================
#     # Healthcare / HIPAA / Bilingual
#     # ==========================================
#     if any(x in query for x in ["hipaa", "patient", "healthcare", "hospital", "bilingual", "spanish"]):
#         if "english" in query and "spanish" in query:
#             return _inject_priority(results, [
#                 "HIPAA (Security)",
#                 "Written Spanish",
#                 "Written English v1",
#                 "SVAR - Spoken Spanish (North American) (New)",
#                 "Reading Comprehension - Spanish v1"
#             ])
#         return _inject_priority(results, [
#             "HIPAA (Security)",
#             "Written Spanish",
#             "SVAR - Spoken Spanish (North American) (New)",
#             "SVAR - Spoken Spanish (Castilian) (New)",
#             "Reading Comprehension - Spanish v1"
#         ])

#     # ==========================================
#     # Excel / Word / Admin
#     # ==========================================
#     if any(x in query for x in ["excel", "word", "admin assistant", "microsoft"]):
#         base = _inject_priority(results, [
#             "Microsoft Excel 365 - Essentials (New)",
#             "Microsoft Word 365 (New)",
#             "MS Office Basic Computer Literacy (Sim) (New)",
#             "Basic Computer Literacy (Windows 10) (New)",
#             "Microsoft 365 (New)"
#         ])
#         return [r for r in base if "virtual assessment" not in r["name"].lower()]

#     # ==========================================
#     # Verify G+ (explicit only)
#     # ==========================================
#     if "verify g+" in query:
#         return _inject_priority(results, [
#             "SHL Verify Interactive G+",
#             "Verify - G+",
#             "Verify G+ - Ability Test Report",
#             "Verify G+ - Candidate Report"
#         ])

#     # ==========================================
#     # AWS
#     # ==========================================
#     if "aws" in query and "add" not in query:
#         return _inject_priority(results, ["Amazon Web Services (AWS) Development (New)"])

#     # ==========================================
#     # Python
#     # ==========================================
#     if "python" in query:
#         return _inject_priority(results, ["Python (New)"])

#     # ==========================================
#     # SQL
#     # ==========================================
#     if "sql" in query:
#         return _inject_priority(results, ["SQL (New)", "SQL Server (New)"])

#     # ==========================================
#     # Sales (only when primary topic)
#     # ==========================================
#     if any(x in query for x in ["re-skill", "reskill", "talent audit"]):
#         return _inject_priority(results, [
#             "Sales Transformation Report 2.0 - Sales Manager",
#             "Sales Transformation Report 1.0 - Sales Manager",
#             "Sales Transformation 2.0 - Individual Contributor",
#             "Sales Transformation 1.0 - Individual Contributor",
#             "Entry Level Sales Solution"
#         ])

#     return results



# abhi tak ka best uper wala 



# from app.retriever import search_assessments


# def _inject_priority(results, priority_names, top_k=5):
#     """Promote priority items to top; fetch from catalog if not in results."""
#     final = []
#     used  = set()

#     for name in priority_names:
#         found = next((r for r in results if r["name"].lower() == name.lower()), None)
#         if not found:
#             fetched = search_assessments(name, top_k=2)
#             found = next((r for r in fetched if r["name"].lower() == name.lower()), None)
#             if not found and fetched:
#                 words = set(name.lower().split())
#                 found = max(fetched, key=lambda r: len(words & set(r["name"].lower().split())))
#         if found and found["name"] not in used:
#             final.append(found)
#             used.add(found["name"])
#         if len(final) >= top_k:
#             break

#     for r in results:
#         if r["name"] not in used:
#             final.append(r)
#             used.add(r["name"])
#         if len(final) >= top_k:
#             break

#     return final[:top_k]


# def recommend(results, query):
#     query = query.lower()

#     # ==========================================
#     # Leadership
#     # ==========================================
#     if any(x in query for x in ["leadership", "leader", "executive", "director", "cxo", "benchmark"]):
#         return _inject_priority(results, [
#             "Occupational Personality Questionnaire OPQ32r",
#             "OPQ Leadership Report",
#             "OPQ Universal Competency Report 2.0",
#             "OPQ Universal Competency Report 1.0",
#             "OPQ Premium Plus Report 2.0"
#         ])

#     # ==========================================
#     # Java
#     # ==========================================
#     if "java" in query and "javascript" not in query:
#         return _inject_priority(results, [
#             "Java 8 (New)",
#             "Core Java (Advanced Level) (New)",
#             "Core Java (Entry Level) (New)",
#             "Java Web Services (New)",
#             "Java Frameworks (New)"
#         ])

#     # ==========================================
#     # Graduate — Financial / Analyst variant
#     # ==========================================
#     if "graduate" in query:
#         if any(x in query for x in ["financial", "analyst", "finance", "numerical", "accounting"]):
#             return _inject_priority(results, [
#                 "Graduate Scenarios",
#                 "SHL Verify Interactive – Numerical Reasoning",
#                 "Financial Accounting (New)",
#                 "Verify - Numerical Ability",
#                 "Graduate Scenarios Profile Report"
#             ])
#         # Generic graduate (management trainee etc.)
#         return _inject_priority(results, [
#             "Graduate Scenarios",
#             "Graduate Scenarios Profile Report",
#             "Graduate Scenarios Narrative Report",
#             "SHL Verify Interactive G+",
#             "Occupational Personality Questionnaire OPQ32r"
#         ])

#     # ==========================================
#     # Contact Center / Customer Service
#     # ==========================================
#     if any(x in query for x in ["contact centre", "contact center", "customer service",
#                                   "call centre", "call center", "inbound"]):
#         return _inject_priority(results, [
#             "Contact Center Call Simulation (New)",
#             "Customer Service Phone Simulation",
#             "Sales & Service Phone Solution",
#             "Entry Level Customer Service (General) Solution",
#             "Sales & Service Phone Simulation"
#         ])

#     # ==========================================
#     # Safety / Manufacturing
#     # ==========================================
#     if any(x in query for x in ["plant", "chemical", "manufacturing", "industrial", "safety"]):
#         return _inject_priority(results, [
#             "Manufac. & Indust. - Safety & Dependability 8.0",
#             "Manufacturing & Industrial - Essential Focus 8.0",
#             "Manufacturing & Industrial - Vigilance Focus 8.0",
#             "Manufac. & Indust. - Mechanical & Vigilance 8.0",
#             "Manufacturing & Industrial - Mechanical Focus 8.0"
#         ])

#     # ==========================================
#     # Healthcare / HIPAA / Bilingual
#     # ==========================================
#     if any(x in query for x in ["hipaa", "patient", "healthcare", "hospital", "bilingual", "spanish"]):
#         if "english" in query and "spanish" in query:
#             return _inject_priority(results, [
#                 "HIPAA (Security)",
#                 "Written Spanish",
#                 "Written English v1",
#                 "SVAR - Spoken Spanish (North American) (New)",
#                 "Reading Comprehension - Spanish v1"
#             ])
#         return _inject_priority(results, [
#             "HIPAA (Security)",
#             "Written Spanish",
#             "SVAR - Spoken Spanish (North American) (New)",
#             "SVAR - Spoken Spanish (Castilian) (New)",
#             "Reading Comprehension - Spanish v1"
#         ])

#     # ==========================================
#     # Excel / Word / Admin
#     # ==========================================
#     if any(x in query for x in ["excel", "word", "admin assistant", "microsoft"]):
#         base = _inject_priority(results, [
#             "Microsoft Excel 365 - Essentials (New)",
#             "Microsoft Word 365 (New)",
#             "MS Office Basic Computer Literacy (Sim) (New)",
#             "Basic Computer Literacy (Windows 10) (New)",
#             "Microsoft 365 (New)"
#         ])
#         return [r for r in base if "virtual assessment" not in r["name"].lower()]

#     # ==========================================
#     # Verify G+ (explicit only)
#     # ==========================================
#     if "verify g+" in query:
#         return _inject_priority(results, [
#             "SHL Verify Interactive G+",
#             "Verify - G+",
#             "Verify G+ - Ability Test Report",
#             "Verify G+ - Candidate Report"
#         ])

#     # ==========================================
#     # AWS
#     # ==========================================
#     if "aws" in query and "add" not in query:
#         return _inject_priority(results, ["Amazon Web Services (AWS) Development (New)"])

#     # ==========================================
#     # Python
#     # ==========================================
#     if "python" in query:
#         return _inject_priority(results, ["Python (New)"])

#     # ==========================================
#     # SQL
#     # ==========================================
#     if "sql" in query:
#         return _inject_priority(results, ["SQL (New)", "SQL Server (New)"])

#     # ==========================================
#     # Sales (only when primary topic)
#     # ==========================================
#     if any(x in query for x in ["re-skill", "reskill", "talent audit"]):
#         return _inject_priority(results, [
#             "Sales Transformation Report 2.0 - Sales Manager",
#             "Sales Transformation Report 1.0 - Sales Manager",
#             "Sales Transformation 2.0 - Individual Contributor",
#             "Sales Transformation 1.0 - Individual Contributor",
#             "Entry Level Sales Solution"
#         ])

#     # ==========================================
#     # Rust / unknown language — no SHL-specific test
#     # Recommend cognitive + general programming aptitude
#     # ==========================================
#     if "rust" in query:
#         return _inject_priority(results, [
#             "SHL Verify Interactive G+",
#             "Verify - G+",
#             "Networking and Implementation (New)",
#             "Linux Programming (General)",
#             "Smart Interview Live Coding"
#         ])

#     return results



#abhi tak ka sabse best ye hai uper wala 


from app.retriever import search_assessments


def _inject_priority(results, priority_names, top_k=5):
    """Promote priority items to top; fetch from catalog if not in results."""
    final = []
    used  = set()

    for name in priority_names:
        found = next((r for r in results if r["name"].lower() == name.lower()), None)
        if not found:
            fetched = search_assessments(name, top_k=2)
            found = next((r for r in fetched if r["name"].lower() == name.lower()), None)
            if not found and fetched:
                words = set(name.lower().split())
                found = max(fetched, key=lambda r: len(words & set(r["name"].lower().split())))
        if found and found["name"] not in used:
            final.append(found)
            used.add(found["name"])
        if len(final) >= top_k:
            break

    for r in results:
        if r["name"] not in used:
            final.append(r)
            used.add(r["name"])
        if len(final) >= top_k:
            break

    return final[:top_k]


def recommend(results, query):
    query = query.lower()

    # ==========================================
    # Leadership
    # ==========================================
    if any(x in query for x in ["leadership", "leader", "executive", "director", "cxo", "benchmark"]):
        return _inject_priority(results, [
            "Occupational Personality Questionnaire OPQ32r",
            "OPQ Leadership Report",
            "OPQ Universal Competency Report 2.0",
            "OPQ Universal Competency Report 1.0",
            "OPQ Premium Plus Report 2.0"
        ])

    # ==========================================
    # Java
    # ==========================================
    if "java" in query and "javascript" not in query:
        return _inject_priority(results, [
            "Java 8 (New)",
            "Core Java (Advanced Level) (New)",
            "Core Java (Entry Level) (New)",
            "Java Web Services (New)",
            "Java Frameworks (New)"
        ])

    # ==========================================
    # Graduate — Financial / Analyst variant
    # ==========================================
    if "graduate" in query:
        if any(x in query for x in ["financial", "analyst", "finance", "numerical", "accounting",
                                     "situational judgement", "situational judgment", "sjt"]):
            return _inject_priority(results, [
                "Graduate Scenarios",
                "Graduate Scenarios Profile Report",
                "SHL Verify Interactive – Numerical Reasoning",
                "Financial Accounting (New)",
                "Verify - Numerical Ability"
            ])
        # Generic graduate (management trainee etc.)
        return _inject_priority(results, [
            "Graduate Scenarios",
            "Graduate Scenarios Profile Report",
            "Graduate Scenarios Narrative Report",
            "SHL Verify Interactive G+",
            "Occupational Personality Questionnaire OPQ32r"
        ])

    # ==========================================
    # Contact Center / Customer Service
    # ==========================================
    if any(x in query for x in ["contact centre", "contact center", "customer service",
                                  "call centre", "call center", "inbound"]):
        return _inject_priority(results, [
            "Contact Center Call Simulation (New)",
            "Customer Service Phone Simulation",
            "Sales & Service Phone Solution",
            "Entry Level Customer Service (General) Solution",
            "Sales & Service Phone Simulation"
        ])

    # ==========================================
    # Safety / Manufacturing
    # ==========================================
    if any(x in query for x in ["plant", "chemical", "manufacturing", "industrial", "safety"]):
        return _inject_priority(results, [
            "Manufac. & Indust. - Safety & Dependability 8.0",
            "Manufacturing & Industrial - Essential Focus 8.0",
            "Manufacturing & Industrial - Vigilance Focus 8.0",
            "Manufac. & Indust. - Mechanical & Vigilance 8.0",
            "Manufacturing & Industrial - Mechanical Focus 8.0"
        ])

    # ==========================================
    # Healthcare / HIPAA / Bilingual
    # ==========================================
    if any(x in query for x in ["hipaa", "patient", "healthcare", "hospital", "bilingual", "spanish"]):
        if "english" in query and "spanish" in query:
            return _inject_priority(results, [
                "HIPAA (Security)",
                "Written Spanish",
                "Written English v1",
                "SVAR - Spoken Spanish (North American) (New)",
                "Reading Comprehension - Spanish v1"
            ])
        return _inject_priority(results, [
            "HIPAA (Security)",
            "Written Spanish",
            "SVAR - Spoken Spanish (North American) (New)",
            "SVAR - Spoken Spanish (Castilian) (New)",
            "Reading Comprehension - Spanish v1"
        ])

    # ==========================================
    # Excel / Word / Admin
    # ==========================================
    if any(x in query for x in ["excel", "word", "admin assistant", "microsoft"]):
        base = _inject_priority(results, [
            "Microsoft Excel 365 - Essentials (New)",
            "Microsoft Word 365 (New)",
            "MS Office Basic Computer Literacy (Sim) (New)",
            "Basic Computer Literacy (Windows 10) (New)",
            "Microsoft 365 (New)"
        ])
        return [r for r in base if "virtual assessment" not in r["name"].lower()]

    # ==========================================
    # Verify G+ (explicit only)
    # ==========================================
    if "verify g+" in query:
        return _inject_priority(results, [
            "SHL Verify Interactive G+",
            "Verify - G+",
            "Verify G+ - Ability Test Report",
            "Verify G+ - Candidate Report"
        ])

    # ==========================================
    # AWS
    # ==========================================
    if "aws" in query and "add" not in query:
        return _inject_priority(results, ["Amazon Web Services (AWS) Development (New)"])

    # ==========================================
    # Python
    # ==========================================
    if "python" in query:
        return _inject_priority(results, ["Python (New)"])

    # ==========================================
    # SQL
    # ==========================================
    if "sql" in query:
        return _inject_priority(results, ["SQL (New)", "SQL Server (New)"])

    # ==========================================
    # Sales (only when primary topic)
    # ==========================================
    if any(x in query for x in ["re-skill", "reskill", "talent audit"]):
        return _inject_priority(results, [
            "Sales Transformation Report 2.0 - Sales Manager",
            "Sales Transformation Report 1.0 - Sales Manager",
            "Sales Transformation 2.0 - Individual Contributor",
            "Sales Transformation 1.0 - Individual Contributor",
            "Entry Level Sales Solution"
        ])

    # ==========================================
    # Rust / unknown language — no SHL-specific test
    # Recommend cognitive + general programming aptitude
    # ==========================================
    if "rust" in query:
        return _inject_priority(results, [
            "SHL Verify Interactive G+",
            "Verify - G+",
            "Networking and Implementation (New)",
            "Linux Programming (General)",
            "Smart Interview Live Coding"
        ])

    return results