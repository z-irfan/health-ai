from fastapi import APIRouter
from pydantic import BaseModel
from backend.models import get_model_response

router = APIRouter(prefix="/treatment", tags=["Treatment Plans"])

class ConditionInput(BaseModel):
    condition: str

@router.post("/plan")
def treatment_plan(data: ConditionInput):
    prompt = f"You are a medical expert. Suggest a treatment plan for: {data.condition}"
    response = get_model_response(prompt)
    return {"plan": response}