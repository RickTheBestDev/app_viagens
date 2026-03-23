from pydantic import BaseModel, Field
from typing import Optional, Annotated
from datetime import datetime
from decimal import Decimal

class PagamentoSchema(BaseModel):
   
    id_corrida: Annotated[int, Field(
        gt=0,
        description="ID da corrida associada a este pagamento",
        examples=[105]
    )]
    
   
    valor: Annotated[Decimal, Field(
        ge=0,
        description="Valor total cobrado na transação",
        examples=[25.50]
    )]
    
    id_metodo_pagamento: Annotated[int, Field(
        gt=0,
        description="ID do método de pagamento utilizado (ex: 1 para PIX, 2 para Cartão)",
        examples=[2]
    )]
    
  
    datahora_transacao: Annotated[datetime, Field(
        description="Data e hora exata em que o pagamento foi processado",
        examples=["2026-03-23T10:45:00"]
    )]

    class Config:
        from_attributes = True