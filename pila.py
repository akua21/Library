# Estructura de datos: PILA
class Pila:
    pil = []

    # Métodos

    # Añadir un elemento a la pila
    def anadir(self, objeto):
        self.pil.append(objeto)

    # Sacar el primer elemento de la pila y eliminarlo (LIFO)
    def sacar(self):
        return self.pil.pop()


    # Obtener el primer elemento de la cola (LIFO)
    def primero(self):
        return self.pil[-1]

    # Obtener todos los elementos de la pila en orden (LIFO)
    def todos(self):
        return self.pil[::-1]
