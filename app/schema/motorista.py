from pydantic import BaseModel, Field
from typing import Optional, Annotated
from decimal import Decimal

class MotoristaSchema(BaseModel):
    id_usuario: Annotated[int, Field(
        gt=0,
        description="ID do usuário vinculado a este perfil de motorista",
        examples=[42]
    )]
    
    
    media_avaliacao: Annotated[Optional[Decimal], Field(
        default=None,
        ge=0,
        le=5, 
        description="Média das avaliações do motorista (0.0 a 5.0)",
        examples=[4.8]
    )]
    
  
    cnh: Annotated[str, Field(
        min_length=11,
        max_length=11,
        pattern=r'^\d{11}$',
        description="Número da CNH com 11 dígitos (apenas números).",
        examples=["12345678901"]
    )]
    class Config:
        from_attributes = True