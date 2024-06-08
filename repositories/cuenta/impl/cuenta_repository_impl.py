from typing import List, Type

from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from repositories.cuenta.cuenta_repository import CuentaRepository
from models.cuenta import Cuenta
from schemas.cuenta_schema import CuentaResponseModel, CuentaRequestModel


class CuentaRepositoryImpl(CuentaRepository):

    @staticmethod
    def create(cuenta: CuentaRequestModel, db: Session) -> CuentaResponseModel:
        try:
            new_cuenta = Cuenta(**cuenta.model_dump())
            db.add(new_cuenta)
            db.commit()           
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
        return new_cuenta

    @staticmethod
    def get(cuenta_id: int, db: Session) -> CuentaResponseModel:
        cuenta = db.query(Cuenta).filter_by(id=cuenta_id).first()
        if cuenta is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cuenta not found")
        return cuenta

    @staticmethod
    def update(cuenta_request: CuentaRequestModel, cuenta_id: int, db: Session) -> CuentaResponseModel:
        try:
            cuenta = db.query(Cuenta).filter_by(id=cuenta_id).first()
            if cuenta is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cuenta not found")
            cuenta.update(**cuenta.model_dump())
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        return cn
    
    @staticmethod
    def get_all(page: int, limit: int, db: Session) -> List[CuentaResponseModel]:
        cuentas = db.query(Cuenta).offset(page).limit(limit).all()
        return cuentas
    