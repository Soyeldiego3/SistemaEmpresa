
def listarTabla(leertabla):

    tabla = leertabla[0]
    desc = leertabla[1]
    nomtabla = leertabla[2]

    # mostrar datos
    print('\n Tabla: {0} \n'.format(nomtabla))

    lista = "" #se puede cambiar a una lista deverdad #esta como string por cosas de la vida

    if nomtabla == "trabajador":
        cantcolumn = (len(desc)-3) #se le resta las llaver foraneas
    else:
        cantcolumn = (len(desc))

    for row in tabla:
        for num in range(cantcolumn):
            lista += (str(desc[num][0]) + " = " + str(row[num]) + " | ") #crea la estructura de la tabla con los datos de esta
        lista += "\n"

    return (lista)

import bcrypt
def encriptar(clave):
    bytes = clave.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes,salt)
    clave = str(hash)
    return clave

def obtenerdatosbd(pedirDatos):

    nomtabla = pedirDatos[0]
    descripciones = pedirDatos[1] 
    newid = pedirDatos[2]

    #lista de Datos de todas las tablas con la ID Pregenerada
    datostrabajador = [newid]
    datoscargas = [newid]
    datoscontactos = [newid]
    datosdepartamento = [newid]
    datoscuenta = [newid]  

    for a in range(len(descripciones)):
        tabla = nomtabla[a]
        nomcol = descripciones[a] #trabajador

        print("\n", tabla.upper(), ": \n") #imprime el nombre de la tabla en la que se esta
        if tabla == "trabajador":
            trabajadorli = ["Rut","Nombre", "Sexo", "Direccion", "Telefono", "FechaDeIngreso"]
            for d in range(len(nomcol)-5): #para no mostrar id y las fk se quitan 5
                if trabajadorli[d] == "Rut" or trabajadorli[d] == "Telefono":
                    numeric = False
                    while numeric != True:
                        dato = input((trabajadorli[d]) + (" = "))
                        if dato.isnumeric() == True:
                            numeric = True
                        else:
                            print("> Debe de ingresar solo Numeros <")
                else:
                    dato = input((trabajadorli[d]) + (" = "))
                datostrabajador.append(dato)

        elif tabla == "t_cargas_familiares":
            cargasli = ["Rut","Nombre","Edad","Parentesco"]
            for d in range(len(nomcol)-1): #para no mostrar la id se le resta 1
                if cargasli[d] == "Rut" or cargasli[d] == "Edad":
                    numeric = False
                    while numeric != True:
                        dato = input((cargasli[d])+(" = "))
                        if dato.isnumeric() == True:
                            numeric = True
                        else:
                            print("> Debe de ingresar solo Numeros <")
                else:
                    dato = input((cargasli[d])+(" = "))
                datoscargas.append(dato)

        elif tabla == "t_contactos_emergencia":
            contactosli = ["Rut","Nombre","Telefono","Relación"]
            for d in range(len(nomcol)-1):
                if contactosli[d] == "Rut" or contactosli[d] == "Telefono":
                    numeric = False
                    while numeric != True:
                        dato = input((contactosli[d])+(" = "))
                        if dato.isnumeric() == True:
                            numeric = True
                        else:
                            print("> Debe de ingresar solo Numeros <")
                else:           
                    dato = input((contactosli[d])+(" = "))
                datoscontactos.append(dato)

        elif tabla == "departamento":
            depali = ["Codigo", "Nombre Departamento", "Cargo"]
            for d in range(len(nomcol)-1):
                if depali[d] == "Codigo":
                    numeric = False
                    while numeric != True:
                        dato = input((depali[d])+(" = "))
                        if dato.isnumeric() == True:
                            numeric = True
                        else:
                            print("> Debe de ingresar solo Numeros <")
                else:
                    dato = input((depali[d])+(" = "))
                datosdepartamento.append(dato)

        elif tabla == "cuenta":
            cuentali = ["Email", "Contraseña"]
            for d in range(len(nomcol)-1):
                dato = input((cuentali[d])+(" = "))
                if cuentali[d] == "Contraseña":
                    dato = encriptar(dato)
                datoscuenta.append(dato)
        else:
            print("\n", tabla, "error: \n")
    
    datos = [datostrabajador,datoscargas,datoscontactos,datosdepartamento,datoscuenta]
    return (datos, nomtabla)

def obtenertabla(tablas):
    print("\nTablas Disponibles: 1-Cuenta, 2-Departamento, 3-Cargas Familiares, 4-Contactos de Emergencia, 5-Trabajador") #tablas[1] = string con el nombre de las tablas
    print("Ingrese el numero de la tabla desde el: 1 al {} \n".format(len(tablas[0])))
    existe = False
    numeric = False

    while existe != True: #verifica que la tabla exista
        while numeric != True:
            numtabla = input ("Tabla: ")
            if numtabla.isnumeric() == True:
                numtabla = int(numtabla)
                if numtabla == 1:
                    nomtabla = "cuenta"
                    numeric = True
                elif numtabla == 2:
                    nomtabla = "departamento"
                    numeric = True
                elif numtabla == 3:
                    nomtabla = "t_cargas_familiares"
                    numeric = True
                elif numtabla == 4:
                    nomtabla = "t_contactos_emergencia"
                    numeric = True
                elif numtabla == 5:
                    nomtabla = "trabajador"
                    numeric = True
                else:
                    numtabla = "No"
            else:
                print("Debes de ingresar un Numero Valido! \n")

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
