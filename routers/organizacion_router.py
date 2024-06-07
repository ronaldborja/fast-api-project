from fastapi import APIRouter, Depends, HTTPException, status
#from app.helpers.auth import oauth2_scheme
from config.db import get_write_db
from sqlalchemy.orm import Session
from schemas.organizacion_schema import OrganizacionRequestModel, OrganizacionResponseModel
from services.organizacion_service import OrganizacionService 


organizacion_router = APIRouter(
    prefix='/organizaciones',
    tags=["organizaciones"],
    # dependencies=[Depends(oauth2_scheme)]
)

@organizacion_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_organizacion(organizacion: OrganizacionRequestModel, db: Session = Depends(get_write_db)) -> OrganizacionResponseModel:
    organizacion_created = OrganizacionService.create_organizacion(organizacion, db)
    return organizacion_created

@organizacion_router.get("/{organizacion_id}", response_model=OrganizacionResponseModel)
async def get_organizacion(organizacion_id: int, db: Session = Depends(get_write_db)) -> OrganizacionResponseModel:
    organizacion = OrganizacionService.get_organizacion(organizacion_id, db)
    return organizacion


@organizacion_router.put("/{organizacion_id}", response_model=OrganizacionResponseModel)
async def update_organizacion(organizacion_id: int, organizacion: OrganizacionRequestModel, db: Session = Depends(get_write_db)) -> OrganizacionResponseModel:
    organizacion = OrganizacionService.update_organizacion(organizacion, organizacion_id, db)
    return organizacion


@organizacion_router.get("/", response_model=list[OrganizacionResponseModel])
async def get_all_organizaciones(page: int, limit: int, db: Session = Depends(get_write_db)) -> list[OrganizacionResponseModel]:
    organizaciones = OrganizacionService.get_organizaciones(page, limit, db)
    return organizaciones
   
