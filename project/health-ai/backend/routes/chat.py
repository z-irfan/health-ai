from fastapi import APIRouter, Request
from backend.models import get_model_response

router = APIRouter()

# Optional: predefined chat FAQs
CHAT_DB = {
    "what should i do for high blood pressure": "Maintain a low-sodium diet, exercise regularly, and take medications if prescribed. Monitor your BP frequently.",
    "how to reduce stress": "Practice deep breathing, get regular sleep, exercise, and avoid too much caffeine. Meditation also helps.",
    "what are symptoms of covid": "Common COVID-19 symptoms include fever, cough, sore throat, loss of taste/smell, and fatigue.",
    "how to improve immunity": "Eat fruits, sleep well, stay active, and consider Vitamin C & D supplements after consulting a doctor."
}

@router.post("/chat")
async def chat_with_bot(request: Request):
    body = await request.json()
    message = body.get("message", "").lower()

    for key, response in CHAT_DB.items():
        if key in message:
            return {"response": response}

    # Fallback to AI
    prompt = f"You are a medical assistant. Respond helpfully to the user's question: {message}"
    response = get_model_response(prompt)
    return {"response": response}
