from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Usuario ,AlarmasRepeticion


engine = create_engine('mysql+mysqlconnector://HJ76u1YF7m:ZL1LDdUYed@remotemysql.com/HJ76u1YF7m')
Session = sessionmaker(bind=engine)
session = Session()


def buscar_alarmas(session):
    alarmas_repeticion = session.query(AlarmasRepeticion).all()
    return alarmas_repeticion

lista_alarmas = buscar_alarmas(session)

for items in lista_alarmas:
        print(items.id)

