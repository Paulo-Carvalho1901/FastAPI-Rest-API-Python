from fastapi import APIRouter

from models import Usuario, db

from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def autenticar():
    """
    Éssa é a rota padrão de autenticação do nosso sistema
    """
    return {'mensagem': 'Você acessou a rota padrão de autenticação', 'autenticação': False}

@auth_router.post('/criar_conta')
async def criar_conta(email: str, senha: str, nome: str):
    session = sessionmaker(bind=db)
    session = session()
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        # Já existe um usuário com esse email
        return {'mensagem': 'Já existe um usuário com esse email.'}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {'mesagem': 'Usuário cadastrado com sucesso.'}
