from models import db
from sqlalchemy.orm import sessionmaker



def pegar_sessao():
    session = sessionmaker(bind=db)
    session = session()

    return session