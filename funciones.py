
import numpy as np
import variables as v
  

def crear_tablero(): 
        num=4
        matrices = np.zeros((10,10))
        num= num+1
        return matrices
        
def crear_barcos(eslora): 
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



def se_tocan(barco, flota):
    for fila, columna in barco:
        for otro_barco in flota:
            for otra_fila, otra_columna in otro_barco:
                if abs(fila - otra_fila) <= 1 and abs(columna - otra_columna) <= 1:
                    return True
    return False


def crear_flota():
    flota = []
    for eslora in v.esloras:
        colocado = False
        while not colocado:
            barco = crear_barcos(eslora)
            if not se_tocan(barco, flota):
                flota.append(barco)
                colocado = True
    return flota


def colocar_barcos(flota,tablero):

    for barco in flota:
        print("Barco",barco)
        for fila,columna in barco:
            tablero[fila,columna]= 1
    
    return tablero       

def comprobar_flota():
    esloras=[4,3,3,2,2,2]
    flota=[]
    for eslora in v.crear_flota:
        flota.append(crear_barcos(eslora))

    for barcos in flota:
        for coordenada in barcos:
            for i in coordenada:
                if i <0 or i>9: #repeat
                    return crear_flota()    # fuero de rango
    
    return flota   

def inicio ():    

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
    
def jugar ():
    coordenada_bot = []
    coordenada_player  = []
    restantes_bot = 16
    restantes_player = 16
    disparos_bot=0
    disparos_player=0
    turno_bot = 0
    turno_player = 0
    v.inicio_juego
     

    if restantes_bot !=0  or  restantes_player !=0:

        while (v.inicio_juego == 1) &  (restantes_bot !=0): # JUEGA EL BOT

            coordenada_bot = np.random.randint(0-10,size=(1,1))
            coordenada_bot = list(coordenada_bot).append
            if coordenada_bot  in  matriz_barcos_player == "1":
                matriz_barcos_player[coordenada_bot] = 4# 4 donde cae el disparo
                matriz_disparos_bot[coordenada_bot] = 4
                turno_bot = turno_bot+1
                restantes_bot= restantes_bot -1
                v.inicio_juego = 1
                print("acierto")
                return jugar()
            else:
                disparos_bot = list(disparos_bot).append
                matriz_barcos_player[coordenada_bot] =2
                matriz_disparos_bot[coordenada_bot] = 2
                turno_bot = turno_bot+1
                v.inicio_juego= 0
                print("AGUA  , es tu turno")
                return jugar()


        while (v.inicio_juego == 0 ) &  (restantes_player !=0): # JUEGO YO
            coordenada_player = input("Dime coordenada")
            coordenada_player  = list(coordenada_player ).append
            if coordenada_player  in  matriz_barcos_bot == "1":
                matriz_barcos_bot[coordenada_bot] = 4# 4 donde cae el disparo
                matriz_disparos_bot[coordenada_bot] = 4
                turno_bot = turno_bot+1
                v.inicio_juego= 0
                restantes_player= restantes_player-1
                print("acierto")
                return jugar()
            else:
                disparos_player = list(disparos_player).append
                matriz_barcos_bot[coordenada_bot] = 2
                matriz_disparos_bot[coordenada_bot] = 2
                turno_player = turno_player+1
                v.inicio_juego= 1
                print("AGUA  , es tu turno")

    if restantes_bot == 0:
        print("Ha ganado el bot")
    else:
        pass
    if restantes_player== 0:
        print("Ha ganado el player")  
    else:
        pass




        

                














