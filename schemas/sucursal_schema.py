from pydantic import ConfigDict, BaseModel

class SucursalRequestModel(BaseModel):
    id: int
    direccion: str
    codigo_postal: str

    model_config: ConfigDict = {
        'example': {
            "direccion": "Cartagena",
            "Codigo Postal": "2305",
        }
    }


class SucursalResponseModel(BaseModel):
    id: int
    direccion: str
    codigo_postal: str

    model_config = ConfigDict(from_attributes=True)
