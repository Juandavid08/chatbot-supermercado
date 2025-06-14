from fastapi import FastAPI
from app.database.db import Base, engine
from app.models import Cliente
from app.routes import users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Chatbot Retail IA")

app.include_router(users.router, prefix="/usuarios", tags=["Clientes"])

@app.get("/")
def home():
    return {"message": "API del Asistente Virtual lista"}
