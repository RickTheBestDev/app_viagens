from pydantic import BaseModel, Field
from typing import Optional, Annotated
from datetime import datetime

class AvaliacaoSchema(BaseModel):
    nota_passageiro: Annotated[Optional[int], Field(
        ge=1, le=5, description="Nota do passageiro (1 a 5)"
    )]= None
    nota_motorista: Annotated[Optional[int], Field(
        ge=1, le=5, description="Nota do passageiro (1 a 5)"
    )]= None
    datahora_limite: Optional[datetime] = Field(
        default=None, 
        description="Data e hora limite"
    )

    class Config:
        from_attributes = True