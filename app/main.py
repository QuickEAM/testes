from fastapi import FastAPI
from app.api import categoria

app = FastAPI(title="GPP API")

app.include_router(categoria.router, prefix="/categorias")

@app.get("/")
def root():
    return {"mensagem": "API do GPP está rodando!"}
