from pydantic import ConfigDict, BaseModel

class ClienteNaturalRequestModel(BaseModel):
    id: int
    nombre: str
    direccion: str
    fecha_nacimiento: str
    sexo: str

    model_config: ConfigDict = {
    }


class ClienteNaturalResponseModel(BaseModel):
    id: int
    nombre: str
    direccion: str
    fecha_nacimiento: str
    sexo: str
    
    model_config = ConfigDict(from_attributes=True)
