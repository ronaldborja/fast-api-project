from typing import List, Type

from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from repositories.empleados.empleado_repository import EmpleadoRepository
from models.empleado import Empleado
from schemas.empleado_schema import EmpleadoResponseModel, EmpleadoRequestModel


class EmpleadoRepositoryImpl(EmpleadoRepository):

    @staticmethod
    def create(empleado: EmpleadoRequestModel, db: Session) -> EmpleadoResponseModel:
        try:
            new_empleado = Empleado(**empleado.model_dump())
            db.add(new_empleado)
            db.commit()           
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
        return new_empleado

    @staticmethod
    def get(empleado_dni: int, db: Session) -> EmpleadoResponseModel:
        empleado = db.query(Empleado).filter_by(dni=empleado_dni).first()
        if empleado is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Empleado not found")
        return empleado

    @staticmethod
    def update(empleado_request: EmpleadoRequestModel, empleado_dni: int, db: Session) -> EmpleadoResponseModel:
        try:
            empleado = db.query(Empleado).filter_by(dni=empleado_dni).first()
            if empleado is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Empleado not found")
            empleado.update(**empleado_request.model_dump())
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        return empleado
    
    @staticmethod
    def get_all(page: int, limit: int, db: Session) -> List[EmpleadoResponseModel]:
        sucursales = db.query(Empleado).offset(page).limit(limit).all()
        return sucursales
    