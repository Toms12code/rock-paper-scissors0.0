def obtener_opcion_usuario():
    while True:
        try:
            opcion = int(input("Elige una opción (1: Piedra, 2: Papel, 3: Tijera): "))
            if opcion in [1, 2, 3]:
                return opcion
            print("Opción inválida. Debes ingresar 1, 2 o 3.")
        except ValueError:
            print("Entrada inválida. Ingresa un número (1, 2 o 3).")
