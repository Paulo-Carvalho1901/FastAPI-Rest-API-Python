from fastapi import FastAPI


app = FastAPI()

from auth_routers import auth_router
from order_routers import order_router

app.include_router(auth_router)
app.include_router(order_router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)


# Para rodar nosso código, rodar no terminal - uvicorn main:app --reload

# endpoint:
# /ordens

# REST APIs
# GET -> LEITURA/PEGAR
# POST -> ENVIAR/CRIAR
# PUT/PET -> EDIÇÃO
# DELETE -> DELETAR

# codigo alembic para migraçãpo de banco de dados
# alembic revision --autogenerate -m "initial migration"
# alembic upgrade head   