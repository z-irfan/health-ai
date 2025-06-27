from fastapi import APIRouter
from pydantic import BaseModel
from backend.models import get_model_response

router = APIRouter(prefix="/disease", tags=["Disease Prediction"])

class SymptomInput(BaseModel):
    symptoms: str

@router.post("/predict")
def predict_disease(data: SymptomInput):
    prompt = f"You are a doctor. Based on the following symptoms, predict the disease: {data.symptoms}"
    response = get_model_response(prompt)
    return {"prediction": response}