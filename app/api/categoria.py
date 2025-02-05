from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import criar_categoria, obter_categoria

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar(cod_categoria: str, descricao: str, cod_idioma: str, db: Session = Depends(get_db)):
    return criar_categoria(db, cod_categoria, descricao, cod_idioma)

@router.get("/{cod_categoria}/{cod_idioma}")
def obter(cod_categoria: str, cod_idioma: str, db: Session = Depends(get_db)):
    return obter_categoria(db, cod_categoria, cod_idioma)
