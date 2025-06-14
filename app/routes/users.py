from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.database.crud import get_cliente_by_ident, create_cliente
from app.utils.validators import (
    validar_identificacion,
    validar_nombre,
    validar_telefono,
    validar_correo,
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/registrar")
def registrar_cliente(cliente: dict, db: Session = Depends(get_db)):
    identificacion = cliente.get("identificacion", "")
    nombre = cliente.get("nombre", "")
    telefono = cliente.get("telefono", "")
    correo = cliente.get("correo", "")

    if not validar_identificacion(identificacion):
        raise HTTPException(status_code=400, detail="Identificación inválida")
    if get_cliente_by_ident(db, identificacion):
        raise HTTPException(status_code=400, detail="Identificación ya registrada")
    if not validar_nombre(nombre):
        raise HTTPException(status_code=400, detail="Nombre inválido")
    if not validar_telefono(telefono):
        raise HTTPException(status_code=400, detail="Teléfono inválido")
    if not validar_correo(correo):
        raise HTTPException(status_code=400, detail="Correo inválido")

    nuevo_cliente = {
        "identificacion": identificacion,
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo,
    }
    creado = create_cliente(db, nuevo_cliente)
    return {"mensaje": "Cliente registrado exitosamente", "cliente": creado.identificacion}

@router.get("/verificar/{identificacion}")
def verificar_cliente(identificacion: str, db: Session = Depends(get_db)):
    if not validar_identificacion(identificacion):
        raise HTTPException(status_code=400, detail="Identificación inválida")

    cliente = get_cliente_by_ident(db, identificacion)
    if cliente:
        return {"mensaje": "Cliente encontrado", "nombre": cliente.nombre}
    else:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
