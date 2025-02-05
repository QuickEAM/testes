from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CategoriaLang(Base):
    __tablename__ = "tb_categoria_lang"

    cod_categoria = Column(String(50), ForeignKey("tb_categoria.cod_categoria"), primary_key=True)
    cod_idioma = Column(String(2), primary_key=True)
    descricao = Column(String(255), nullable=False)

    categoria = relationship("Categoria", back_populates="traducoes")
