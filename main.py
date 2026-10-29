import numpy as np
import funciones as f 
import variables as v
  



matriz_barcos_player = f.crear_tablero() # crear los tableros vacios
matriz_disparos_player = f.crear_tablero()
matriz_barcos_bot = f.crear_tablero()
matriz_disparos_bot = f.crear_tablero()


print("~~~~~~~~~~ - HUNDIR LA FLOTA - ~~~~~~~~~~~~") 
print("                           ")
print("                           ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                           ")
print("TABLERO PLAYER PARA DISPARAR")
print("                           ")
matriz_barcos_player = f.crear_tablero()
print("------------------------------")
print("------------------------------")
print("TABLERO BOT PARA DISPARAR")
print(matriz_disparos_bot)
print("                           ")
print("///////////////////////////")
print("                           ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                           ")
print("TABLERO PLAYER PARA COMPROBAR")
print("                           ")
print(matriz_barcos_player)
print("------------------------------")
print("------------------------------")
print("TABLERO BOT PARA COMPROBAR")
print(matriz_disparos_bot)
print("                           ")

flota_jugador = f.crear_flota() # crear las flotas
flota_bot = f.crear_flota()

tablero_jugador = f.crear_tablero() # crear tablero con los barcos
tablero_bot = f.crear_tablero()

f.colocar_barcos(flota_jugador, tablero_jugador) # colocar los barcos en el tablero
f.colocar_barcos(flota_bot, tablero_bot)

#print("Barcos del jugador:", flota_jugador) # mostrar coordenadas para probar el juego
#print("Barcos del bot:", flota_bot)

f.inicio()
f.jugar(tablero_jugador, matriz_disparos_player, tablero_bot, matriz_disparos_bot)












