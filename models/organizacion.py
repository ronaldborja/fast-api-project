from sqlalchemy import DateTime, ForeignKey, String
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from config.db import Base


class Organizacion(Base):
    __tablename__ = "organizaciones"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(primary_key=True, index=True)
    direccion: Mapped[str] = mapped_column(primary_key=True, index=True)
    tipo_organizacion: Mapped[str] = mapped_column(primary_key=True, index=True)
    num_empleados: Mapped[int] = mapped_column(primary_key=True, index=True)
    representante: Mapped[str] = mapped_column(primary_key=True, index=True)

    def __str__(self):
        return f"<Organizacion {self.nombre}>"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
