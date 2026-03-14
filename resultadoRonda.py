def resultado_ronda(opcion_usuario, opcion_pc):
    if opcion_usuario == opcion_pc:
        return "empate"

    if (
        (opcion_usuario == 1 and opcion_pc == 3)
        or (opcion_usuario == 2 and opcion_pc == 1)
        or (opcion_usuario == 3 and opcion_pc == 2)
    ):
        return "usuario"

    return "pc"
