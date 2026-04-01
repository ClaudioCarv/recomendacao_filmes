from fastapi import FastAPI
from src.sistema_recomendacao.main import recomendar


app = FastAPI()

@app.get('/recomendacoes')
def recomendar_api(filme: str):
    return recomendar(filme)