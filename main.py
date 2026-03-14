import random
import obtenerOpcionUsuario
import obtenerNombre
import constantes
import resultadoRonda


def obtener_opcion_usuario():
 return obtenerOpcionUsuario.obtener_opcion_usuario()


def obtener_nombre_opcion(opcion):
    return obtenerNombre.obtener_nombre_opcion(opcion)


def resultado_ronda(opcion_usuario, opcion_pc):
    return resultadoRonda.resultado_ronda(opcion_usuario,opcion_pc)

def main():
    vidas_usuario = constantes.VIDAS_INICIALES
    vidas_pc = constantes.VIDAS_INICIALES
    
 
    print("=== JUEGO PIEDRA, PAPEL O TIJERA ===")
    print("Empiezan con 5 vidas cada uno. ¡Pierde una vida quien pierda la ronda!\n")

    while vidas_usuario > 0 and vidas_pc > 0:
        print(f"Vidas -> Usuario: {vidas_usuario} | PC: {vidas_pc}")

        opcion_usuario = obtener_opcion_usuario()
        opcion_pc = random.randint(1, 3)

        nombre_usuario = obtener_nombre_opcion(opcion_usuario)
        nombre_pc = obtener_nombre_opcion(opcion_pc)

        print(f"Tú elegiste: {nombre_usuario}")
        print(f"La PC eligió: {nombre_pc}")

        ganador = resultado_ronda(opcion_usuario, opcion_pc)

        if ganador == "empate":
            print("Resultado de la ronda: ¡Empate!\n")
        elif ganador == "usuario":
            vidas_pc -= 1
            print("Resultado de la ronda: ¡Ganaste esta ronda!\n")
        else:
            vidas_usuario -= 1
            print("Resultado de la ronda: La PC gana esta ronda.\n")

    print("=== FIN DEL JUEGO ===")
    if vidas_usuario > 0:
        print("¡Felicidades! Ganaste el juego.")
    else:
        print("La PC ganó el juego. ¡Inténtalo de nuevo!")


if __name__ == "__main__":
    main()