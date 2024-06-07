from typing import List, Type

from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from repositories.sucursal.sucursal_repository import SucursalRepository
from models.sucursal import Sucursal
from schemas.sucursal_schema import SucursalResponseModel, SucursalRequestModel


class SucursalRepositoryImpl(SucursalRepository):

    @staticmethod
    def create(sucursal: SucursalRequestModel, db: Session) -> SucursalResponseModel:
        try:
            new_sucursal = Sucursal(**sucursal.model_dump())
            db.add(new_sucursal)
            db.commit()           
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
        return new_sucursal

    @staticmethod
    def get(sucursal_id: int, db: Session) -> SucursalResponseModel:
        sucursal = db.query(Sucursal).filter_by(id=sucursal_id).first()
        if sucursal is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sucursal not found")
        return sucursal

    @staticmethod
    def update(sucursal_request: SucursalRequestModel, sucursal_id: int, db: Session) -> SucursalResponseModel:
        try:
            sucursal = db.query(Sucursal).filter_by(id=sucursal_id).first()
            if sucursal is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sucursal not found")
            sucursal.update(**sucursal_request.model_dump())
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        return sucursal
    
    @staticmethod
    def get_all(page: int, limit: int, db: Session) -> List[SucursalResponseModel]:
        sucursales = db.query(Sucursal).offset(page).limit(limit).all()
        return sucursales
    