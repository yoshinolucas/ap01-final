from typing import List
from fastapi import APIRouter, Response, Depends, status, Query
from sqlalchemy.orm import Session
from db.database import engine,SessionLocal
from db.models import Pagamento as PagamentoModel
from schemas.pagamento import Pagamento as PagamentoOutput
from sqlalchemy.orm import Session

from db.base import Base

#cria a tabela
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/pagamentos")   

def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()

#post usando schema
@router.post("/addComSchema", status_code=status.HTTP_201_CREATED, description='Adicionar pagamento')
def add_pagamento(request:PagamentoOutput, db: Session = Depends(get_db)):
        pagamento_on_db = PagamentoModel(**request.dict())
        db.add(pagamento_on_db)
        db.commit()
        return Response(status_code=status.HTTP_201_CREATED)

@router.get("/id/{id}", description="Listar o pagamento pelo número de identificação")
def get_Pagamento(id,db: Session = Depends(get_db)):
    pagamento_on_db= db.query(PagamentoModel).filter(PagamentoModel.id == id).first()
    return pagamento_on_db


@router.get("/listar")
async def get_pagamentos(db: Session = Depends(get_db)):
    Pagamento= db.query(PagamentoModel).all()
    return Pagamento

#validação no código
@router.delete("/{id}", description="Deletar o pagamento pelo id")
def delete_pagamento(id: int, db: Session = Depends(get_db)):


    pagamento_on_db = db.query(PagamentoModel).filter(PagamentoModel.id == id).first()
    if pagamento_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem pagamento com este id')
    db.delete(pagamento_on_db)
    db.commit()
    return f"Banco with id {id} deletado.", Response(status_code=status.HTTP_200_OK)

@router.put('/update/{id}', description='Update pagamento')
def update_pagamento(
    id: int,
    pagamento: PagamentoOutput,
    db: Session = Depends(get_db)
    
    ):
    pagamento_on_db = db.query(PagamentoModel).filter_by(id=id).first()
    if pagamento_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No pagamento was found with the given id')
        
    pagamento_on_db.metodo_pagamento = pagamento.metodo_pagamento
    

    db.add(pagamento_on_db)
    db.commit()
    return "ok"
