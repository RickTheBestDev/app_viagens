from pydantic import BaseModel,Field
from typing import Optional, Annotated

class MetodoPagamentoSchema(BaseModel):
    
    descricao: Annotated[str, Field(
        min_length=3,
        max_length=50,
        description="Descrição do método de pagamento (ex: Cartão de Crédito, PIX, Dinheiro).",
        examples=["Cartão de Crédito"]
    )]
    
    nome_financeira: Annotated[str, Field(
        min_length=2, # Tem bandeiras/bancos com nomes curtos, tipo "B3" ou "X"
        max_length=100,
        description="Nome da instituição financeira ou bandeira do cartão.",
        examples=["Mastercard"]
    )]
class Config:
        from_attributes = True