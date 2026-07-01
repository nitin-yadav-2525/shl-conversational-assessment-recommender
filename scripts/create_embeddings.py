# import os
# import json
# import numpy as np
# import faiss

# from tqdm import tqdm
# from sentence_transformers import SentenceTransformer

# # ============================================================
# # Paths
# # ============================================================

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# DATA_PATH = os.path.join(BASE_DIR, "data", "full_catalog.json")

# VECTOR_DIR = os.path.join(BASE_DIR, "vector_db")
# os.makedirs(VECTOR_DIR, exist_ok=True)

# INDEX_PATH = os.path.join(VECTOR_DIR, "faiss.index")
# EMBEDDING_PATH = os.path.join(VECTOR_DIR, "embeddings.npy")
# METADATA_PATH = os.path.join(VECTOR_DIR, "metadata.json")

# # ============================================================
# # Load Embedding Model
# # ============================================================

# print("=" * 60)
# print("Loading Sentence Transformer Model...")
# print("=" * 60)

# model = SentenceTransformer("all-MiniLM-L6-v2")

# # ============================================================
# # Load SHL Catalog
# # ============================================================

# print("\nLoading SHL Catalog...\n")

# with open(DATA_PATH, "r", encoding="utf-8") as f:
#     catalog = json.load(f)

# print(f"Total Assessments Found : {len(catalog)}")

# # ============================================================
# # Build Search Documents
# # ============================================================

# documents = []
# metadata = []

# print("\nPreparing documents...\n")

# for item in tqdm(catalog):

#     text = " ".join([
#         item.get("name", ""),
#         item.get("description", ""),
#         " ".join(item.get("job_levels", [])),
#         " ".join(item.get("languages", [])),
#         " ".join(item.get("keys", [])),
#         item.get("duration", "")
#     ]).lower()

#     documents.append(text)

#     metadata.append({
#         "entity_id": item.get("entity_id", ""),
#         "name": item.get("name", ""),
#         "description": item.get("description", ""),
#         "duration": item.get("duration", ""),
#         "job_levels": item.get("job_levels", []),
#         "languages": item.get("languages", []),
#         "test_type": item.get("keys", []),
#         "url": item.get("link", "")
#     })

# # ============================================================
# # Create Embeddings
# # ============================================================

# print("\nGenerating Embeddings...\n")

# embeddings = model.encode(
#     documents,
#     convert_to_numpy=True,
#     show_progress_bar=True,
#     normalize_embeddings=True
# )

# print("\nEmbedding Shape :", embeddings.shape)

# # ============================================================
# # Create FAISS Index (Cosine Similarity)
# # ============================================================

# dimension = embeddings.shape[1]

# index = faiss.IndexFlatIP(dimension)

# index.add(embeddings)

# print("\nTotal Indexed Assessments :", index.ntotal)

# # ============================================================
# # Save Files
# # ============================================================

# faiss.write_index(index, INDEX_PATH)

# np.save(EMBEDDING_PATH, embeddings)

# with open(METADATA_PATH, "w", encoding="utf-8") as f:
#     json.dump(metadata, f, indent=4)

# print("\n" + "=" * 60)
# print("SUCCESS")
# print("=" * 60)

# print(f"FAISS Index Saved      : {INDEX_PATH}")
# print(f"Embeddings Saved      : {EMBEDDING_PATH}")
# print(f"Metadata Saved        : {METADATA_PATH}")



import os
import json
import numpy as np
import faiss

from tqdm import tqdm
from sentence_transformers import SentenceTransformer

# ============================================================
# Paths
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "full_catalog.json")

VECTOR_DIR = os.path.join(BASE_DIR, "vector_db")
os.makedirs(VECTOR_DIR, exist_ok=True)

INDEX_PATH = os.path.join(VECTOR_DIR, "faiss.index")
EMBEDDING_PATH = os.path.join(VECTOR_DIR, "embeddings.npy")
METADATA_PATH = os.path.join(VECTOR_DIR, "metadata.json")

# ============================================================
# Load Embedding Model
# ============================================================

print("=" * 70)
print("Loading Sentence Transformer...")
print("=" * 70)

model = SentenceTransformer("all-MiniLM-L6-v2")

# ============================================================
# Load SHL Catalog
# ============================================================

