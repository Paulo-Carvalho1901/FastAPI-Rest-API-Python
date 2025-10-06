from pydantic import BaseModel, EmailStr
from typing import Optional


class UsuarioSchema(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_atrribute = True


class PedidoSchema(BaseModel):
    usuario: int

    class config:
        from_atrribute =True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class config:
        from_atrribute = True
