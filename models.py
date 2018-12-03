from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey,
    String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('mysql+mysqlconnector://root:tsensor@localhost/test')
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(120), index=True, nullable=False)
    nombre = Column(String(120))
    email = Column(String(120))


class AlarmasRepeticion(Base):
    __tablename__ = 'repeticion_alarmas'
    id = Column(Integer, primary_key=True)
    pi_dispositivo = Column(String(120), index=True, nullable=False)
    nombre = Column(String(120))
    email = Column(String(120))

#Base.metadata.create_all(engine)