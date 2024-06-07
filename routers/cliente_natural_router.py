from fastapi import APIRouter, Depends, HTTPException, status
#from app.helpers.auth import oauth2_scheme
from config.db import get_write_db
from sqlalchemy.orm import Session
from schemas.cliente_natural_schema import ClienteNaturalRequestModel, ClienteNaturalResponseModel
from services.cliente_natural_service import ClienteNaturalService 


cn_router = APIRouter(
    prefix='/naturales',
    tags=["naturales"],
    # dependencies=[Depends(oauth2_scheme)]
)

@cn_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_cn(cn: ClienteNaturalRequestModel, db: Session = Depends(get_write_db)) -> ClienteNaturalResponseModel:
    natural_created = ClienteNaturalService.create_cn(cn, db)
    return natural_created

@cn_router.get("/{natural_id}", response_model=ClienteNaturalResponseModel)
async def get_cn(natural_id: int, db: Session = Depends(get_write_db)) -> ClienteNaturalResponseModel:
    natural = ClienteNaturalService.get_cn(natural_id, db)
    return natural


@cn_router.put("/{natural_id}", response_model=ClienteNaturalResponseModel)
async def update_cn(natural_id: int, natural: ClienteNaturalRequestModel, db: Session = Depends(get_write_db)) -> ClienteNaturalResponseModel:
    natural = ClienteNaturalService.update_cn(natural, natural_id, db)
    return natural


@cn_router.get("/", response_model=list[ClienteNaturalResponseModel])
async def get_all_cns(page: int, limit: int, db: Session = Depends(get_write_db)) -> list[ClienteNaturalResponseModel]:
    cns = ClienteNaturalService.get_cns(page, limit, db)
    return cns
