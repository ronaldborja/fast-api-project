from pydantic import ConfigDict, BaseModel

class CuentaRequestModel(BaseModel):
    id: int
    tipo_cuenta: str
    saldo_actual: float
    saldo_medio: float
    numero_cuenta: int 
    fecha_apertura: str 
    banco_id: int 
    sucursal_id: int 
    cliente_id: int 
    model_config: ConfigDict = {
    }


class CuentaResponseModel(BaseModel):
    id: int
    tipo_cuenta: str
    saldo_actual: float
    saldo_medio: float
    numero_cuenta: int 
    fecha_apertura: str 
    banco_id: int 
    sucursal_id: int 
    cliente_id: int 
    
    model_config = ConfigDict(from_attributes=True)
