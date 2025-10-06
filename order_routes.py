from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schamas import PedidoSchema
from models import Pedido

order_router = APIRouter(prefix='/pedidos', tags=['pedidos'])

@order_router.get('/')
async def pedidos():
    """
    Éssa é a rota padrão de pedidos do nosso sistema
    """
    return {'mensagem': 'Você acessou a rota de pedidos.'}


@order_router.post('/pedido')
async def criar_pedido(pedido_schama: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schama.usuario)
    session.add(novo_pedido)
    session.commit()
    return {'mensagem': f'Pedido criado com sucesso. ID do pedido: {novo_pedido.id}'}
