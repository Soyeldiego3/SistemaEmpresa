from BD.conexion import DAO
import BD.funciones as f

def menu():
    print("----- MENÚ -----")
    print("1. Listar Trabajadores")
    print("2. Crear Trabajador")
    print("3. Eliminar registro")
    print("4. Actualizar registro")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    bd = DAO()
    if opcion == "1":
        #listar
        tabla = f.obtenertabla(bd.tablas())
        listado = f.listarTabla(bd.leer(tabla)) #tabla se puede cambiar por el nombre directo
        print(listado)
        input("Presiona Enter para continuar...")
        menu()
    elif opcion == "2":
        #crear
        #tabla = f.obtenertabla(bd.tablas())
        datos = f.obtenerdatosbd(bd.pedirDatos())
        bd.crear(datos)
        input("Presiona Enter para continuar...")
        menu()
    elif opcion == "3":
        #Eliminar
        tabla = f.obtenertabla(bd.tablas())
        datos = f.obtenereliminar(bd.leer(tabla))
        bd.eliminar(datos)
        input("Presiona Enter para continuar...")
        menu()
    elif opcion == "4":
        tabla = input("Ingrese el nombre de la tabla: ")
        #actualizar(tabla)
        menu()
    elif opcion == "5":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu()

# Ejecutar el menú al iniciar el programa
menu()
