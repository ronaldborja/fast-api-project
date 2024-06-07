from abc import ABC, abstractmethod
from typing import List

from sqlalchemy.orm import Session
from schemas.sucursal_schema import SucursalResponseModel, SucursalRequestModel


class SucursalRepository(ABC):
    @abstractmethod
    def create(self, sucursal: SucursalRequestModel, db: Session) -> SucursalResponseModel:
        pass

    @abstractmethod
    def get(self, sucursal_id: int, db: Session) -> SucursalResponseModel:
        pass

    @abstractmethod
    def update(self, sucursal_request: SucursalRequestModel, sucursal_id: int, db: Session) -> SucursalResponseModel:
        pass

    @abstractmethod
    def get_all(self, page: int, limit: int, db: Session) -> List[SucursalResponseModel]:
        pass
