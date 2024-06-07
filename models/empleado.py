from sqlalchemy import DateTime, ForeignKey, String
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from config.db import Base


class Empleado(Base):
    __tablename__ = "empleados"

    dni: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(primary_key=True, index=True)
    direccion: Mapped[str] = mapped_column(primary_key=True, index=True)
    telefono: Mapped[str] = mapped_column(primary_key=True, index=True)
    fecha_nacimiento: Mapped[str] = mapped_column(primary_key=True, index=True)
    sexo: Mapped[str] = mapped_column(primary_key=True, index=True)
    sucursal_id: Mapped[int] = mapped_column(primary_key=True, index=True)

    def __str__(self):
        return f"<Empleado {self.nombre}>"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
