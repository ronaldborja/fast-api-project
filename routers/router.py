from fastapi import APIRouter

sucursal = APIRouter()

@sucursal.get("/")
def root():
    return {"message": "Hola mundo!!!"}
