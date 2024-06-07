from typing import List, Type

from sqlalchemy.orm import Session
from schemas.organizacion_schema import OrganizacionRequestModel, OrganizacionResponseModel
from repositories.organizacion.impl import OrganizacionRepositoryImpl


class OrganizacionService:
    organizacion_repository = OrganizacionRepositoryImpl()

    @classmethod
    def create_organizacion(cls, organizacion: OrganizacionRequestModel, db: Session) -> OrganizacionResponseModel:
        organizacion_response = cls.organizacion_repository.create(organizacion, db)
        return organizacion_response

    @classmethod
    def get_organizacion(cls, organizacion_id: int, db: Session) -> OrganizacionResponseModel:
        organizacion = cls.organizacion_repository.get(organizacion_id, db)
        return organizacion

    @classmethod
    def update_organizacion(cls, organizacion_request: OrganizacionRequestModel, organizacion_id: int, db: Session) \
            -> OrganizacionResponseModel:
        organizacion = cls.organizacion_repository.update(organizacion_request, organizacion_id, db)
        return organizacion

    @classmethod
    def get_organizaciones(cls, page: int, limit: int, db: Session) -> List[OrganizacionResponseModel]:
        organizaciones = cls.organizacion_repository.get_all(page, limit, db)
        return organizaciones
