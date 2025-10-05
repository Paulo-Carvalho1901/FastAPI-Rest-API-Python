from fastapi import APIRouter, Depends, HTTPException, status
from models import Usuario
from dependencies import pegar_sessao
from config import bcrypt_context

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def home():
    """
    Éssa é a rota padrão de autenticação do nosso sistema
    """
    return {'mensagem': 'Você acessou a rota padrão de autenticação', 'autenticação': False}

@auth_router.post('/criar_conta')
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        # Já existe um usuário com esse email
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email do usuário já cadastrado')
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {'mesagem': f'Usuário cadastrado com sucesso. {email}'}
