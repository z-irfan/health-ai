from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import disease, treatment, analytics, chat

app = FastAPI(title="HealthAI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(disease.router)
app.include_router(treatment.router)
app.include_router(analytics.router)
app.include_router(chat.router)