from fastapi import FastAPI
from app.database import Base, engine
from app.route.pagamentos import pagamento
from app.route.usuario import usuario
from app.route.corrida import corrida
from app.route.veiculo import veiculo
from app.route.passageiro import passageiro
from app.route.motorista import motorista
from app.route.motorista_veiculo import motorista_veiculo
from app.route.avaliacao import avaliacao
from app.route.servico import servico
from app.route.classe import classe
from app.route.tipo_combustivel import tipo_combustivel
from app.route.modelo_veiculo import modelo_veiculo
from app.route.metodo_pagamento import metodo_pagamento

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(pagamento, usuario, corrida, veiculo, passageiro, motorista, motorista_veiculo,
                   avaliacao, servico, classe, tipo_combustivel, modelo_veiculo, metodo_pagamento )

@app.get("/")
async def health_check():
    return{"status": "API online!"}