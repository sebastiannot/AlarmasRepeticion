# -- coding: utf-8 --

from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Usuario

# conexion
engine = create_engine('mysql+mysqlconnector://root:pass@localhost/bd')
# sesion
Session = sessionmaker(bind=engine)
session = Session()


def buscar_alarmas(session):
    alarmas_repeticion = session.query(Usuario).filter(Usuario.id==1).first()
    pass


# insertamos autores
#autor_1 = Autor('Patrick Rothfuss')
#autor_2 = Autor('Fred Saberhagen')

#lista_autores = (autor_1, autor_2)
#session.add_all(lista_autores)
#session.commit()

# insertamos etiquetas
#etiqueta_1 = Etiqueta('aventuras')
#session.add(etiqueta_1)

# insertamos libros
#libro_1 = Libro('El nombre del fuego', date(2009, 5, 30), '978-8401337208')
#libro_1.etiquetas.append(etiqueta_1)
#libro_1.autores.append(autor_1)


#session.add(libro_1)
#session.commit()

# realizando una consulta
libro = session.query(Usuario).filter(Usuario.id==1).first()
print libro.nombre

# alterando uno de los atributos
#libro.titulo = 'El nombre del viento'
#session.commit()

#print libro