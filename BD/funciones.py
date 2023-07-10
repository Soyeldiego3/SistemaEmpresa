
def listarTabla(leertabla):

    tabla = leertabla[0]
    desc = leertabla[1]
    nomtabla = leertabla[2]

    # mostrar datos
    print('\n Tabla: {0} \n'.format(nomtabla))

    lista = "" #se puede cambiar a una lista deverdad #esta como string por cosas de la vida
    for row in tabla:
        for num in range(len(desc)):
            lista += (str(desc[num][0]) + " = " + str(row[num]) + " | ") #crea la estructura de la tabla con los datos de esta
        lista += "\n"

    print(lista)

def obtenerdatosbd(pedirDatos):

    nomcol  = pedirDatos[0]
    datos = pedirDatos[1]
    nomtabla = pedirDatos[2]

    for ncolumn in (range(len(nomcol)-1)): #pide los datos
        a = input(str(nomcol[ncolumn+1][0])+(" = "))
        datos.append(a)

    return (datos, nomtabla)