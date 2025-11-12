# --------------------------------------------
#  Clase Tablero para el juego Hundir la flota
# --------------------------------------------


import numpy as np
import variables

class Tablero:
    def __init__(self, id_jugador: str):
        self.id_jugador = id_jugador
        self.dimension = dim_tablero
        self.tablero_barcos = np.full((dim_tablero, dim_tablero), agua) # con los barcos propios
        self.tablero_disparos = np.full((dim_tablero, dim_tablero), desconocido) # con los disparos hechos al enemigo
        self.vidas = 0  # total de casillas con barco
