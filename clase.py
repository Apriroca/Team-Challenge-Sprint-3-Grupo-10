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


#### Codigo ajustado por ANA (con el codigo de antes los barcos solo se pueden poner de manera horizontal. se pueden salir del tablero o se pueden pisar entre ellos)

# 1. Función para generar las coordenadas de los barcos,
# dado una lista de barcos que contenga dos parámetros, 
# el primero la eslora, y el segundo la cantidad de barcos iguales.
# Se tiene en cuenta que no se salga del tablero y que no pise otro barco

    
    def colocar_barcos_aleatorio(self, barcos, dim_tablero):

        lista_coord_ocupadas = []  # En esta lista se guardan todas las casillas ocupadas

        # recorremos todos los barcos que queremos colocar
        for (eslora, cantidad) in barcos.values():
            for i in range(cantidad):

                # se elige la orientacion del barco al azar (True: barco horizontal y False: barco vertical)
                es_horizontal = np.random.choice([True, False])  # random.choice elige al azar True o False
            
                # Intenta colocar el barco (máximo 100 intentos)
                colocado = False  # todavía no hemos colocado el barco
                intentos = 0  # contador de intentos
            
                while not colocado and intentos < 100:  #mientras el barco no esté colocado y no hayamos llegado a los 100 intentos, sigue intentando buscar un sitio para el barco
                
                    if es_horizontal: # Si el barco esta orientado horizontalmente 
                        x = np.random.randint(0, dim_tablero - 1)  # elige una fila al azar entre 0 y la ultima fila (9)
                        y = np.random.randint(0, dim_tablero - eslora)  # Columna donde empieza el barco, asegurándonos de que cabe hacia la derecha

                        # generar coordenadas del barco
                        coords = [] #crea una lista donde guardaremos todas las coordenadas que ocupa el barco.
                        for j in range(eslora):
                            coords.append([x, y + j])

                    # Si el barco esta orientado verticalmente (barco va hacia abajo)
                    else:
                        x = np.random.randint(0, dim_tablero - eslora)  # la fila donde empieza el barco, asegurándonos de que cabe hacia abajo
                        y = np.random.randint(0, dim_tablero - 1)  # Elige cualquier columna (0-9)

                        # generar coordenadas del barco
                        coords = [] #crea una lista donde guardaremos todas las coordenadas que ocupa el barco.
                        for j in range(eslora):
                            coords.append([x + j, y]) 

                    # Comprobar si todas las casillas están libres. Queremos saber si el barco que estamos intentando colocar pisa otro barco. 
                    todas_libres = True # empezamos asumiendo que el barco nuevo no pisa otro barco
                    for c in coords: #miramos cada casilla del barco actual una por una
                        if c in lista_coord_ocupadas: #aqui miramos si las casillas ya estan ocupadas por otro barco
                            todas_libres = False  # si hay una casilla ocupada marcamos que no está libre con el False
                            break  # salimos del bucle, no hace falta seguir comprobando

                    # Si todas las casillas del barco están libres, entonces podemos colocar el barco
                    if todas_libres:
                        for c in coords: #coords contiene las coordenadas del barco
                            lista_coord_ocupadas.append(c)  # añadimos cada casilla del barco a la lista lista_coord_ocupadas, tiene todas las coordenadas de todos los barcos del tablero
                        colocado = True  # Ya está colocado, salir del while
                        # comento el print para que deje de salir por pantalla ahora que sabemos que funciona
                        # print(f"El barco con eslora {eslora} está colocado en: {coords}")

                    intentos += 1  # incrementa contador

                # si después de 100 intentos no se pudo colocar el barco, avisar
                if not colocado:
                    print(f"⚠️ No se pudo colocar el barco de eslora {eslora}")

        return lista_coord_ocupadas
    


    # ------------------------------------------------------------
    # Mostrar tablero de barcos
    # ------------------------------------------------------------
    def mostrar_barcos(self):
        for fila in self.tablero_barcos:
            print(" ".join(fila))
        return