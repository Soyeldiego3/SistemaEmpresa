import mysql.connector
from mysql.connector import Error

# create connection object
try:
    con = mysql.connector.connect(host="localhost", user="root",password="", database="yuri")
except Error as er:
    print("Error al Conectar: {0}".format(er))

def leer(tabla): #ToDo: ademas de tabla pida condiciones para filtrar o buscar con los "where" ademas de pedir la cantidad de datos que se muestran en pantalla tipo "5 primeros"
    cursor = con.cursor()

    query = "select * from {0}".format(tabla) #sentencia sql
    query2 = "desc {0}".format(tabla) #obtiene la descripcion de las columnas de forma que 'desc[0][0]' la salida es el nombre de la primera columna

    cursor.execute(query)
    table = cursor.fetchall()
    cursor.execute(query2)
    desc = cursor.fetchall()

    # mostrar datos
    print('\n Tabla: \n')

    lista = "" #se puede cambiar a una lista deverdad #esta como string por cosas de la vida
    for row in table:
        for num in range(len(desc)):
            lista += (str(desc[num][0]) + " = " + str(row[num]) + " | ") #crea la estructura de la tabla con los datos de esta
        lista += "\n"

    print(lista)

    # closing cursor connection
    cursor.close()
    # closing connection object
    con.close() #cerrar conexion con bd

def crear():
    cursor = con.cursor()
    tabla = input("nombre tabla = ")

    queryy = "desc {0}".format(tabla) #sentencia sql
    cursor.execute(queryy)
    nomcol = cursor.fetchall()

    #crear la nueva id
    obtener = "select {0} from {1}".format(nomcol[0][0],tabla)
    cursor.execute(obtener)
    lastid = cursor.fetchall()
    newid = (int(lastid[-1][0])) #obtiene la ultima id de la tabla

    datos = []
    datos.append(newid+1) #enumera la id y la agrega a la lista

    for ncolumn in (range(len(nomcol)-1)):
        a = input(str(nomcol[ncolumn+1][0])+(" = "))
        datos.append(a)
        print(datos) #muestra como va quedando la lista

    query = "insert into {0} values {1}".format(tabla,(tuple(datos))) #inserta la lista como tupla dentro del sql
    print (query) #muestra como queda la query final para el sql

    try:
        cursor.execute(query) #ejecuta el sql
        con.commit() #guarda los cambios
        print("Datos Guardados!")
    except:
        print("Error") 

    # closing cursor connection
    cursor.close()
    # closing connection object
    con.close() #cerrar conexion con bd

def eliminar():
    cursor = con.cursor()
    tabla = input("nombre tabla = ")
    cualid = input("ingrese id/rut "+tabla+ " = ")
    print(cualid)
    queryy = "desc {0}".format(tabla)
    cursor.execute(queryy)
    nomcol = cursor.fetchall() #obtener nombre de las columnas

    condicion = (str(nomcol[0][0]) + "=" + (cualid))

    query = "DELETE FROM {0} WHERE {1};".format(tabla,condicion)
    print(query)
    cursor.execute(query)
    
    try:
        cursor.execute(query)
        con.commit() #Guardar datos/Aplicar cambios
        print("Datos Eliminados!")
    except:
        print("Error") 

def actualizar():
    cursor = con.cursor()
    tabla = input("nombre tabla = ")
    cualid = input("ingrese id/rut "+tabla+ " = ")
    print(cualid)
    queryy = "desc {0}".format(tabla)
    cursor.execute(queryy)
    nomcol = cursor.fetchall() #obtener nombre de las columnas

    condicion = (str(nomcol[0][0]) + "=" + (cualid))

    #ToDo: mostrar campos disponibles, preguntar cuantos valores se van a actaulizar y poder actulizarlos de una tipo *Especificar las condiciones de la actualización


#crear()
#leer("cuenta")
#actualizar()
#eliminar()
