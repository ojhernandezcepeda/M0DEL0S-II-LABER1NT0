class Nodo():
    def __init__(self,valor,posicion,hijos=[]):
        self.valor=valor
        self.posicion = posicion
        self.hijos=hijos

    def agregarHijo(self,hijo):
        self.hijos.append(hijo)
        
    def setPosicion(self,posicion):
        self.posicion=posicion

    def setHijos(self,hijos):
        self.hijos=hijos

def cargarArchivo():
    return[list(linea)[:-1] for linea in open ("Laberinto.txt").readlines()]

def buscar(arbol,posicion):
    if arbol==None:
        return False
    if arbol.posicion==posicion:
        return True
    return buscarhijos(arbol.hijos,posicion) 


def buscarhijos(hijos,posicion):
    if hijos==[]:
        return False
    return buscar(hijos[0],posicion) or buscarhijos(hijos[1:],posicion)

def buscarX(laberinto):
   for x in laberinto:
       for y in range(len(x)):
           if x[y] == "x":
               colocarArbol(laberinto.index(x),y,laberinto, Nodo(0,0,[])) 
                
def colocarArbol(x,y,laberinto, arbol):
        raiz.setPosicion((x,y))
        arbol.setPosicion((x,y))
        raiz.setHijos([verIzquierda(x,y,arbol,laberinto),verAbajo(x,y,arbol,laberinto),verArriba(x,y,arbol,laberinto),verDerecha(x,y,arbol,laberinto)])

def verDerecha(x,y,nodo,laberinto):
    print((x,y)," -> DERECHA")
    if(y+1<=len(laberinto[x])-1 and laberinto[x][y+1]!="1"):
        if(buscar(nodo,(x,y+1))!=True):
            nodo.agregarHijo(Nodo(laberinto[x][y+1],(x,y+1),[]))
            return Nodo(laberinto[x][y+1],(x,y+1),[verAbajo(x,y+1,nodo,laberinto),verArriba(x,y+1,nodo,laberinto),verIzquierda(x,y+1,nodo,laberinto),verDerecha(x,y+1,nodo,laberinto)])
        else:
            return None
    else:
        return None
 
def verIzquierda(x,y,nodo,laberinto):
    print((x,y)," -> IZQUIERDA")
    if(y-1>=0 and laberinto[x][y-1]!="1"):
        if(buscar(nodo,(x,y-1))!=True):
            nodo.agregarHijo(Nodo(laberinto[x][y-1],(x,y-1),[]))
            return Nodo(laberinto[x][y-1],(x,y-1),[verAbajo(x,y-1,nodo,laberinto),verArriba(x,y-1,nodo,laberinto),verIzquierda(x,y-1,nodo,laberinto),verDerecha(x,y-1,nodo,laberinto)])
        else:
            return None
    else:
        return None
 
def verAbajo(x,y,nodo,laberinto):
    print((x,y)," -> ABAJO")
    if(x+1<=len(laberinto)-1 and laberinto[x+1][y]!="1"):
        if(buscar(nodo,(x+1,y))!=True):
            nodo.agregarHijo(Nodo(laberinto[x+1][y],(x+1,y),[]))
            return Nodo(laberinto[x+1][y],(x+1,y),[verAbajo(x+1,y,nodo,laberinto),verArriba(x+1,y,nodo,laberinto),verIzquierda(x+1,y,nodo,laberinto),verDerecha(x+1,y,nodo,laberinto)])
        else:
            return None
    else:
        return None
 
def verArriba(x,y,nodo,laberinto):
    print((x,y)," -> ARRIBA")
    if(x-1>=0 and laberinto[x-1][y]!="1"):
        if(buscar(nodo,(x-1,y))!=True):
            nodo.agregarHijo(Nodo(laberinto[x-1][y],(x-1,y),[]))
            return Nodo(laberinto[x-1][y],(x-1,y),[verAbajo(x-1,y,nodo,laberinto),verArriba(x-1,y,nodo,laberinto),verAbajo(x-1,y,nodo,laberinto),verDerecha(x-1,y,nodo,laberinto)])
        else:
            return None
    else:
        return None

def buscarValor(arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    return buscarhijosValor(arbol.hijos,valor) 


def buscarhijosValor(hijos,valor):
    if hijos==[]:
        return False
    return buscarValor(hijos[0],valor) or buscarhijosValor(hijos[1:],valor)    

"""PRUEBA DEL PROGRAMA"""
raiz=Nodo(0,0,[])
buscarX(cargarArchivo())

if(buscarValor(raiz,"y")==True):
    print("Si tiene solución")
else:
    print("No tiene solución")
