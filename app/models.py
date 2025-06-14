from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    identificacion = Column(String, unique=True, index=True)
    nombre = Column(String)
    telefono = Column(String)
    correo = Column(String)
