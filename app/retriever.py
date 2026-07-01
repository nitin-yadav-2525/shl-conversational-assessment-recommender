# import os
# import json
# import faiss
# import numpy as np

# from sentence_transformers import SentenceTransformer


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# VECTOR_DIR = os.path.join(BASE_DIR, "vector_db")

# INDEX_PATH = os.path.join(VECTOR_DIR, "faiss.index")
# METADATA_PATH = os.path.join(VECTOR_DIR, "metadata.json")


# print("Loading FAISS Index...")
# index = faiss.read_index(INDEX_PATH)

# print("Loading Metadata...")
# with open(METADATA_PATH, "r", encoding="utf-8") as f:
#     metadata = json.load(f)

# print("Loading Embedding Model...")
# model = SentenceTransformer("all-MiniLM-L6-v2")


# def search_assessments(query, top_k=5):
#     """
#     Search similar assessments
#     """

#     query_embedding = model.encode(
#         [query],
#         convert_to_numpy=True
#     )

#     distances, indices = index.search(query_embedding, top_k)

#     results = []

#     for idx, distance in zip(indices[0], distances[0]):

#         item = metadata[idx].copy()

#         item["score"] = float(distance)

#         results.append(item)

#     return results


# if __name__ == "__main__":

#     query = input("Enter recruiter requirement : ")

#     results = search_assessments(query)

#     print("\nTop Matching Assessments\n")

#     for i, item in enumerate(results, start=1):

#         print("=" * 60)

#         print(f"Rank : {i}")

#         print("Name :", item["name"])

#         print("Duration :", item["duration"])

#         print("Type :", item["test_type"])

#         print("URL :", item["url"])

#         print("Similarity Score :", item["score"])





# import os
# import json
# import faiss
# import numpy as np

# from sentence_transformers import SentenceTransformer

# # ============================================================
# # Paths
# # ============================================================

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# VECTOR_DIR = os.path.join(BASE_DIR, "vector_db")

# INDEX_PATH = os.path.join(VECTOR_DIR, "faiss.index")
# METADATA_PATH = os.path.join(VECTOR_DIR, "metadata.json")

# # ============================================================
# # Load FAISS Index
# # ============================================================

# print("Loading FAISS Index...")

# index = faiss.read_index(INDEX_PATH)

# # ============================================================
# # Load Metadata
# # ============================================================

# print("Loading Metadata...")

# with open(METADATA_PATH, "r", encoding="utf-8") as f:
#     metadata = json.load(f)

# # ============================================================
# # Load Embedding Model
# # ============================================================

# print("Loading Embedding Model...")

# model = SentenceTransformer("all-MiniLM-L6-v2")

# # ============================================================
# # Search Function
# # ============================================================
# def expand_query(query: str):

#     query_lower = query.lower()

#     expanded = query

#     # Leadership
#     if any(x in query_lower for x in [
#         "leadership",
#         "leader",
#         "executive",
#         "director",
#         "cxo",
#         "benchmark"
#     ]):

#         expanded += """
#         occupational personality questionnaire
#         opq32
#         opq32r
#         opq
#         personality assessment
#         leadership assessment
#         leadership report
#         universal competency report
#         selection
#         behavioural assessment
#         executive assessment
#         """

#     # Java
#     if "java" in query_lower:

#         expanded += """
#         java developer
#         core java
#         java 8
#         spring
#         hibernate
#         jdbc
#         collections
#         multithreading
#         """

#     # Python
#     if "python" in query_lower:

#         expanded += """
#         python developer
#         django
#         flask
#         fastapi
#         pandas
#         numpy
#         """

#     return expanded




# def search_assessments(query, top_k=30):

#     # --------------------------------------------------------
#     # Encode Query
#     # --------------------------------------------------------

#     expanded_query = expand_query(query)

#     query_embedding = model.encode(
#     [expanded_query], 
#         convert_to_numpy=True,
#         normalize_embeddings=True
#     )

#     # --------------------------------------------------------
#     # Search More Results First
#     # --------------------------------------------------------

#     scores, indices = index.search(query_embedding, 20)

#     results = []

#     for score, idx in zip(scores[0], indices[0]):

#         if idx == -1:
#             continue

#         item = metadata[idx].copy()

#         item["similarity"] = round(float(score) * 100, 2)

#         results.append(item)

#     # ========================================================
#     # RERANKING
#     # ========================================================

#     query_lower = query.lower()

#     def boost(item):

#         score = item["similarity"]

#         name = item["name"].lower()

#         description = item["description"].lower()

#         # ====================================================
#         # Leadership Queries
#         # ====================================================

#         if any(x in query_lower for x in [
#             "leadership",
#             "leader",
#             "executive",
#             "director",
#             "cxo",
#             "benchmark"
#         ]):

#             if "occupational personality questionnaire" in name:
#                 score += 50

#             elif "opq32" in name:
#                 score += 50

#             elif "opq leadership report" in name:
#                 score += 40

#             elif "universal competency report" in name:
#                 score += 35

#             elif "enterprise leadership" in name:
#                 score += 20

#         # ====================================================
#         # Java Queries
#         # ====================================================

#         if "java" in query_lower:

#             if "java 8" in name:
#                 score += 30

#             elif "core java" in name:
#                 score += 25

#             elif "java web" in name:
#                 score += 20

#             elif "framework" in name:
#                 score += 15

#         # ====================================================
#         # Python Queries
#         # ====================================================

#         if "python" in query_lower:

#             if "python" in name:
#                 score += 25

#         # ====================================================
#         # SQL Queries
#         # ====================================================

#         if "sql" in query_lower:

#             if "sql" in name:
#                 score += 20

#         # ====================================================
#         # Selection Queries
#         # ====================================================

#         if "selection" in query_lower:

#             if "selection report" in description:
#                 score += 10

#             if "selection" in name:
#                 score += 10

#         return score

#     results = sorted(
#         results,
#         key=boost,
#         reverse=True
#     )

#     return results[:top_k]


# # ============================================================
# # Testing
# # ============================================================

# if __name__ == "__main__":

#     while True:

#         print("\n" + "=" * 70)

#         query = input("Recruiter Requirement (type exit to quit): ")

#         if query.lower() == "exit":
#             break

#         results = search_assessments(query)

#         print("\nTop Matching Assessments\n")

#         for rank, item in enumerate(results, start=1):

#             print("=" * 70)

#             print(f"Rank              : {rank}")
#             print(f"Assessment        : {item['name']}")
#             print(f"Similarity        : {item['similarity']}%")
#             print(f"Duration          : {item['duration']}")
#             print(f"Job Levels        : {', '.join(item['job_levels'])}")
#             print(f"Languages         : {', '.join(item['languages'])}")
#             print(f"Assessment Type   : {', '.join(item['test_type'])}")
#             print(f"Description       : {item['description']}")
#             print(f"URL               : {item['url']}")

#         print()





import os
import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

# ============================================================
# Paths
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VECTOR_DIR = os.path.join(BASE_DIR, "vector_db")

INDEX_PATH = os.path.join(VECTOR_DIR, "faiss.index")
METADATA_PATH = os.path.join(VECTOR_DIR, "metadata.json")

# ============================================================
# Load FAISS Index
# ============================================================

print("Loading FAISS Index...")

index = faiss.read_index(INDEX_PATH)

# ============================================================
# Load Metadata
# ============================================================

print("Loading Metadata...")

with open(METADATA_PATH, "r", encoding="utf-8") as f:
    metadata = json.load(f)

# ============================================================
# Load Embedding Model
# ============================================================

