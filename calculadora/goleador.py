# PUNTO 2.
def goleador(estadisticas):
    max_goles = max(estadisticas, key=lambda x: x['Goles a favor'])
    return max_goles['Nombre'], max_goles['Goles a favor']
