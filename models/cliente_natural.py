from sqlalchemy import DateTime, ForeignKey, String
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from config.db import Base


class ClienteNatural(Base):
    __tablename__ = "clientes_naturales"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(primary_key=True, index=True)
    direccion: Mapped[str] = mapped_column(primary_key=True, index=True)
    fecha_nacimiento: Mapped[str] = mapped_column(primary_key=True, index=True)
    sexo: Mapped[str] = mapped_column(primary_key=True, index=True)

    def __str__(self):
        return f"<Cliente Natural {self.nombre}>"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