print("\nLoading SHL Catalog...\n")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

print(f"Total Assessments : {len(catalog)}")

# ============================================================
# Build Documents
# ============================================================

documents = []
metadata = []

print("\nPreparing Search Documents...\n")

for item in tqdm(catalog):

    name = item.get("name", "")
    description = item.get("description", "")
    job_levels = " ".join(item.get("job_levels", []))
    languages = " ".join(item.get("languages", []))
    keys = " ".join(item.get("keys", []))
    duration = item.get("duration", "")

    name_lower = name.lower()
    desc_lower = description.lower()

    extra_keywords = []

    # ============================================================
    # Personality / Leadership
    # ============================================================

    if (
        "opq" in name_lower
        or "personality" in desc_lower
        or "leadership" in name_lower
    ):

        extra_keywords += [
            "leadership",
            "senior leadership",
            "executive",
            "cxo",
            "director",
            "manager",
            "behavior",
            "behaviour",
            "personality",
            "leadership benchmark",
            "selection",
            "development",
            "developmental",
            "competency",
            "talent",
            "succession planning",
            "leadership assessment"
        ]

    # ============================================================
    # Ability Tests
    # ============================================================

    if (
        "ability" in keys.lower()
        or "verify" in name_lower
        or "reasoning" in desc_lower
    ):

        extra_keywords += [
            "aptitude",
            "logical reasoning",
            "numerical reasoning",
            "verbal reasoning",
            "analytical thinking",
            "problem solving",
            "cognitive ability"
        ]

    # ============================================================
    # Java
    # ============================================================

    if "java" in name_lower:

        extra_keywords += [
            "java developer",
            "backend developer",
            "software engineer",
            "spring",
            "hibernate",
            "oop",
            "multithreading",
            "collections",
            "jdbc"
        ]

    # ============================================================
    # Python
    # ============================================================

    if "python" in name_lower:

        extra_keywords += [
            "python developer",
            "django",
            "flask",
            "fastapi",
            "backend",
            "automation",
            "data science",
            "machine learning"
        ]

    # ============================================================
    # SQL
    # ============================================================

    if "sql" in name_lower:

        extra_keywords += [
            "database",
            "mysql",
            "postgresql",
            "oracle",
            "queries",
            "joins",
            "stored procedures"
        ]

    # ============================================================
    # Sales
    # ============================================================

    if "sales" in name_lower:

        extra_keywords += [
            "sales executive",
            "business development",
            "communication",
            "client handling",
            "negotiation"
        ]

    # ============================================================
    # Searchable Document
    # ============================================================

    searchable_document = f"""
Assessment Name:
{name}

Assessment Name:
{name}

Assessment Name:
{name}

Description:
{description}

Assessment Type:
{keys}

Job Levels:
{job_levels}

Languages:
{languages}

Duration:
{duration}

Relevant Keywords:
{' '.join(extra_keywords)}

Description Again:
{description}
"""

    documents.append(searchable_document.lower())

    metadata.append({

        "entity_id": item.get("entity_id", ""),

        "name": name,

        "description": description,

        "duration": duration,

        "job_levels": item.get("job_levels", []),

        "languages": item.get("languages", []),

        "test_type": item.get("keys", []),

        "url": item.get("link", "")

    })

# ============================================================
# Create Embeddings
# ============================================================

print("\nGenerating Embeddings...\n")

embeddings = model.encode(

    documents,

    convert_to_numpy=True,

    normalize_embeddings=True,

    show_progress_bar=True

)

print("\nEmbedding Shape :", embeddings.shape)

# ============================================================
# Create FAISS Index
# ============================================================

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(embeddings)

print("\nTotal Indexed :", index.ntotal)

# ============================================================
# Save Files
# ============================================================

faiss.write_index(index, INDEX_PATH)

np.save(EMBEDDING_PATH, embeddings)

with open(METADATA_PATH, "w", encoding="utf-8") as f:

    json.dump(metadata, f, indent=4)

print("\n" + "=" * 70)
print("SUCCESS")
print("=" * 70)

print(f"FAISS Index : {INDEX_PATH}")
print(f"Embeddings : {EMBEDDING_PATH}")
print(f"Metadata : {METADATA_PATH}")