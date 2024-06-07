from fastapi import APIRouter, Depends, HTTPException, status
#from app.helpers.auth import oauth2_scheme
from config.db import get_write_db
from sqlalchemy.orm import Session
from schemas.empleado_schema import EmpleadoRequestModel, EmpleadoResponseModel
from services.empleado_service import EmpleadoService 


empleado_router = APIRouter(
    prefix='/empleados',
    tags=["empleados"],
    # dependencies=[Depends(oauth2_scheme)]
)

@empleado_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_empleado(empleado: EmpleadoRequestModel, db: Session = Depends(get_write_db)) -> EmpleadoResponseModel:
    empleado_created = EmpleadoService.create_empleado(empleado, db)
    return empleado_created

@empleado_router.get("/{empleado_id}", response_model=EmpleadoResponseModel)
async def get_empleado(empleado_id: int, db: Session = Depends(get_write_db)) -> EmpleadoResponseModel:
    empleado = EmpleadoService.get_empleado(empleado_id, db)
    return empleado


@empleado_router.put("/{empleado_id}", response_model=EmpleadoResponseModel)
async def update_empleado(empleado_id: int, empleado: EmpleadoRequestModel, db: Session = Depends(get_write_db)) -> EmpleadoResponseModel:
    empleado = EmpleadoService.update_empleado(empleado, empleado_id, db)
    return empleado


@empleado_router.get("/", response_model=list[EmpleadoResponseModel])
async def get_all_empleados(page: int, limit: int, db: Session = Depends(get_write_db)) -> list[EmpleadoResponseModel]:
    empleados = EmpleadoService.get_empleados(page, limit, db)
    return empleados
