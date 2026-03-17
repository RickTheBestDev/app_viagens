from pydantic import BaseModel
from typing import Optional

class MetodoPagamentoSchema(BaseModel):
    
    descricao: str
    nome_financeira: str

    class Config:
        from_attributes = True