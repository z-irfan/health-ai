from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/analytics", tags=["Health Analytics"])

class VitalsInput(BaseModel):
    heart_rate: list[int]
    blood_pressure: list[tuple[int, int]]
    glucose: list[int]

@router.post("/vitals")
def get_vitals(data: VitalsInput):
    return {
        "heart_rate": data.heart_rate,
        "blood_pressure": data.blood_pressure,
        "glucose": data.glucose
    }