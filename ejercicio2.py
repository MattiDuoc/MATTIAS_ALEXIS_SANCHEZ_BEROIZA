opcion = 0
STOCK_MAXIMO = 20
laboratorio = STOCK_MAXIMO
while opcion == 0:
    print('Bienvenida ¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Inves-tigación!')
    print("""
    === MENÚ PRINCIPAL ===
    1.- Equipos disponibles.
    2.- Asignar equipo.
    3.- Liberar equipo.
    4.- Historial de usos.
    5.- Salir.
    """)
    try:
        opcion = int(input('Ingrese una opcion (1-5):\n'))
    except:
        print("Ingresa un entero positivo para continuar.")
    if opcion == "1":
        print(f"Cantidad actual de equipos disponibles {laboratorio}.")
    elif opcion == "2":
        entrada = input("Ingrese la cantiad de equipo a asignar:\n")
        if entrada.isdigit():
            cantidad = int(entrada)
            print("Error; la cantidad a asignar debe de ser mayor a 0.")
        elif  cantidad > laboratorio:

    elif opcion == "3":
    elif opcion == "4":
    elif opcion == "5":