from sqlalchemy.orm import Session
from app.models import Cliente

def get_cliente_by_ident(db: Session, identificacion: str):
    return db.query(Cliente).filter(Cliente.identificacion == identificacion).first()

def create_cliente(db: Session, cliente_data: dict):
    nuevo_cliente = Cliente(**cliente_data)
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente
