from pydantic import BaseModel, Field
from typing import Optional, Annotated
from datetime import date

class UsuarioSchema(BaseModel):
    nome: Annotated[str, Field(
        min_length=3, 
        max_length=100, 
        description="Nome completo do usuário",
        examples=["João Silva"]
    )]
    
   
    cpf: Annotated[str, Field(
        min_length=11, 
        max_length=11, 
        pattern=r'^\d{11}$', 
        description="CPF (apenas os 11 números)",
        examples=["12345678901"]
    )]
    
    data_nascimento: Annotated[date, Field(
        description="Data de nascimento",
        examples=["1995-05-15"]
    )]
    
    
    idade: Annotated[int, Field(
        ge=18, 
        le=120, 
        description="Idade do usuário (mínimo 18 anos)"
    )]
    
    
    senha: Annotated[str, Field(
        min_length=8, 
        description="Senha de acesso (mínimo 8 caracteres)"
    )]
    
   
    email: Annotated[str, Field(

        description="E-mail válido para contato",
        examples=["joao@email.com"]
    )]
    
    usuario: Annotated[str, Field(
        min_length=3, 
        max_length=20, 
        description="Username único no sistema",
        examples=["joaosilva95"]
    )]

    class Config:
        from_attributes = True