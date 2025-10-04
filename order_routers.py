from fastapi import APIRouter

order_router = APIRouter(prefix='/pedidos', tags=['pedidos'])

@order_router.get('/')
async def pedidos():
    """
    Éssa é a rota padrão de pedidos do nosso sistema
    """
    return {'mensagem': 'Você acessou a rota de pedidos.'}