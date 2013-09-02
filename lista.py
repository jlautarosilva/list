from pila import *

class Cola(object):
    def __init__(self):
        self.items=[]

    def encolar(self,x):
	self.items.append(x)

    def esta_vacia(self):
	if len(self.items)==0:
	    return True
        else:
	    return False

    def desencolar(self):
	if self.esta_vacia():
	    return None
        else:
	    return self.items.pop(0)


#
#class Nodo:
#    def __init__(self, elemento=None, siguiente=None):
#        self.elemento = elemento
#        self.siguiente = siguiente
# 
#    def __str__(self):
#        return str(self.elemento)
# 
#class ListaEnlazada :
#    def __init__(self) :
#        self.longitud = 0
#        self.cabeza = None
#
#    def imprimeAlReves(self):
#        print "[",
#        if self.cabeza != None:
#        self.cabeza.imprimeAlReves()
#        print "]",
#
#    def agregaPrimero(self, carga):
#        nodo = Nodo(carga)
#        nodo.siguiente = self.cabeza
#        self.cabeza = nodo
#        self.longitud = self.longitud + 1 
#
#
#def imprimeLista(nodo):
#    while nodo:
#        print nodo,
#        nodo = nodo.siguiente
#        print
#def imprimeAlReves(lista):
#    if lista == None: return
#    cabeza = lista
#    cola = lista.siguiente
#    imprimeAlReves(cola)
#    print cabeza,
#def imprimeAlRevesBonito(lista) :
#    print "[",
#    if lista != None :
#        cabeza = lista
#        cola = lista.siguiente
# 
#imprimeAlReves(cola)
#print cabeza,
#print "]",
# 
#def eliminaSegundo(lista):
#    if lista == None: return
#        primero = lista
#        segundo = lista.siguiente
#        primero.siguiente = segundo.siguiente
#        segundo.siguiente = None
#        return segundo
# 

