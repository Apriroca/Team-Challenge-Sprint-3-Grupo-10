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

# IDs jugadores ## Añadido por ANA
jugador = "Jugador"
maquina = "Maquina"

# damos una semilla para la generación aleatoria
np.random.seed(42)

# mensaje de bienvenida
mensaje = """
==========================================
        ¡BIENVENIDO A HUNDIR LA FLOTA!
==========================================

Prepárate para una batalla naval épica entre
TÚ y la MÁQUINA.

NORMAS DEL JUEGO:
-----------------
1. El tablero es de 10 x 10 casillas.
2. Tú y la máquina tenéis los siguientes barcos,
   colocados ALEATORIAMENTE en vuestros tableros:

      - 4 barcos de 1 casilla
      - 3 barcos de 2 casillas
      - 2 barcos de 3 casillas
      - 1 barco de 4 casillas

3. Empiezas tú. Cada turno introduces una
   coordenada (X, Y) para disparar al tablero enemigo.

4. Si aciertas un barco enemigo, ¡repites turno!
   Si fallas, dispara la máquina.

5. La máquina dispara a coordenadas aleatorias,
   pero si acierta, también repite turno.

6. El juego termina cuando uno de los dos jugadores
   se queda sin barcos... ¡y el otro gana la batalla!

¡Buena suerte, capitana! ⚓🔥
"""
