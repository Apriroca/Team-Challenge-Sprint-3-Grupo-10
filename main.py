# --------------------------------------------
#  Archivo principal main.py
# --------------------------------------------

# Hago las llamadas a los otros archivos
from variables import *
from clase import *
from funciones import *

# 0. Mensaje de bienvenida
print(mensaje)

# 1. gereno tablero vacío
t = tablero("Jugador")
tablero_jugador = t.tablero_barcos
t_m = tablero("Máquina")
tablero_maquina = t_m.tablero_barcos

# 2. genero la lista de coordenadas de barcos
lista_coord_barcos_jugador = t.colocar_barcos_aleatorio(barcos, dim_tablero)
lista_coord_barcos_maquina = t_m.colocar_barcos_aleatorio(barcos, dim_tablero)

# 3. coloco los barcos en el tablero
tablero_barcos_jugador = colocar_barcos(tablero_jugador, lista_coord_barcos_jugador)
tablero_barcos_maquina = colocar_barcos(tablero_maquina, lista_coord_barcos_maquina)

# 4. muestro los tableros. para el jugador muestro el tablero tal cual
# para la máquina, primero creo el tablero oculto y luego lo muestro
print("Tablero jugador \n")
print(tablero_barcos_jugador)

tablero_barcos_maquina_oculto = mostrar_tablero_maquina_oculto(tablero_barcos_maquina)
print("\n Tablero máquina \n")
print(tablero_barcos_maquina_oculto)

# 5. Comienzan los turnos. Pedimos coordenadas hasta que sean válidas
while True:
    print("Te toca atacar")    
    
    # Turno del jugador
    while True:
        try:
            x = int(input("Introduce la fila (0-9): "))
            y = int(input("Introduce la columna (0-9): "))
            if 0 <= x <= 9 and 0 <= y <= 9:
                break
            else:
                print("Coordenadas fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Debes introducir números. Intenta de nuevo.")

    # Disparo del jugador
    tablero_barcos_maquina = disparo_jugador(tablero_barcos_maquina, x, y)
    tablero_barcos_maquina_oculto = mostrar_tablero_maquina_oculto(tablero_barcos_maquina)
    print("\n Tablero máquina \n")
    print(tablero_barcos_maquina_oculto)

    # Comprobar si el jugador ha ganado
    if not quedan_barcos(tablero_maquina):
        print("🎉 ¡HAS GANADO! Todos los barcos enemigos han sido hundidos.")
        break

    # Disparo de la máquina
    tablero_barcos_jugador = disparo_maquina(tablero_barcos_jugador) 
    print("Tablero jugador \n")
    print(tablero_barcos_jugador)

    # Comprobar si la máquina ha ganado
    if not quedan_barcos(tablero_jugador):
        print("💀 La máquina ha ganado... ¡Más suerte la próxima vez!")
        break
