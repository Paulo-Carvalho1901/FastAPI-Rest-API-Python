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