print("Loading Embedding Model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

# ============================================================
# Query Expansion
# ============================================================

def expand_query(query: str):

    query_lower = query.lower()

    expanded = query

    # Leadership
    if any(x in query_lower for x in [
        "leadership", "leader", "executive", "director", "cxo", "benchmark"
    ]):
        expanded += """
        occupational personality questionnaire
        opq32
        opq32r
        opq
        personality assessment
        leadership assessment
        leadership report
        universal competency report
        selection
        behavioural assessment
        executive assessment
        """

    # Java
    if "java" in query_lower:
        expanded += """
        java developer
        core java
        java 8
        spring
        hibernate
        jdbc
        collections
        multithreading
        """

    # Python
    if "python" in query_lower:
        expanded += """
        python developer
        django
        flask
        fastapi
        pandas
        numpy
        """

    # Rust  ← NEW
    if "rust" in query_lower:
        expanded += """
        rust
        systems programming
        networking
        linux
        concurrency
        multithreading
        performance
        memory safety
        distributed systems
        """

    # Finance  ← NEW
    if any(x in query_lower for x in [
        "finance", "financial", "analyst", "accounting", "banking"
    ]):
        expanded += """
        finance
        financial accounting
        accounting
        numerical reasoning
        statistics
        business finance
        graduate
        """

    return expanded


# ============================================================
# Search Function
# ============================================================

def search_assessments(query, top_k=30):

    # --------------------------------------------------------
    # Encode Query
    # --------------------------------------------------------

    expanded_query = expand_query(query)

    query_embedding = model.encode(
        [expanded_query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # --------------------------------------------------------
    # Fetch 50 candidates first, reranker picks the best  ← CHANGED from 20
    # --------------------------------------------------------

    scores, indices = index.search(query_embedding, 50)

    results = []

    for score, idx in zip(scores[0], indices[0]):

        if idx == -1:
            continue

        item = metadata[idx].copy()

        item["similarity"] = round(float(score) * 100, 2)

        results.append(item)

    # ========================================================
    # RERANKING
    # ========================================================

    query_lower = query.lower()

    def boost(item):

        score = item["similarity"]

        name = item["name"].lower()

        description = item["description"].lower()

        # ====================================================
        # Leadership Queries
        # ====================================================

        if any(x in query_lower for x in [
            "leadership", "leader", "executive", "director", "cxo", "benchmark"
        ]):
            if "occupational personality questionnaire" in name:
                score += 50
            elif "opq32" in name:
                score += 50
            elif "opq leadership report" in name:
                score += 40
            elif "universal competency report" in name:
                score += 35
            elif "enterprise leadership" in name:
                score += 20

        # ====================================================
        # Java Queries
        # ====================================================

        if "java" in query_lower:
            if "java 8" in name:
                score += 30
            elif "core java" in name:
                score += 25
            elif "java web" in name:
                score += 20
            elif "framework" in name:
                score += 15

        # ====================================================
        # Python Queries
        # ====================================================

        if "python" in query_lower:
            if "python" in name:
                score += 25

        # ====================================================
        # SQL Queries
        # ====================================================

        if "sql" in query_lower:
            if "sql" in name:
                score += 20

        # ====================================================
        # Selection Queries
        # ====================================================

        if "selection" in query_lower:
            if "selection report" in description:
                score += 10
            if "selection" in name:
                score += 10

        # ====================================================
        # Rust Queries  ← NEW
        # ====================================================

        if "rust" in query_lower:
            if "network" in name or "network" in description:
                score += 30
            if "linux" in name or "linux" in description:
                score += 25
            if "programming" in description:
                score += 15
            if "java" in name:
                score -= 40
            if "spring" in name:
                score -= 30

        # ====================================================
        # Finance Queries  ← NEW
        # ====================================================

        if any(x in query_lower for x in [
            "finance", "financial", "analyst", "accounting"
        ]):
            if "financial accounting" in name:
                score += 35
            if "accounting" in name:
                score += 30
            if "numerical" in name:
                score += 25
            if "statistics" in name:
                score += 15
            if "graduate scenarios" in name:
                score += 20

        return score

    results = sorted(results, key=boost, reverse=True)

    return results[:top_k]


# ============================================================
# Testing
# ============================================================

if __name__ == "__main__":

    while True:

        print("\n" + "=" * 70)

        query = input("Recruiter Requirement (type exit to quit): ")

        if query.lower() == "exit":
            break

        results = search_assessments(query)

        print("\nTop Matching Assessments\n")

        for rank, item in enumerate(results, start=1):

            print("=" * 70)
            print(f"Rank              : {rank}")
            print(f"Assessment        : {item['name']}")
            print(f"Similarity        : {item['similarity']}%")
            print(f"Duration          : {item['duration']}")
            print(f"Job Levels        : {', '.join(item['job_levels'])}")
            print(f"Languages         : {', '.join(item['languages'])}")
            print(f"Assessment Type   : {', '.join(item['test_type'])}")
            print(f"Description       : {item['description']}")
            print(f"URL               : {item['url']}")

        print()