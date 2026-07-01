# SHL Conversational Assessment Recommender

A conversational AI system built for the **SHL AI Intern Take-Home Assignment**. The application helps recruiters discover suitable **SHL Individual Test Solutions** through natural language conversations instead of manual catalog search.

---

## Features

- Conversational assessment recommendations
- Clarification of vague hiring requirements
- Context-aware recommendation refinement
- Assessment comparison
- Stateless conversation handling
- Semantic retrieval using FAISS
- LLM-generated conversational responses
- Refusal for legal and out-of-scope queries
- FastAPI REST API

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.13 |
| Backend | FastAPI |
| LLM | Gemini 2.0 Flash |
| Embeddings | all-MiniLM-L6-v2 |
| Vector Database | FAISS |
| Dataset | SHL Individual Test Solutions Catalog |

---

## Project Structure

```text
shl_assignment/
│
├── app/
│   ├── chatbot.py
│   ├── llm.py
│   ├── retriever.py
│   ├── recommendation_engine.py
│   ├── compare.py
│   ├── refine.py
│   ├── edit_recommendations.py
│   ├── conversation_state.py
│   ├── dialogue_manager.py
│   ├── response_builder.py
│   ├── rules.py
│   └── schemas.py
│
├── data/
│   └── full_catalog.json
│
├── vector_db/
│   ├── faiss.index
│   ├── metadata.json
│   └── embeddings.npy
│
├── tests/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## System Workflow
                        User
                          │
                          ▼
                FastAPI (/chat)
                          │
                          ▼
                  process_chat()
                          │
                          ▼
          Conversation State Detection
                          │
                          ▼
               Intent Detection (rules.py)
                          │
      ┌──────────┬─────────────┬──────────────┬──────────────┐
      │          │             │              │
      ▼          ▼             ▼              ▼
  Clarify     Compare       Refine      Recommendation
      │          │             │              │
      │          │             ▼              ▼
      │          │     Recommendation     Retriever
      │          │        Editing             │
      │          │             │              ▼
      │          │             │      FAISS Vector Search
      │          │             │              │
      │          │             ▼              ▼
      │          └────────► Top Assessments ◄──────────┐
      │                                                │
      └────────────────────────────────────────────────┘
                           │
                           ▼
                 Gemini 2.0 Flash (Reply)
                           │
                           ▼
              Response Builder (JSON)
                           │
                           ▼
                    FastAPI Response

---

## API Endpoints

### Health Check

```
GET /health
```

Response

```json
{
  "status": "ok"
}
```

---

### Chat

```
POST /chat
```

Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a Java Developer"
    }
  ]
}
```

Example Response

```json
{
  "reply": "Based on your requirements, here are the most relevant SHL assessments.",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "https://www.shl.com/...",
      "test_type": "Knowledge & Skills"
    }
  ],
  "end_of_conversation": false
}
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd shl_assignment
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the server

```bash
uvicorn main:app --reload
```

Server URL

```
http://127.0.0.1:8000
```

---

## Evaluation

The chatbot was tested using the provided SHL public conversation traces and supports:

- Clarification
- Recommendation
- Comparison
- Recommendation Refinement
- Safe Refusal
- Stateless Conversations

---

## Future Improvements

- Hybrid Retrieval (BM25 + FAISS)
- Better reranking
- Multi-language support
- Enhanced conversation reasoning

---

## Author

**Nitin Yadav**

M.Sc. Computer Science  
National Institute of Technology Tiruchirappalli

---

**Developed for the SHL AI Intern Take-Home Assignment.**