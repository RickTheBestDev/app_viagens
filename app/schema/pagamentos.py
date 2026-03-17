from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class PagamentoSchema(BaseModel):
    id_corrida: int
    valor: Decimal
    id_metodo_pagamento: int
    datahora_transacao: datetime

    class Config:
        from_attributes = True