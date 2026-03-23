from pydantic import BaseModel, Field
from typing import Optional, Annotated
from decimal import Decimal

class PassageiroSchema(BaseModel):
   
    id_usuario: Annotated[int, Field(
        gt=0,
        description="ID do usuário vinculado a este perfil de passageiro",
        examples=[42]
    )]
    
   
    media_avaliacao: Annotated[Optional[Decimal], Field(
        default=None,
        ge=0, 
        le=5, 
        description="Média das avaliações recebidas pelo passageiro (0.0 a 5.0)",
        examples=[4.9]
    )]

    class Config:
        from_attributes = True