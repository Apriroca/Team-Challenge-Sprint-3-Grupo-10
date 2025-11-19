# --------------------------------------------
#  Clase Tablero para el juego Hundir la flota
# --------------------------------------------


import numpy as np
from variables import *

class Tablero:
    def __init__(self, id_jugador: str):
        self.id_jugador = id_jugador
        self.dimension = dim_tablero
        self.tablero_barcos = np.full((dim_tablero, dim_tablero), agua) # con los barcos propios
        self.tablero_disparos = np.full((dim_tablero, dim_tablero), desconocido) # con los disparos hechos al enemigo
        self.vidas = 0  # total de casillas con barco

# Colocar barcos SIN SALIRSE y SIN SOLAPARSE(cris)
    # ------------------------------------------------------------
    def colocar_barcos(self):
        coords_ocupadas = []

        for (eslora, cantidad) in variables.BARCOS.values():
            for _ in range(cantidad):

                colocado = False
                while not colocado:

                    # orientación aleatoria
                    orientacion = np.random.choice(["H", "V"])

                    if orientacion == "H":
                        x = np.random.randint(0, self.dimension)
                        y = np.random.randint(0, self.dimension - eslora + 1)

                        nuevas = [(x, y + i) for i in range(eslora)]

                    else:  # Vertical
                        x = np.random.randint(0, self.dimension - eslora + 1)
                        y = np.random.randint(0, self.dimension)

                        nuevas = [(x + i, y) for i in range(eslora)]

                    # Comprobar solapamientos
                    if any(coord in coords_ocupadas for coord in nuevas):
                        continue
                    else:
                        coords_ocupadas.extend(nuevas)
                        colocado = True

        # Marcar barcos en tablero
        for (x, y) in coords_ocupadas:
            self.tablero_barcos[x, y] = variables.BARCO
            self.vidas += 1

    # ------------------------------------------------------------
    # Mostrar tablero de barcos
    # ------------------------------------------------------------
    def mostrar_barcos(self):
        for fila in self.tablero_barcos:
            print(" ".join(fila))
        return
    # Recibir disparo del enemigo falta