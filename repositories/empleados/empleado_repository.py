from abc import ABC, abstractmethod
from typing import List

from sqlalchemy.orm import Session
from schemas.empleado_schema import EmpleadoResponseModel, EmpleadoRequestModel

class EmpleadoRepository(ABC):
    @abstractmethod
    def create(self, empleado: EmpleadoRequestModel, db: Session) -> EmpleadoResponseModel:
        pass

    @abstractmethod
    def get(self, empleado_dni: int, db: Session) -> EmpleadoResponseModel:
        pass

    @abstractmethod
    def update(self, empleado_request: EmpleadoRequestModel, empleado_dni: int, db: Session) -> EmpleadoResponseModel:
        pass

    @abstractmethod
    def get_all(self, page: int, limit: int, db: Session) -> List[EmpleadoResponseModel]:
        pass
