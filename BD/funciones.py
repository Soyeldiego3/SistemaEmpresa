
def listarTabla(leertabla):

    tabla = leertabla[0]
    desc = leertabla[1]
    nomtabla = leertabla[2]

    print(desc, "\n")
    # mostrar datos
    print('\n Tabla: {0} \n'.format(nomtabla))

    lista = "" #se puede cambiar a una lista deverdad #esta como string por cosas de la vida

    #if nomtabla == "trabajador":
    #    foraneas = 3
    #    cantcolumn = (len(desc)) - foraneas
    #else:
    cantcolumn = (len(desc))

    for row in tabla:
        for num in range(cantcolumn):
            lista += (str(desc[num][0]) + " = " + str(row[num]) + " | ") #crea la estructura de la tabla con los datos de esta
        lista += "\n"

    return (lista)

def obtenerdatosbd(pedirDatos):

    nomtabla = pedirDatos[0]
    descripciones = pedirDatos[1] 
    newid = pedirDatos[2]

    datostrabajador = [newid]
    datoscargas = [newid]
    datoscontactos = [newid]
    datosdepartamento = [newid]
    datoscuenta = [newid]  

    #for t in range(len(nomtabla)): #ARREGLAR ESTO AQUI AQUI AQUI 👇👇
        #tabla = nomtabla[t] #trabajador = 0
        #print(tabla, " AQUI\n")
    for a in range(len(descripciones)):
        tabla = nomtabla[a]
        #print(tabla, " AQUI\n")
        nomcol = descripciones[a] #trabajador
        #print(nomcol, "\n")
        #print(len(nomcol), "\n")
        print("\n", tabla.upper(), ": \n")
        if tabla == "trabajador":
            for d in range(len(nomcol)-4): #-4 para descontar id y las fk
                d += 1 #para saltar la id
                dato = input(((str(nomcol[d][0]))+(" = ")))
                print("\n")
                datostrabajador.append(dato)
        elif tabla == "t_cargas_familiares":
            for d in range(len(nomcol)-1):
                d += 1
                dato = input((str(nomcol[d][0]))+(" = "))
                #print(tabla, "\n")
                print("\n")
                datoscargas.append(dato)
        elif tabla == "t_contactos_emergencia":
            for d in range(len(nomcol)-1):
                d += 1
                dato = input(str(nomcol[d][0])+(" = "))
                #print(tabla, "\n")
                print("\n")
                datoscontactos.append(dato)
        elif tabla == "departamento":
            for d in range(len(nomcol)-1):
                d += 1
                dato = input(str(nomcol[d][0])+(" = "))
                #print(tabla, "\n")
                print("\n")
                datosdepartamento.append(dato)
        elif tabla == "cuenta":
            for d in range(len(nomcol)-1):
                d += 1
                dato = input(str(nomcol[d][0])+(" = "))
                #print(tabla, "\n")
                print("\n")
                datoscuenta.append(dato)
        else:
            print(tabla, "error\n")
            #print("\n\m ¡¡¡ALGO SALIO MAL!!! \n\n")
    
    datos = [datostrabajador,datoscargas,datoscontactos,datosdepartamento,datoscuenta]
    #print(datos, "\n")
    #print(datos[0], "\n")
    return (datos, nomtabla)

def obtenertabla(tablas):
    print("tablas Disponibles: ", tablas[1]) #tablas[1] = string con el nombre de las tablas
    existe = False
    while existe != True: #verifica que la tabla exista
        nomtabla = input ("Nombre Tabla: ")
        if nomtabla in tablas[0]:  #tablas[0] = lista con los nombres de las tablas
            existe = True
    return (nomtabla)

def obtenereliminar(leertabla):
    desc = leertabla[1]

    nomtabla = leertabla[2]
    print(nomtabla, "\n")

    tablaid = desc[0][0]
    id = input("ingrese {}: ".format(tablaid))

    return (nomtabla, tablaid, id)
