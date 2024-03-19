from typing import List
from fastapi import APIRouter, Response, Depends, status, Query
from sqlalchemy.orm import Session
from db.database import engine,SessionLocal
from db.models import Usuario as UsuarioModel
from schemas.usuario import Usuarios as UsuarioOutput
from sqlalchemy.orm import Session

from db.base import Base

#cria a tabela
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/usuarios")   

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/addComSchema", status_code=status.HTTP_201_CREATED, description='Adicionar Usuario')
def add_usuario(request:UsuarioOutput, db: Session = Depends(get_db)):
        usuario_on_db = UsuarioModel(**request.dict())
        db.add(usuario_on_db)
        db.commit()
        return usuario_on_db

@router.get("/id/{id}", description="Listar o Usuario pelo número de identificação")
def get_usuario_por_id(id,db: Session = Depends(get_db)):
    usuario_on_db= db.query(UsuarioModel).filter(UsuarioModel.id == id).first()
    return usuario_on_db


@router.get("/listar")
async def get_usuarios(db: Session = Depends(get_db)):
        usuarios= db.query(UsuarioModel).all()
        return usuarios

#validação no código
@router.delete("/{id}", description="Deletar o Usuario pelo id")
def delete_Usuario(id: int, db: Session = Depends(get_db)):


    usuario_on_db = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()
    if usuario_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem Usuario com este id')
    db.delete(usuario_on_db)
    db.commit()
    return f"Banco with id {id} deletado.", Response(status_code=status.HTTP_200_OK)

@router.put('/update/{id}', description='Update Usuario')
def update_Usuario(
    id: int,
    Usuario: UsuarioOutput,
    db: Session = Depends(get_db)
    
    ):
    usuario_on_db = db.query(UsuarioModel).filter_by(id=id).first()
    if usuario_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No Usuario was found with the given id')
        
    usuario_on_db.metodo_Usuario = Usuario.metodo_Usuario
    

    db.add(usuario_on_db)
    db.commit()
    return "ok"