# ------------------------------------------
# Funciones que usaremos en Hundir la flota
# ------------------------------------------

import numpy as np
import variables


# 1. Función para generar las coordenadas de los barcos,
# dado una lista de barcos que contenga dos parámetros, 
# el primero la eslora, y el segundo la cantidad de barcos iguales.
# Se tiene en cuenta que no se salga del tablero y que no pise otro barco
def generar_barcos_aleatorio(barcos, dim_tablero):

    lista_coord_ocupadas = []

    for (eslora, cantidad) in barcos.values():
        for i in range(cantidad):
            x = np.random.randint(0, dim_tablero)
            y = np.random.randint(0, dim_tablero-eslora)
            
            while [x, y] in lista_coord_ocupadas:
                x = np.random.randint(0, dim_tablero)
                y = np.random.randint(0, dim_tablero-eslora)

            lista_coord_ocupadas.append([x, y])

            for j in range(1,eslora):
                yj = y+j
                lista_coord_ocupadas.append([x, yj])

            print("eslora", eslora, "cantidad", cantidad, lista_coord_ocupadas)

    return lista_coord_ocupadas



# 2. Esta función coloca los barcos en el tablero, 
# dada la lista de coordenadas ocupadas
# y el tablero original
def colocar_barcos(tablero, lista_coord_ocupadas):
    for [x, y] in lista_coord_ocupadas:
       tablero[x, y] = "B"
    print(tablero)
    return tablero



# Función para mostrar el tablero


# Función para disparar

def disparar(tablero, x, y):
    if tablero[x, y] == barco:
        tablero[x, y] = impacto
        print("Tocado")
    elif tablero[x, y] == agua:
        tablero[x, y] = fallo
        print("Agua")
    else:
        print("Ya has disparado aquí")

    return tablero



# recibir disparo aleatorio



