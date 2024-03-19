from pydantic import BaseModel

class Usuarios(BaseModel):
    id:int
    username: str
    password: str


