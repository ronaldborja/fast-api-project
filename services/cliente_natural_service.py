from typing import List, Type

from sqlalchemy.orm import Session
from schemas.cliente_natural_schema import ClienteNaturalRequestModel, ClienteNaturalResponseModel
from repositories.cliente_natural.impl import ClienteNaturalRepositoryImpl


class ClienteNaturalService:
    natural_repository = ClienteNaturalRepositoryImpl()

    @classmethod
    def create_cn(cls, cn: ClienteNaturalRequestModel, db: Session) -> ClienteNaturalResponseModel:
        natural_response = cls.natural_repository.create(cn, db)
        return natural_response

    @classmethod
    def get_cn(cls, natural_id: int, db: Session) -> ClienteNaturalResponseModel:
        cn = cls.natural_repository.get(natural_id, db)
        return cn

    @classmethod
    def update_cn(cls, natural_request: ClienteNaturalRequestModel, natural_id: int, db: Session) \
            -> ClienteNaturalResponseModel:
        cn = cls.natural_repository.update(natural_request, natural_id, db)
        return cn

    @classmethod
    def get_cns(cls, page: int, limit: int, db: Session) -> List[ClienteNaturalResponseModel]:
        cns = cls.natural_repository.get_all(page, limit, db)
        return cns
