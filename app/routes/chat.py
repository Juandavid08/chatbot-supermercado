from fastapi import APIRouter
from pydantic import BaseModel
from app.services.nlp_engine import construir_bot

router = APIRouter()
retriever = construir_bot()

# Modelo de entrada para el mensaje del usuario
class MensajeEntrada(BaseModel):
    identificacion: str
    mensaje: str

@router.post("/chat")
def responder_mensaje(data: MensajeEntrada):
    pregunta = data.mensaje

    # Usar el método moderno de LangChain
    resultados = retriever.invoke(pregunta)

    if resultados:
        respuesta = resultados[0].page_content
        return {"respuesta": respuesta}
    else:
        return {"respuesta": "Lo siento, no encontré una respuesta relacionada."}
