from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

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

""""
/app
│
├── main.py
├── routes/
│   ├── __init__.py
│   ├── auth_routes.py
│   └── order_routes.py
├── core/
│   ├── config.py
│   └── security.py
└── models/
"""