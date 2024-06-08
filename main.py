from fastapi import FastAPI
from routers import sucursal_router, empleado_router, cn_router, organizacion_router, cuentas_router
from fastapi.middleware.cors import CORSMiddleware
import logging


app = FastAPI()

app.include_router(sucursal_router)
app.include_router(empleado_router)
app.include_router(cn_router)
app.include_router(organizacion_router)
app.include_router(cuentas_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

