from abc import ABC, abstractmethod
from typing import List

from sqlalchemy.orm import Session
from schemas.cliente_natural_schema import ClienteNaturalResponseModel, ClienteNaturalRequestModel

class ClienteNaturalRepository(ABC):
    @abstractmethod
    def create(self, cn: ClienteNaturalRequestModel, db: Session) -> ClienteNaturalResponseModel:
        pass

    @abstractmethod
    def get(self, cn_id: int, db: Session) -> ClienteNaturalResponseModel:
        pass

    @abstractmethod
    def update(self, cn_request: ClienteNaturalRequestModel, cn_id: int, db: Session) -> ClienteNaturalResponseModel:
        pass

    @abstractmethod
    def get_all(self, page: int, limit: int, db: Session) -> List[ClienteNaturalResponseModel]:
        pass
