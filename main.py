from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Usuario,UsuarioLocal,SensorAsignacion,Sensor,AlarmasRepeticion
from pprint import pprint
import time,datetime

engine = create_engine('mysql+mysqlconnector://root:pass@localhost/bd')

Session = sessionmaker(bind=engine)
session = Session()

def main():
  usuario = session.query(Usuario).filter(Usuario.login=='csalinas').first()
  print usuario.login
  
  #alarma = session.query(AlarmasRepeticion).filter(AlarmasRepeticion.id_usuario_local==1).first()
  #print(alarma.usuario_local.usuario.login)
  
 
if __name__== "__main__":
  main()

