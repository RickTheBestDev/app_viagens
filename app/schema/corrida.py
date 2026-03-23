from pydantic import BaseModel, Field
from typing import Optional, Annotated
from datetime import datetime
from decimal import Decimal

class CorridaSchema(BaseModel):

    id_passageiro: Annotated[int, Field(gt=0, description="ID do passageiro solicitante")]
    id_motorista: Annotated[int, Field(gt=0, description="ID do motorista")]
    id_servico: Annotated[int, Field(gt=0, description="ID da categoria/serviço escolhido")]
   
    id_avaliacao: Annotated[Optional[int], Field(
        default=None, 
        gt=0, 
        description="ID da avaliação, caso já tenha sido feita"
    )]

    datahora_inicio: Annotated[datetime, Field(
        description="Data e hora de início da corrida",
    )]

    datahora_fim: Annotated[Optional[datetime], Field(
        default=None,
        description="Data e hora de finalização da corrida",
        examples=["2026-03-23T11:15:00"]
    )]

    local_partida: Annotated[str, Field(
        min_length=5, 
        max_length=255, 
        description="Endereço completo ou coordenadas de origem"
    )]

    local_destino: Annotated[str, Field(
        min_length=5, 
        max_length=255, 
        description="Endereço completo ou coordenadas de destino"
    )]

    valor_estimado: Annotated[Decimal, Field(
        ge=0,
        description="Valor estimado da corrida"
    )]
    status: Annotated[str, Field(
        min_length=3,
        max_length=20,
        description="Situação atual da viagem",
    )]

    class Config:
        from_attributes = True