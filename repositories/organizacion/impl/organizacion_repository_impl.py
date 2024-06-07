from typing import List, Type

from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from repositories.organizacion.organizacion_repository import OrganizacionRepository
from models.organizacion import Organizacion
from schemas.organizacion_schema import OrganizacionResponseModel, OrganizacionRequestModel

class OrganizacionRepositoryImpl(OrganizacionRepository):

    @staticmethod
    def create(organizacion: OrganizacionRequestModel, db: Session) -> OrganizacionResponseModel:
        try:
            new_organizacion = Organizacion(**organizacion.model_dump())
            db.add(new_organizacion)
            db.commit()           
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
        return new_organizacion

    @staticmethod
    def get(organizacion_id: int, db: Session) -> OrganizacionResponseModel:
        organizacion = db.query(Organizacion).filter_by(id=organizacion_id).first()
        if organizacion is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organizacion not found")
        return organizacion

    @staticmethod
    def update(organizacion_request: OrganizacionRequestModel, organizacion_id: int, db: Session) -> OrganizacionResponseModel:
        try:
            organizacion = db.query(Organizacion).filter_by(id=organizacion_id).first()
            if organizacion is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organizacion not found")
            organizacion.update(**organizacion_request.model_dump())
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        return organizacion
    
    @staticmethod
    def get_all(page: int, limit: int, db: Session) -> List[OrganizacionResponseModel]:
        organizaciones = db.query(Organizacion).offset(page).limit(limit).all()
        return organizaciones
    