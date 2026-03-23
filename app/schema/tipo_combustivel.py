from pydantic import BaseModel,Field
from typing import Optional, Annotated
from decimal import Decimal

class TipoCombustivelSchema(BaseModel):
    
    descricao: Annotated[str, Field(
        min_length=3,
        max_length=50,
        description="Nome ou descrição do tipo de combustível (ex: Gasolina, Etanol, GNV, Elétrico)",
        examples=["Etanol"]
    )]
    
   
    fator_carbono: Annotated[Decimal, Field(
        ge=0,
        description="Fator multiplicador para cálculo de emissão de carbono",
        examples=[0.85]
    )]

    class Config:
        from_attributes = True