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


@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = process_chat(request.messages)
        return response

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return {"error": str(e)}