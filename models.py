from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey,
    String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(120), index=True, nullable=False)
    nombre = Column(String(120))
    email = Column(String(120))
    usuario_local = relationship("UsuarioLocal",backref="usuario")

class UsuarioLocal(Base):
    __tablename__ = 'usuarios_locales'
    id = Column(Integer, primary_key=True)
    elementos_id = Column(Integer)
    usuario_alarma = relationship("AlarmasRepeticion",backref="usuario_local")
    usuario_id = Column(Integer,ForeignKey('usuarios.id'))
    
class AlarmasRepeticion(Base):
    __tablename__ = 'repeticion_alarmas'
    id_repeticion = Column(Integer, primary_key=True)
    pi_dispositivo = Column(String(120), index=True, nullable=False)
    diferencia = Column(Integer)
    pi_temp = Column(Integer)
    pi_fecha = Column(Integer)
    repeticion = Column(Integer)
    tipo_medicion = Column(String(120))
    fecha = Column(Date)
    cont_repeticion = Column(Integer)
    valor_min = Column(Integer)
    valor_max = Column(Integer)
    id_usuario_local = Column(Integer,ForeignKey('usuarios_locales.id'))
    
class RefrigeracionDatos(Base):
    __tablename__ = 'refrigeracion_datos'
    id = Column(Integer, primary_key=True)
    codigo_sensor = Column(String(120), index=True, nullable=False)
    simcard = Column(String(120))
    valor = Column(Integer)
    pi_fecha = Column(Date)
    fecha = Column(Date)
    valido = Column(Integer)
   
class Sensor(Base):
    __tablename__ = 'sensores'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(120))
    estado = Column(Integer)
    variable_id = Column(Integer)

class SensorAsignacion(Base):
    __tablename__ = 'sensores_asignacion'
    id = Column(Integer,primary_key=True)
    fecha_reg = Column(Date)
    fecha_fin = Column(Date)
    vmin = Column(Integer)
    vmax = Column(Integer)
