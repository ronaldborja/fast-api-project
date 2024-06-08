from typing import List, Type

from sqlalchemy.orm import Session
from schemas.cuenta_schema import CuentaRequestModel, CuentaResponseModel
from repositories.cuenta.impl import CuentaRepositoryImpl

class CuentaService:
    cuenta_repository = CuentaRepositoryImpl()

    @classmethod
    def create_cuenta(cls, cuenta: CuentaRequestModel, db: Session) -> CuentaResponseModel:
        cuenta_response = cls.cuenta_repository.create(cuenta, db)
        return cuenta_response

    @classmethod
    def get_cuenta(cls, cuenta_id: int, db: Session) -> CuentaResponseModel:
        cuenta = cls.cuenta_repository.get(cuenta_id, db)
        return cuenta

    @classmethod
    def update_cuenta(cls, cuenta_request: CuentaRequestModel, cuenta_id: int, db: Session) \
            -> CuentaResponseModel:
        cuenta = cls.cuenta_repository.update(cuenta_request, cuenta_id, db)
        return cuenta

    @classmethod
    def get_cuentas(cls, page: int, limit: int, db: Session) -> List[CuentaResponseModel]:
        cuentas = cls.cuenta_repository.get_all(page, limit, db)
        return cuentas
