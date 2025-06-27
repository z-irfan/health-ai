from fastapi import APIRouter, Request
from backend.models import get_model_response

router = APIRouter()

# Hardcoded symptom-to-disease mapping
DISEASE_DB = {
    "fever, cough, fatigue": "You may be experiencing the flu. Stay hydrated and consult a doctor if symptoms worsen.",
    "headache, nausea, sensitivity to light": "These symptoms are commonly linked to migraine.",
    "chest pain, shortness of breath": "These may be signs of a heart condition. Seek immediate medical attention.",
    "runny nose, sneezing, itchy eyes": "This sounds like allergic rhinitis.",
    "fever, sore throat, body ache": "You might have a viral infection like COVID-19 or influenza."
}

@router.post("/predict")
async def predict_disease(request: Request):
    body = await request.json()
    symptoms = body.get("symptoms", "").lower()

    for key, response in DISEASE_DB.items():
        if all(s in symptoms for s in key.split(", ")):
            return {"prediction": response}

    # If no match, use AI fallback
    prompt = f"You are a medical expert. Based on these symptoms, suggest the most likely disease: {symptoms}"
    prediction = get_model_response(prompt)
    return {"prediction": prediction}
