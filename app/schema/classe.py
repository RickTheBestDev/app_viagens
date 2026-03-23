from pydantic import BaseModel, Field
from typing import Optional, Annotated
from decimal import Decimal

class ClasseSchema(BaseModel):
    nome_classe: Annotated[str,Field(
        min_length=3, 
        max_length=50,
        description="Nome da classe do veículo"
    )]

    fator_preco: Annotated[Decimal, Field(
        gt=0, 
        description="Fator de preço para a classe do veículo"
    )]

    class Config:
        from_attributes = True