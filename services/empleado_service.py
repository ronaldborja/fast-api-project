from typing import List, Type

from sqlalchemy.orm import Session
from schemas.empleado_schema import EmpleadoRequestModel, EmpleadoResponseModel
from repositories.empleados.impl import EmpleadoRepositoryImpl


class EmpleadoService:
    empleado_repository = EmpleadoRepositoryImpl()

    @classmethod
    def create_empleado(cls, empleado: EmpleadoRequestModel, db: Session) -> EmpleadoResponseModel:
        empleado_response = cls.empleado_repository.create(empleado, db)
        return empleado_response

    @classmethod
    def get_empleado(cls, empleado_id: int, db: Session) -> EmpleadoResponseModel:
        empleado = cls.empleado_repository.get(empleado_id, db)
        return empleado

    @classmethod
    def update_empleado(cls, empleado_request: EmpleadoRequestModel, empleado_id: int, db: Session) \
            -> EmpleadoResponseModel:
        empleado = cls.empleado_repository.update(empleado_request, empleado_id, db)
        return empleado

    @classmethod
    def get_empleados(cls, page: int, limit: int, db: Session) -> List[EmpleadoResponseModel]:
        empleados = cls.empleado_repository.get_all(page, limit, db)
        return empleados
