from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse
from app.chatbot import process_chat

app = FastAPI(
    title="SHL Conversational Assessment Recommender",
    version="2.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = process_chat(request.messages)
    return response