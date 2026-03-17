from pydantic import BaseModel
from datetime import date

class UsuarioSchema(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    idade: int
    senha: str
    email: str
    usuario: str

    class Config:
        from_attributes = True