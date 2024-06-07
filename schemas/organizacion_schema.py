from pydantic import ConfigDict, BaseModel

class OrganizacionRequestModel(BaseModel):
    id: int
    nombre: str
    direccion: str
    tipo_organizacion: str
    num_empleados: int
    representante: str


    model_config: ConfigDict = {
    }

class OrganizacionResponseModel(BaseModel):
    id: int
    nombre: str
    direccion: str
    tipo_organizacion: str
    num_empleados: int
    representante: str
    
    model_config = ConfigDict(from_attributes=True)
