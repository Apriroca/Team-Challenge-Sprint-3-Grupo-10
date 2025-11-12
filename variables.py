# ----------------------------------------
# Constantes para el juego Hundir la flota
# ----------------------------------------

import numpy as np

# Dimensión del tablero
dim_tablero = 10

# definimos los barcos
barcos = {
    "barco1": (1, 4), # siendo el primer número la eslora y el segundo número la cantidad de barcos
    "barco2": (2, 3),
    "barco3": (3, 2),
    "barco4": (4, 1)
}

# definimos los símbolos para el tablero
agua = "~"
barco = "B"
impacto = "X"
fallo = "O"
desconocido = "." # para el tablero del enemigo donde aun no se ha disparado

# damos una semilla para la generación aleatoria
np.random.seed(42)

