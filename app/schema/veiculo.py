from pydantic import BaseModel


class VeiculoSchema(BaseModel):
    placa: str
    id_modelo: int
    tem_seguro: int
    id_classe: int

    class Config:
        from_attributes = True