
import numpy as np
import variables as v
  
    
def crear_tablero(): # crear tableros
       
        matrices = np.full((10,10),"¨")
        return matrices
        
def crear_barcos(eslora): #crear barcos
    barco = []
    direccion = np.random.choice(("v", "h"))

    if direccion == "v":
        fila = np.random.randint(0, 11 - eslora)
        columna = np.random.randint(0, 10)
        for i in range(eslora):
            barco.append((fila + i, columna))
    else:
        fila = np.random.randint(0, 10)
        columna = np.random.randint(0, 11 - eslora)
        for i in range(eslora):
            barco.append((fila, columna + i))

    return barco

def se_tocan(barco, flota): # condicion que no se toquen
    for fila, columna in barco:
        for otro_barco in flota:
            for otra_fila, otra_columna in otro_barco:
                if abs(fila - otra_fila) <= 1 and abs(columna - otra_columna) <= 1:
                    return True
    return False


def crear_flota(): # crear la flota
    flota = []
    for eslora in v.esloras:
        colocado = False
        while not colocado:
            barco = crear_barcos(eslora)
            if not se_tocan(barco, flota):
                flota.append(barco)
                colocado = True
    return flota


def colocar_barcos(flota,tablero): # colocar barcos en tablero

    for barco in flota:
        for fila,columna in barco:
            tablero[fila,columna]= "1"
    
    return tablero       

def comprobar_flota(): # comprobar si la flota cumple condiciones, si fuera de rango
    esloras=[4,3,3,2,2,2] # si fuera de rango, repetir
    flota=[]
    for eslora in v.crear_flota:
        flota.append(crear_barcos(eslora))

    for barcos in flota:
        for coordenada in barcos:
            for i in coordenada:
                if i <0 or i>9: #repeat
                    return crear_flota()    # fuero de rango
    
    return flota   

def inicio ():  # inicio de progama y sorteo de jugador que inicia la partida  

    var1=input("Elige cara o cruz para ver quien comienza el juego:      ").lower()

    if  var1 == "cara" or var1 =="cruz":
            var1 = np.random.rand(1)
            print(var1)
            if var1 > 0.5:
             print("Comienza el jugador")
             v.inicio_juego=0
            else:
             print("Comienza el bot") 
             v.inicio_juego=1

    else:
        return inicio()  
    
def jugar (matriz_barcos_player, matriz_disparos_player, matriz_barcos_bot,matriz_disparos_bot,): # funcion principal y logica del juego de juego 
    coordenadas_bot = [] # lista coordenadas
    coordenadas_player  = []
    restantes_bot = 16 # aciertos restantes apra terminar el juego
    restantes_player = 16
    disparos_bot=0 # numero de disparos realizados
    disparos_player=0
    turno_bot = 0 # nuemro de turnos jugados 
    turno_player = 0
    v.inicio_juego # por defecto 0, cara o cruz para sortear el player que comienza a jugar
   
    
     

    while restantes_bot !=0  and  restantes_player !=0:

        while (v.inicio_juego == 1) &  (restantes_bot !=0): # JUEGA EL BOT 1
                
                coordenada_bot = tuple(np.random.randint(0,10,size=2))
                if coordenada_bot in coordenadas_bot:# COMPROBACION DE REPETICION
                    print("esa cooordenada ya al has dicho")
                    print("dime otra coordenada")
                    continue 
                   
                coordenadas_bot.append(coordenada_bot)
                              
                if  matriz_barcos_player[coordenada_bot] == "1": # COMPROBACION DISPARO                  
                    matriz_barcos_player[coordenada_bot] = 4 # 4  cambio donde cae el disparo
                    matriz_disparos_bot[coordenada_bot] = 4
                    turno_bot = turno_bot+1 # Numero de turnos
                    restantes_bot= restantes_bot -1 # posiciones restantes
                    v.inicio_juego = 1
                    print(matriz_disparos_bot)
                    print("acierto en ", coordenada_bot)
                    
                else:                 
                    matriz_barcos_player[coordenada_bot] =0
                    matriz_disparos_bot[coordenada_bot] = 0
                    turno_bot = turno_bot+1
                    v.inicio_juego= 0
                    print(matriz_disparos_bot)
                    print("AGUA  en ",coordenada_bot ,  "es tu turno")
                    print(coordenada_bot)
                    continue


        while (v.inicio_juego == 0 ) &  (restantes_player !=0): # JUEGO YO 0
                    
                    entrada = input("Dime dos números seguidos (fila y columna): ")
                    coordenada_player = (int(entrada[0]), int(entrada[1]))

                    if coordenada_player in coordenadas_player:
                     print("Ya has disparado ahí")
                     continue
                   
                    coordenadas_player.append(coordenada_player)
                
                    if matriz_barcos_bot[coordenada_player] == "1":
                        matriz_barcos_bot[coordenada_player]  = 4 # 4 donde cae el disparo acertando
                        matriz_disparos_player[coordenada_player] = 4
                        turno_player = turno_player+1
                        v.inicio_juego= 0
                        restantes_player= restantes_player-1
                        print(matriz_disparos_player)
                        print("acierto en ",coordenada_player)
                        #if  coordenada_player in matriz_barcos_bot   no tiene otra al lado           #HUNDIDO
                                    
                    else:
                        matriz_barcos_bot[coordenada_player] = 0
                        matriz_disparos_player[coordenada_player] = 0
                        turno_player = turno_player+1
                        v.inicio_juego= 1
                        print(matriz_disparos_player)
                        print("AGUA  ",coordenada_player ,  "es tu turno")
                        print(coordenada_player)
                   

    if restantes_bot == 0:
        print("Ha ganado el bot")
   
    if restantes_player== 0:
        print("Ha ganado el player")  

print("~~~~~~~~~~ - HUNDIR LA FLOTA - ~~~~~~~~~~~~") 




        

                














