import numpy as np
import funciones as f 
import variables as v
  

 


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                           ")
print("TABLERO PLAYER PARA DISPARAR")
print("                           ")
print(f.crear_tablero())
print("------------------------------")
print("------------------------------")
print("TABLERO BOT PARA DISPARAR")
print(f.crear_tablero())
print("                           ")
print("///////////////////////////")
print("                           ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                           ")
print("TABLERO PLAYER PARA COMPROBAR")
print("                           ")
print(f.crear_tablero())
print("------------------------------")
print("------------------------------")
print("TABLERO BOT PARA COMPROBAR")
print(f.crear_tablero())
print("                           ")


matriz_barcos_player = f.crear_tablero()
matriz_disparos_player = f.crear_tablero()
matriz_barcos_bot = f.crear_tablero()
matriz_disparos_bot = f.crear_tablero()

flota_jugador = f.crear_flota()
flota_bot = f.crear_flota()

tablero_jugador = f.crear_tablero()
tablero_bot = f.crear_tablero()

f.colocar_barcos(flota_jugador, tablero_jugador)
f.colocar_barcos(flota_bot, tablero_bot)

print("Barcos del jugador:")
print(tablero_jugador)

print("Barcos del bot:")
print(tablero_bot)

f.inicio()
f.jugar()












