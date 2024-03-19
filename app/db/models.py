from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, func
from sqlalchemy.orm import relationship
from db.base import Base




class Produtos(Base):
    __tablename__ = "produtos"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    item = Column('item', String, nullable=False)
    peso = Column('peso', Float)
    numero_caixas = Column('numero_caixas', Integer)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)


class Pagamento(Base):
    __tablename__="pagamentos"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    metodo_pagamento = Column('metodo_pagamento',String,nullable=False)
    valor = Column('valor',Float,nullable=False)
    cnpj_comprador = Column('cnpj_comprador',String,nullable=False)
    id_usuario = Column(Integer, nullable=False)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())

