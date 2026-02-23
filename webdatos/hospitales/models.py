from django.db import models
import oracledb

# Create your models here.
class Departamento:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.localidad = ""

class ServiceDepartamentos:
    def __init__(self):
        self.conection = oracledb.connect(user="system", 
                                          password="oracle", 
                                          dsn="localhost/freepdb1")
        
    def getDepartamentos(self):
        sql = "select * from DEPT"
        cursor = self.conection.cursor()
        cursor.execute(sql)
        listaDepartamentos = []
        for row in cursor:
            dept = Departamento()
            dept.id = row[0]
            dept.nombre = row[1]
            dept.localidad = row[2]
            listaDepartamentos.append(dept)
        cursor.close()
        return listaDepartamentos

    def insertarDepartamento(self, id, nom, loc):
        sql = "insert into DEPT values (:id, :nombre, :loc)"
        cursor = self.conection.cursor()
        cursor.execute(sql, (id, nom, loc,))
        self.conection.commit()
        cursor.close()

    def actualizarDepartamento(self, id, nom, loc):
        sql = "update DEPT set DNOMBRE=:nom, LOC=:loc WHERE DEPT_NO=:id"
        cursor = self.conection.cursor()
        cursor.execute(sql, (nom, loc, id,))
        self.conection.commit()
        cursor.close()
    
    def buscarDepartamento(self, id):
        sql = "select * from DEPT where DEPT_NO=:id"
        cursor = self.conection.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        dept = Departamento()
        dept.id = row[0]
        dept.nombre = row[1]
        dept.localidad = row[2]
        cursor.close()
        return dept
    


