from fastapi import APIRouter, Depends, HTTPException, status
#from app.helpers.auth import oauth2_scheme
from config.db import get_write_db
from sqlalchemy.orm import Session
from schemas.sucursal_schema import SucursalRequestModel, SucursalResponseModel
from services.sucursal_service import SucursalService 


sucursal_router = APIRouter(
    prefix='/sucursales',
    tags=["sucursales"],
    # dependencies=[Depends(oauth2_scheme)]
)

@sucursal_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_sucursal(sucursal: SucursalRequestModel, db: Session = Depends(get_write_db)) -> SucursalResponseModel:
    sucursal_created = SucursalService.create_sucursal(sucursal, db)
    return sucursal_created

@sucursal_router.get("/{sucursal_id}", response_model=SucursalResponseModel)
async def get_sucursal(sucursal_id: int, db: Session = Depends(get_write_db)) -> SucursalResponseModel:
    sucursal = SucursalService.get_sucursal(sucursal_id, db)
    return sucursal


@sucursal_router.put("/{sucursal_id}", response_model=SucursalResponseModel)
async def update_sucursal(sucursal_id: int, sucursal: SucursalRequestModel, db: Session = Depends(get_write_db)) -> SucursalResponseModel:
    sucursal = SucursalService.update_sucursal(sucursal, sucursal_id, db)
    return sucursal


@sucursal_router.get("/", response_model=list[SucursalResponseModel])
async def get_all_sucursales(page: int, limit: int, db: Session = Depends(get_write_db)) -> list[SucursalResponseModel]:
    sucursales = SucursalService.get_sucursales(page, limit, db)
    return sucursales
   
