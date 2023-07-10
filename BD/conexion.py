import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root",password="", database="yuri")
        except Error as er:
            print("Error al Conectar: {0}".format(er))
    
    def leer(self):
        if self.con.is_connected():
            try:
                nomtabla = input ("Nombre Tabla: ")

                cursor = self.con.cursor()
                seleccionar = "select * from {0}".format(nomtabla)
                desccolumna = "desc {0}".format(nomtabla)

                cursor.execute(seleccionar)
                listatabla = cursor.fetchall()
                cursor.execute(desccolumna)
                nomcol = cursor.fetchall()

                return (listatabla,nomcol,nomtabla)

            except Error as er:
                print("Error al Conectar: {0}".format(er)) 

    def crear(self,datos):
        if self.con.is_connected():
            try:
                cursor = self.con.cursor()

                query = "insert into {0} values {1}".format(datos[1],(tuple(datos[0]))) #inserta la lista como tupla dentro del sql
                print ("\n" + query + "\n") #muestra como queda la query final para el sql

                try:
                    cursor.execute(query) #ejecuta el sql
                    self.con.commit() #guarda los cambios
                    print("Datos Guardados!")
                except:
                    print("Error al Guardar") 

            except Error as er:
                print("Error al Conectar: {0}".format(er))

    def pedirDatos(self): #para crear
        if self.con.is_connected():
            try:

                nomtabla = input ("Nombre Tabla: ")
                cursor = self.con.cursor()

                desc = "desc {0}".format(nomtabla)
                cursor.execute(desc)
                nomcol = cursor.fetchall()

                try:
                    #crear la nueva id
                    obtener = "select {0} from {1}".format(nomcol[0][0],nomtabla)
                    cursor.execute(obtener)
                    lastid = cursor.fetchall()
                    newid = (int(lastid[-1][0])) #obtiene la ultima id de la tabla

                    datos = [] #lista con los datos ingresados
                    datos.append(newid+1) #enumera la id y la agrega a la lista
                except:
                    print("error")
                
                return (nomcol, datos, nomtabla)

            except Error as er:
                print("Error al Conectar: {0}".format(er))