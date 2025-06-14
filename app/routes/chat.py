from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.database.crud import get_cliente_by_ident
from app.services.nlp_engine import construir_bot
from app.utils.validators import validar_identificacion

router = APIRouter()
retriever = construir_bot()

class MensajeEntrada(BaseModel):
    identificacion: str
    mensaje: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/chat")
def responder_mensaje(data: MensajeEntrada, db: Session = Depends(get_db)):
    # Validar ID
    if not validar_identificacion(data.identificacion):
        raise HTTPException(status_code=400, detail="Identificación inválida")

    cliente = get_cliente_by_ident(db, data.identificacion)

    # validar si no está registrado
    if not cliente:
        return {
            "respuesta": "No encontré tu identificación. Por favor regístrate en /usuarios/registrar antes de continuar.",
            "estado": "nuevo"
        }

    # validar si esta registrado
    if not data.mensaje:
        raise HTTPException(status_code=400, detail="Por favor escribe una pregunta.")
    
    resultados = retriever.invoke(data.mensaje)

    if resultados:
        return {
            "respuesta": resultados[0].page_content,
            "estado": "frecuente",
            "cliente": cliente.nombre
        }
    else:
        return {
            "respuesta": "Lo siento, no encontré una respuesta relacionada.",
            "estado": "frecuente"
        }
