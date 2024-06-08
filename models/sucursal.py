from sqlalchemy import DateTime, ForeignKey, String
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from config.db import Base


class Sucursal(Base):
    __tablename__ = "sucursales"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    direccion: Mapped[str] = mapped_column(nullable=False, index=True)
    codigo_postal: Mapped[str] = mapped_column(nullable=False, index=True)

    def __str__(self):
        return f"<Sucursal {self.direccion}>"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
