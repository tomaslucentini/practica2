# PUNTO 3.
def jugador_influyente(estadisticas):
    def puntaje(jugador):
        return jugador['Goles a favor'] * 1.5 + jugador['Goles evitados'] * 1.25 + jugador['Asistencias']
    jugador_mas_influyente = max(estadisticas, key=puntaje)
    nombre_mas_influyente = jugador_mas_influyente['Nombre']
    puntaje_mas_influyente = puntaje(jugador_mas_influyente)
    return nombre_mas_influyente, puntaje_mas_influyente
