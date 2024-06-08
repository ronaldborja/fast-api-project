from abc import ABC, abstractmethod
from typing import List

from sqlalchemy.orm import Session
from schemas.cuenta_schema import CuentaResponseModel, CuentaRequestModel

class CuentaRepository(ABC):
    @abstractmethod
    def create(self, cuenta: CuentaRequestModel, db: Session) -> CuentaResponseModel:
        pass

    @abstractmethod
    def get(self, cuenta: int, db: Session) -> CuentaResponseModel:
        pass

    @abstractmethod
    def update(self, cuenta_request: CuentaRequestModel, cn_id: int, db: Session) -> CuentaResponseModel:
        pass

    @abstractmethod
    def get_all(self, page: int, limit: int, db: Session) -> List[CuentaResponseModel]:
        pass
