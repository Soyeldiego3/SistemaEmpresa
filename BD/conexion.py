import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root",password="", database="yuri")
        except Error as er:
            print("Error al Conectar: {0}".format(er))
    
    def leer(self,nomtabla):
        if self.con.is_connected():
            try:
                cursor = self.con.cursor() #crea el cursor

                #if nomtabla == "trabajador":
                    #seleccionar = "select * from trabajador INNER JOIN cuenta ON trabajador.Usuario_ID=cuenta.Usuario_ID;"
                    #desccolumna = "desc trabajador"
                    #print("a")
                #else:
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

                newdatos = datos[0]
                tablaname = datos[1]

                for q in range(len(tablaname)):
                    titulo = tablaname[q]
                    if titulo == "trabajador":
                        dt = newdatos[q]
                        #print(dt, " Conexion\n")
                        faltan = []
                        for f in range(3):
                            id = newdatos[q][0]
                            faltan.append(id)
                        dt.extend(faltan)
                        #print(dt, "\n")
                        query = "insert into {0} values {1}".format(titulo,(tuple(dt)))
                        print ("\n TRABAJADOR: ", query, "\n")
                    else:
                        query = "insert into {0} values {1}".format(titulo,(tuple(newdatos[q])))
                        #print(tablaname[q] , "\n")
                        #print (tablaname[q], query, "\n") #descomentar para mostrar como queda la query final para el sql

                    try:
                        cursor.execute(query) #ejecuta el sql
                        self.con.commit() #guarda los cambios
                        print("Datos Guardados!")
                    except:
                        print("Error al Guardar. {0}".format(er)) 

            except Error as er:
                print("Error al Conectar: {0}".format(er))

    def pedirDatos(self): #para crear
        if self.con.is_connected():
            try:
                cursor = self.con.cursor()
                nomtabla = ["trabajador", "t_cargas_familiares","t_contactos_emergencia", "departamento", "cuenta"]
                descripciones = []

                for i in range(len(nomtabla)):
                    descquery = "desc {0}".format(nomtabla[i]) 
                    cursor.execute(descquery)
                    descripcion = cursor.fetchall()
                    descripciones.append(descripcion)
                try:
                    #crear la nueva id
                    obtener = "select {0} from {1}".format("T_ID","trabajador")
                    cursor.execute(obtener)
                    lastid = cursor.fetchall()
                    if lastid == "" or lastid == []:
                        newid = 0
                    else:
                        newid = (int(lastid[-1])) #obtiene la ultima id de la tabla
                except:
                    print("error")
                
                return (nomtabla, descripciones, newid)
            except Error as er:
                print("Error al Conectar: {}".format(er))
    
    def tablas(self):
        if self.con.is_connected():
            cursor = self.con.cursor()
                    
            tablesquery = "SHOW TABLES FROM yuri" #muestra todas las tablas de la BD
            cursor.execute(tablesquery)
            nomtablas = cursor.fetchall() #tablas de la BD
            ntablas = ""  #nombre de las tablas(string)
            tablasdisponibles = [] #nombre de las tablas (lista)

            for tablas in range(len(nomtablas)):
                ntablas += ((nomtablas[tablas][0]) + ", ") #agrega el nombre de la tabla a un string
                tablasdisponibles.append(nomtablas[tablas][0]) #agrega el nombre de la tabla a una lista
            return(tablasdisponibles,ntablas)


    def eliminar(self,datos):
        if self.con.is_connected():
            cursor = self.con.cursor()

            nomtabla = datos[0]
            nomcol = datos[1]
            id = datos[2]

            condicion = "{0}={1}".format(str(nomcol),int(id))

            eliminarquery = "DELETE FROM {0} WHERE {1};".format(nomtabla,condicion)
            try:
                print(eliminarquery, "\n")
                cursor.execute(eliminarquery)
                self.con.commit() #Aplicar cambios
                print("Datos Eliminados!")
            except:
                print("Error! verifique que la id ingresada sea valida")
    
    def actualizar(self):
        print("ACTUALIZADOO WAOWAOWAO!")


