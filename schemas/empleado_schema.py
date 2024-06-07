from pydantic import ConfigDict, BaseModel

class EmpleadoRequestModel(BaseModel):
    dni: int
    nombre: str
    direccion: str
    telefono: str
    fecha_nacimiento: str
    sexo: str
    sucursal_id: int

    model_config: ConfigDict = {
    }


class EmpleadoResponseModel(BaseModel):
    dni: int
    nombre: str
    direccion: str
    telefono: str
    fecha_nacimiento: str
    sexo: str
    sucursal_id: int
    
    model_config = ConfigDict(from_attributes=True)
