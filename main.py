import cola
import pila
import colaOrdenada
import arbol

import objeto

# Árbol--------------------------
nuevoArbol = arbol.Arbol()

nuevoObj = objeto.Objeto("raíz", 1)
a = nuevoArbol.anadir(nuevoObj)

nuevoObj = objeto.Objeto("hijo1", 1)
b = nuevoArbol.anadir(nuevoObj, a)

nuevoObj = objeto.Objeto("hijo2", 1)
c = nuevoArbol.anadir(nuevoObj, a)

nuevoObj = objeto.Objeto("hijo11", 1)
d = nuevoArbol.anadir(nuevoObj, b)




nuevoObj = objeto.Objeto("hijo12", 1)
e = nuevoArbol.anadir(nuevoObj, b)


nuevoObj = objeto.Objeto("hijo21", 1)
f = nuevoArbol.anadir(nuevoObj, c)





print("id objeto 0 añadido: ",a)
print("id objeto 1 añadido: ",b)

print("objeto 0 valor: ", nuevoArbol.arb[0].obj.valor)
print("objeto 1 valor: ", nuevoArbol.arb[1].obj.valor)
print("objeto 0 hijos: ", nuevoArbol.arb[0].hijos)
print("arbol: ", nuevoArbol.arb[1].hijos)

#
# x = nuevoArbol.sacar(2)
# print("elem sacado: ", x.obj.valor)

y = nuevoArbol.obtenerHijo(a)
print("hijos de la raíz: ", y)

z = nuevoArbol.obtenerPadre(1)
print("padre del elemento 1: ", z)


arb = nuevoArbol.todos()
for i in arb:
    print("árbol: ", i.id)

# # Cola--------------------------------------------------------------------------
# nuevaCola = cola.Cola()
#
# nuevoObj = objeto.Objeto("hola", 1)
# nuevaCola.anadir(nuevoObj)
# nuevoObj = objeto.Objeto("cara", 2)
# nuevaCola.anadir(nuevoObj)
#
#
# print("cola 0: ",nuevaCola.col[0].valor)
# print("cola 1: ",nuevaCola.col[1].valor)
#
#
# x = nuevaCola.sacar()
# print("primer elem sacado: ",x.valor)
#
#
# y = nuevaCola.primero()
# print("primer elem de la cola después de sacar: ",y.valor)
#
# nuevoObj = objeto.Objeto("cola", 1)
# nuevaCola.anadir(nuevoObj)
#
# col = nuevaCola.todos()
# print("cola: ", col)
# print("valor primer elem de la cola: ",col[0].valor)
# print("valor segundo elem de la cola: ",col[1].valor)



# # Pila--------------------------------------------------------------------------
# nuevaPila = pila.Pila()
#
# nuevoObj = objeto.Objeto("buenas", 1)
# nuevaPila.anadir(nuevoObj)
# nuevoObj = objeto.Objeto("tardes", 2)
# nuevaPila.anadir(nuevoObj)
#
#
# print("pila 0: ",nuevaPila.pil[0].valor)
# print("pila 1: ",nuevaPila.pil[1].valor)
#
#
# x = nuevaPila.sacar()
# print("primer elem sacado: ",x.valor)
#
#
# y = nuevaPila.primero()
# print("primer elem de la pila después de sacar: ",y.valor)
#
# nuevoObj = objeto.Objeto("amigos", 2)
# nuevaPila.anadir(nuevoObj)
#
# pil = nuevaPila.todos()
# print("pila: ", pil)
# print("valor primer elem de la pila: ",pil[0].valor)
# print("valor segundo elem de la pila: ",pil[1].valor)




# # Cola Ordenada-----------------------------------------------------------------
# nuevaColaOrd = colaOrdenada.ColaOrdenada()
#
# nuevoObj = objeto.Objeto("como", 5)
# nuevaColaOrd.anadir(nuevoObj)
# nuevoObj = objeto.Objeto("va", 4)
# nuevaColaOrd.anadir(nuevoObj)
#
#
# print("cola 0: ",nuevaColaOrd.colOrd[0].valor, nuevaColaOrd.colOrd[0].prioridad)
# print("cola 1: ",nuevaColaOrd.colOrd[1].valor, nuevaColaOrd.colOrd[1].prioridad)
#
#
# x = nuevaColaOrd.sacar()
# print("primer elem sacado: ",x.valor)
#
#
# y = nuevaColaOrd.primero()
# print("primer elem de la cola después de sacar: ",y.valor)
#
# nuevoObj = objeto.Objeto("todo", 3)
# nuevaColaOrd.anadir(nuevoObj)
#
#
# colOrd = nuevaColaOrd.todos()
# print("cola: ", colOrd)
# print("valor primer elem de la cola: ",colOrd[0].valor)
# print("valor segundo elem de la cola: ",colOrd[1].valor)
