from fastapi import APIRouter, Depends, HTTPException, status
#from app.helpers.auth import oauth2_scheme
from config.db import get_write_db
from sqlalchemy.orm import Session
from schemas.cuenta_schema import CuentaRequestModel, CuentaResponseModel
from services.cuenta_service import CuentaService 


cuentas_router = APIRouter(
    prefix='/cuentas',
    tags=["cuentas"],
    # dependencies=[Depends(oauth2_scheme)]
)

@cuentas_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_cuenta(cuenta: CuentaRequestModel, db: Session = Depends(get_write_db)) -> CuentaResponseModel:
    cuenta_created = CuentaService.create_cuenta(cuenta, db)
    return cuenta_created

@cuentas_router.get("/{cuenta_id}", response_model=CuentaResponseModel)
async def get_cuenta(cuenta_id: int, db: Session = Depends(get_write_db)) -> CuentaResponseModel:
    cuenta = CuentaService.get_cuenta(cuenta_id, db)
    return cuenta


@cuentas_router.put("/{cuenta_id}", response_model=CuentaResponseModel)
async def update_cuenta(cuenta_id: int, cuenta: CuentaRequestModel, db: Session = Depends(get_write_db)) -> CuentaResponseModel:
    cuenta = CuentaService.update_cuenta(cuenta, cuenta_id, db)
    return cuenta


@cuentas_router.get("/", response_model=list[CuentaResponseModel])
async def get_all_cuentas(page: int, limit: int, db: Session = Depends(get_write_db)) -> list[CuentaResponseModel]:
    cuentas = CuentaService.get_cuentas(page, limit, db)
    return cuentas