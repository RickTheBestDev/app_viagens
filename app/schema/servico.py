from pydantic import BaseModel, Field
from typing import Optional, Annotated


class ServicoSchema(BaseModel):
    
    nome_servico: Annotated[str, Field(
        min_length=1,
        max_length=50,
        description="Nome do serviço oferecido (ex: X, Comfort, Black, Entregas)",
        examples=["Comfort"]
    )]
    
   
    id_classe_minima: Annotated[int, Field(
        gt=0,
        description="ID da classe mínima de veículo exigida para realizar este serviço",
        examples=[2]
    )]

    class Config:
        from_attributes = True