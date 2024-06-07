from typing import List, Type

from sqlalchemy.orm import Session
from schemas.sucursal_schema import SucursalRequestModel, SucursalResponseModel
from repositories.sucursal.impl import SucursalRepositoryImpl


class SucursalService:
    sucursal_repository = SucursalRepositoryImpl()

    @classmethod
    def create_sucursal(cls, sucursal: SucursalRequestModel, db: Session) -> SucursalResponseModel:
        sucursal_response = cls.sucursal_repository.create(sucursal, db)
        return sucursal_response

    @classmethod
    def get_sucursal(cls, sucursal_id: int, db: Session) -> SucursalResponseModel:
        sucursal = cls.sucursal_repository.get(sucursal_id, db)
        return sucursal

    @classmethod
    def update_sucursal(cls, sucursal_request: SucursalRequestModel, sucursal_id: int, db: Session) \
            -> SucursalResponseModel:
        sucursal = cls.sucursal_repository.update(sucursal_request, sucursal_id, db)
        return sucursal

    @classmethod
    def get_sucursales(cls, page: int, limit: int, db: Session) -> List[SucursalResponseModel]:
        sucursales = cls.sucursal_repository.get_all(page, limit, db)
        return sucursales
