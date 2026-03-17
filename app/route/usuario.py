from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.usuario import UsuarioModel
from app.schema.usuario import UsuarioSchema

usuario = APIRouter()

@usuario.post("/")
async def criar_usuario(dados: UsuarioSchema, db: Session = Depends(get_db)):
    novo_usuario = UsuarioModel(**dados.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@usuario.get("/")
async def listar_usuario(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()

@usuario.delete("/{id}/delete")
async def deletar_usuario(id: int, db: Session = Depends(get_db)):
    usuario_encontrado = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == id).first()
    
    if not usuario_encontrado:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f"o usuario com id {id} nao foi encontrado.")
    
    db.delete(usuario_encontrado)
    db.commit()
    return {"usuario deletado com sucesso"}

@usuario.put("/{id}")
async def atualizar_usuario(id: int, dados: UsuarioSchema = Depends(), db: Session = Depends(get_db)):
    usuario_encontrado = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == id).first()

    if not usuario_encontrado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"usuario com {id} nao encontrado")       
    
    dados_atualizados = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_atualizados.items():
        setattr(usuario_encontrado, chave, valor)

    db.commit()
    db.refresh(usuario_encontrado)
    return usuario_encontrado