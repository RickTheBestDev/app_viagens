from pydantic import BaseModel,Field
from typing import Optional, Annotated
from datetime import datetime

class MotoristaVeiculoSchema(BaseModel):
    id_motorista: Annotated[int, Field(
        gt=0, 
        description="ID do motorista no banco de dados",
        examples=[14]
    )]
    
    id_veiculo: Annotated[int, Field(
        gt=0, 
        description="ID do veículo que o motorista vai utilizar",
        examples=[7]
    )]
    
    datahora_inicio: Annotated[datetime, Field(
        description="Data e hora exata em que o motorista assumiu o veículo",
        examples=["2026-03-23T08:00:00"]
    )]
    
    # Optional com default=None, pois o motorista pode estar com o carro AGORA
    datahora_fim: Annotated[Optional[datetime], Field(
        default=None,
        description="Data e hora em que o motorista devolveu o veículo (Nulo se ainda estiver em uso)",
        examples=["2026-03-23T18:00:00"]
    )]

    class Config:
        from_attributes = True