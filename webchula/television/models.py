from django.db import models
import oracledb

# Create your models here.
class Serie:
    def __init__(self):
        self.idSerie = 0
        self.nombre = ""
        self.imagen = ""
        self.anyo = 0

class Personaje:
    def __init__(self):
        self.idPersonaje = 0
        self.nombre = ""
        self.imagen = ""
        self.idSerie = 0

class ServiceSeries:
    def __init__(self):
        self.connection = oracledb.connect(user="system",
                                           password="oracle",
                                           dsn="localhost/freepdb1")
    
    def getSeries(self):
        sql = "select * from SERIES"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        listaSeries = []
        for row in cursor:
            serie = Serie()
            serie.idSerie = row[0]
            serie.nombre = row[1]
            serie.imagen = row[2]
            serie.anyo = row[3]
            listaSeries.append(serie)
        cursor.close()
        return listaSeries

    def getPersonajesSerie(self, idSerie,):
        sql = "select * from PERSONAJES where IDSERIE=:idserie"
        cursor = self.connection.cursor()
        cursor.execute(sql, (idSerie,))
        listaPersonajes = []
        for row in cursor:
            p = Personaje()
            p.idPersonaje = row[0]
            p.nombre = row[1]
            p.imagen = row[2]
            p.idSerie = row[3]
            listaPersonajes.append(p)
        cursor.close()
        return listaPersonajes

    def insertarPersonaje(self, nombre, imagen, idserie):
        sql = "insert into PERSONAJES (IDPERSONAJE, PERSONAJE, IMAGEN, IDSERIE) values ((SELECT max(IDPERSONAJE)+1 FROM PERSONAJE), :nombre, :imagen, :idserie)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, imagen, idserie,))
        self.connection.commit()
        cursor.close()







