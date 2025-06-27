from fastapi import APIRouter
from pydantic import BaseModel
from backend.models import get_model_response

router = APIRouter(prefix="/chat", tags=["Patient Chat"])

class ChatInput(BaseModel):
    message: str

@router.post("/message")
def chat_with_ai(data: ChatInput):
    prompt = f"You are a helpful healthcare assistant. {data.message}"
    reply = get_model_response(prompt)
    return {"reply": reply}