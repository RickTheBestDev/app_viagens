from pydantic import BaseModel, Field
from typing import Optional, Annotated


class VeiculoSchema(BaseModel):
    
    placa: Annotated[str, Field(
        min_length=7,
        max_length=7,
        description="Placa do veículo (Formato padrão ou Mercosul, sem espaços ou traços)",
        examples=["BRA2E19", "ABC1234"]
    )]
    
    id_modelo: Annotated[int, Field(
        gt=0,
        description="ID do modelo do veículo (vinculado ao ModeloVeiculoSchema)",
        examples=[5]
    )]
    
  
    tem_seguro: Annotated[int, Field(
        ge=0,
        le=1,
        description="O veículo possui seguro? (0 = Não, 1 = Sim)",
        examples=[1]
    )]
    
    id_classe: Annotated[int, Field(
        gt=0,
        description="ID da classe/categoria do veículo",
        examples=[2]
    )]
    class Config:
        from_attributes = True