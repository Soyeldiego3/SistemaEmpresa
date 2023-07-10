from BD.conexion import DAO
import BD.funciones as f

def menu():
    print("----- MENÚ -----")
    print("1. Leer registros")
    print("2. Crear registro")
    print("3. Eliminar registro")
    print("4. Actualizar registro")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    bd = DAO()
    if opcion == "1":
        f.listarTabla(bd.leer())
        input("Presiona cualquier tecla para continuar...")
        menu()
    elif opcion == "2":
        datos = f.obtenerdatosbd(bd.pedirDatos())
        bd.crear(datos)
        input("Presiona cualquier tecla para continuar...")
        menu()
    elif opcion == "3":
        tabla = input("Ingrese el nombre de la tabla: ")
        #eliminar(tabla)
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
