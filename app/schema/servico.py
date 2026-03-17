from pydantic import BaseModel
from typing import Optional

class ServicoSchema(BaseModel):
    nome_servico: str
    id_classe_minima: int

    class Config:
        from_attributes = True