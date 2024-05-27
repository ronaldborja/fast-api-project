from fastapi import FastAPI
from routers.router import sucursal

app = FastAPI()

app.include_router(sucursal)