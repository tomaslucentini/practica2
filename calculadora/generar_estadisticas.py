# PUNTO 1. 
def generar_estadisticas(names, goals, goals_avoided, assists):
    estadisticas = []
    for nombre, goles, goles_evitados, asistencias in zip(names.split(', '), goals, goals_avoided, assists):
        jugador = {
            'Nombre': nombre,
            'Goles a favor': goles,
            'Goles evitados': goles_evitados,
            'Asistencias': asistencias
        }
        estadisticas.append(jugador)
    return estadisticas