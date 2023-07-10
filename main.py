from CRUD import crear, leer, eliminar, actualizar

def menu():
    print("----- MENÚ -----")
    print("1. Leer registros")
    print("2. Crear registro")
    print("3. Eliminar registro")
    print("4. Actualizar registro")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tabla = input("Ingrese el nombre de la tabla: ")
        leer(tabla)
        menu()
    elif opcion == "2":
        tabla = input("Ingrese el nombre de la tabla: ")
        crear(tabla)
        menu()
    elif opcion == "3":
        tabla = input("Ingrese el nombre de la tabla: ")
        eliminar(tabla)
        menu()
    elif opcion == "4":
        tabla = input("Ingrese el nombre de la tabla: ")
        actualizar(tabla)
        menu()
    elif opcion == "5":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu()

# Ejecutar el menú al iniciar el programa
menu()
