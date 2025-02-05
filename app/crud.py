from sqlalchemy.orm import Session
from app.models.categoria import Categoria
from app.models.categoria_lang import CategoriaLang

def criar_categoria(db: Session, cod_categoria: str, descricao: str, cod_idioma: str):
    nova_categoria = Categoria(cod_categoria=cod_categoria)
    traducao = CategoriaLang(cod_categoria=cod_categoria, cod_idioma=cod_idioma, descricao=descricao)

    db.add(nova_categoria)
    db.add(traducao)
    db.commit()
    return {"mensagem": "Categoria criada com sucesso!"}

def obter_categoria(db: Session, cod_categoria: str, cod_idioma: str):
    traducao = db.query(CategoriaLang).filter(
        CategoriaLang.cod_categoria == cod_categoria,
        CategoriaLang.cod_idioma == cod_idioma
    ).first()
    
    return {"descricao": traducao.descricao if traducao else "Tradução não encontrada"}
