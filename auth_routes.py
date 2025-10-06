from fastapi import APIRouter, Depends, HTTPException, status
from models import Usuario
from dependencies import pegar_sessao
from config import bcrypt_context
from sqlalchemy.orm import Session

from schamas import UsuarioSchema, LoginSchema


def criar_token(email):
    token = f'fnsnsldf47sd{email}'
    return token


auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def home():
    """
    Éssa é a rota padrão de autenticação do nosso sistema
    """
    return {'mensagem': 'Você acessou a rota padrão de autenticação', 'autenticação': False}

@auth_router.post('/criar_conta')
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        # Já existe um usuário com esse email
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email do usuário já cadastrado')
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {'mesagem': f'Usuário cadastrado com sucesso. {usuario_schema.email}'}


@auth_router.post('/login')
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==login_schema.email).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuário não encontrado.')
    else:
        access_token = criar_token(usuario.id)
        return {
            'access_token': access_token,
            'token_type': 'Bearer'    
        }