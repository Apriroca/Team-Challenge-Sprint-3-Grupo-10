import numpy as np
import variables

class Tablero:
    def __init__(self, id_jugador: str):
        """Inicializa el tablero del jugador"""
        self.id_jugador = id_jugador
        self.dimension = dim_tablero
        self.tablero_barcos = np.full((dim_tablero, dim_tablero), agua) # con los barcos propios
        self.tablero_disparos = np.full((dim_tablero, dim_tablero), desconocido) # con los disparos hechos al enemigo
        self.vidas = 0  # total de casillas con barco

        self.colocar_barcos_iniciales()

    def colocar_barcos_iniciales(self):
        """Coloca los barcos en el tablero de forma fija o aleatoria"""
        for _, (eslora, cantidad) in barcos.items():
            for _ in range(cantidad):
                self.colocar_barco_aleatorio(eslora)
                self.vidas += eslora

    def colocar_barco_aleatorio(self, eslora: int):
        """Coloca un barco de tamaño 'eslora' aleatoriamente en el tablero"""
        colocado = False
        while not colocado:
            orientacion = np.random.choice(ORIENTACIONES)
            x = np.random.randint(0, self.dimension)
            y = np.random.randint(0, self.dimension)

            if self.puede_colocar_barco(x, y, eslora, orientacion):
                self.poner_barco(x, y, eslora, orientacion)
                colocado = True

    def puede_colocar_barco(self, x, y, eslora, orientacion):
        """Comprueba si el barco cabe sin salirse ni superponerse"""
        dx, dy = 0, 0
        if orientacion == "N": dx = -1
        elif orientacion == "S": dx = 1
        elif orientacion == "E": dy = 1
        elif orientacion == "O": dy = -1

        for i in range(eslora):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < self.dimension and 0 <= ny < self.dimension):
                return False
            if self.tablero_barcos[nx, ny] == barco:
                return False
        return True

    def poner_barco(self, x, y, eslora, orientacion):
        """Coloca el barco en el tablero"""
        dx, dy = 0, 0
        if orientacion == "N": dx = -1
        elif orientacion == "S": dx = 1
        elif orientacion == "E": dy = 1
        elif orientacion == "O": dy = -1

        for i in range(eslora):
            nx, ny = x + i * dx, y + i * dy
            self.tablero_barcos[nx, ny] = barco

    def recibir_disparo(self, x, y):
        """Procesa un disparo en las coordenadas dadas"""
        if self.tablero_barcos[x, y] == barco:
            self.tablero_barcos[x, y] = impacto
            self.vidas -= 1
            return True  # impacto
        elif self.tablero_barcos[x, y] == agua:
            self.tablero_barcos[x, y] = fallo
            return False  # agua
        else:
            return False  # ya había disparo previo

    def disparar_a(self, tablero_enemigo, x, y):
        """Realiza un disparo sobre el tablero enemigo"""
        impacto = tablero_enemigo.recibir_disparo(x, y)
        self.tablero_disparos[x, y] = impacto if impacto else fallo
        return impacto

    def mostrar_tablero(self, mostrar_barcos=False):
        """Imprime el tablero en pantalla"""
        print(f"\n🧭 Tablero de {self.id_jugador}")
        tablero = self.tablero_barcos if mostrar_barcos else self.tablero_disparos
        for fila in tablero:
            print(" ".join(fila))

    def esta_derrotado(self):
        """Devuelve True si el jugador no tiene barcos"""
        return self.vidas <= 0
