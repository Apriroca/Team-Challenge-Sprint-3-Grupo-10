# --------------------------------------------
#  Funciones para el juego Hundir la flota
# --------------------------------------------


from variables import *
from clase import *

# Esta función coloca los barcos en el tablero, 
# dada la lista de coordenadas ocupadas
# y el tablero original
def colocar_barcos(tablero, lista_coord_ocupadas):
    for [x, y] in lista_coord_ocupadas:
       tablero[x, y] = "B"
    return tablero

# Función para disparar el jugador
def disparo_jugador(tablero, x, y):
    if tablero[x, y] == barco:
        tablero[x, y] = impacto
        print("Tocado")
    elif tablero[x, y] == agua:
        tablero[x, y] = fallo
        print("Agua")
    else:
        print("Ya has disparado aquí")
    return tablero


# Función para disparar de forma aleatoria la máquina
def disparo_maquina(tablero):
    # esta función toma valores aleatorios de x e y
    x = np.random.randint(0,9)
    y = np.random.randint(0,9)
    if tablero[x, y] == barco:
        tablero[x, y] = impacto
        print("Tocado")
    elif tablero[x, y] == agua:
        tablero[x, y] = fallo
        print("Agua")
    else:
        print("Ya has disparado aquí")
    return tablero

# Función para mostrar el tablero de la máquina sin desvelar dónde están los barcos
def mostrar_tablero_maquina_oculto(tablero):
    tablero_oculto = tablero.copy()
    tablero_oculto[tablero_oculto == barco] = desconocido
    tablero_oculto[tablero_oculto == agua] = desconocido
    return tablero_oculto


# Función para saber quedan barcos
def quedan_barcos(tablero):
    for fila in tablero:
        if "B" in fila:   # mientras quede al menos una parte de barco
            return True
    return False