from pydantic import BaseModel

class ModeloVeiculoSchema(BaseModel):
    nome_modelo: str
    cor: str
    fabricante: str
    ano: int
    capacidade: int
    propriedade: str
    id_combustivel: int

    class Config:
        from_attributes = True