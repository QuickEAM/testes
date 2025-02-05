from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Categoria(Base):
    __tablename__ = "tb_categoria"

    cod_categoria = Column(String(50), primary_key=True)
    cod_categoria_pai = Column(String(50), ForeignKey("tb_categoria.cod_categoria"), nullable=True)

    subcategorias = relationship("Categoria", backref="categoria_pai", remote_side=[cod_categoria])
    traducoes = relationship("CategoriaLang", back_populates="categoria", cascade="all, delete-orphan")