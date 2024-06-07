from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session
from schemas.organizacion_schema import OrganizacionResponseModel, OrganizacionRequestModel

class OrganizacionRepository(ABC):
    @abstractmethod
    def create(self, organizacion: OrganizacionRequestModel, db: Session) -> OrganizacionResponseModel:
        pass

    @abstractmethod
    def get(self, organizacion_id: int, db: Session) -> OrganizacionResponseModel:
        pass

    @abstractmethod
    def update(self, organizacion_request: OrganizacionRequestModel, organizacion_id: int, db: Session) -> OrganizacionResponseModel:
        pass

    @abstractmethod
    def get_all(self, page: int, limit: int, db: Session) -> List[OrganizacionResponseModel]:
        pass
