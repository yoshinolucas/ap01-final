from pydantic import BaseModel
from pydantic import validator
import re

class Pagamento(BaseModel):
    id:int
    metodo_pagamento: str
    valor: float
    cnpj_comprador: str
    id_usuario: int

    @validator('cnpj_comprador')
    def validate_cnpj_comprador(cls, value):
        if not re.match(r"\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}", value):
            raise ValueError('Invalid CNPJ')
        return value
    
    @validator('metodo_pagamento')
    def validate_metodo(cls,value):
        if value != 'Cartão' or value != 'Dinheiro':
            raise ValueError('Método Inválido')
        return value



