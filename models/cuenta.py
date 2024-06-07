from sqlalchemy import DateTime, ForeignKey, String
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from config.db import Base


class ClienteNatural(Base):
    __tablename__ = "cuenta"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    tipo_cuenta: Mapped[str] = mapped_column(primary_key=True, index=True)
    saldo_actual: Mapped[float] = mapped_column(primary_key=True, index=True)
    saldo_medio: Mapped[float] = mapped_column(primary_key=True, index=True)
    numero_cuenta: Mapped[int] = mapped_column(primary_key=True, index=True)
    fecha_apertura: Mapped[str] = mapped_column(primary_key=True, index=True)
    banco_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    sucursal_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    cliente_id: Mapped[int] = mapped_column(primary_key=True, index=True)

    def __str__(self):
        return f"<Cuenta {self.numero_cuenta}>"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
