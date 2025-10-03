from fastapi import FastAPI


app = FastAPI()

from auth_routers import auth_router
from order_routers import order_router

app.include_router(auth_router)
app.include_router(order_router)

# Para rodar nosso código, rodar no terminal - uvicorn main:app --reload

# endpoint:
# /ordens

# REST APIs
# GET -> LEITURA/PEGAR
# POST -> ENVIAR/CRIAR
# PUT/PET -> EDIÇÃO
# DELETE -> DELETAR
