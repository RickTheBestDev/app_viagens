from pydantic import BaseModel, Field
from typing import Optional, Annotated

class ModeloVeiculoSchema(BaseModel):
    nome_modelo: Annotated[str, Field(
        min_length=2, 
        max_length=100,
        description="Nome do modelo do veículo",
        examples=["Corolla"]
    )]
    
    cor: Annotated[str, Field(
        min_length=3,
        max_length=30,
        description="Cor predominante do veículo",
        examples=["Prata"]
    )]
    
    fabricante: Annotated[str, Field(
        min_length=2,
        max_length=50,
        description="Marca/Fabricante do veículo",
        examples=["Toyota"]
    )]
    
   
    ano: Annotated[int, Field(
        ge=1950, 
        le=2027, 
        description="Ano de fabricação ou modelo do veículo",
        examples=[2024]
    )]
    
   
    capacidade: Annotated[int, Field(
        ge=2, 
        le=60, 
        description="Capacidade máxima de pessoas no veículo",
        examples=[5]
    )]
    
    propriedade: Annotated[str, Field(
        min_length=5,
        max_length=30,
        description="Tipo de posse do veículo (ex: Próprio, Alugado, Financiado)",
        examples=["Próprio"]
    )]
    
    
    id_combustivel: Annotated[int, Field(
        gt=0,
        description="ID do tipo de combustível no banco de dados",
        examples=[1]
    )]

    class Config:
        from_attributes = True