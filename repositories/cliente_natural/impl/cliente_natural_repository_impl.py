from typing import List, Type

from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from repositories.cliente_natural.cliente_natural_repository import ClienteNaturalRepository
from models.cliente_natural import ClienteNatural
from schemas.cliente_natural_schema import ClienteNaturalResponseModel, ClienteNaturalRequestModel


class ClienteNaturalRepositoryImpl(ClienteNaturalRepository):

    @staticmethod
    def create(cn: ClienteNaturalRequestModel, db: Session) -> ClienteNaturalResponseModel:
        try:
            new_cn = ClienteNatural(**cn.model_dump())
            db.add(new_cn)
            db.commit()           
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
        return new_cn

    @staticmethod
    def get(cn_id: int, db: Session) -> ClienteNaturalResponseModel:
        cn = db.query(ClienteNatural).filter_by(id=cn_id).first()
        if cn is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente Natural not found")
        return cn

    @staticmethod
    def update(cn_request: ClienteNaturalRequestModel, cn_id: int, db: Session) -> ClienteNaturalResponseModel:
        try:
            cn = db.query(ClienteNatural).filter_by(id=cn_id).first()
            if cn is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente natural not found")
            cn.update(**cn_request.model_dump())
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        return cn
    
    @staticmethod
    def get_all(page: int, limit: int, db: Session) -> List[ClienteNaturalResponseModel]:
        cns = db.query(ClienteNatural).offset(page).limit(limit).all()
        return cns
    