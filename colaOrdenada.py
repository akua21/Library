# Estructura de datos: COLA ORDENADA
class ColaOrdenada:
    colOrd = []

    # Métodos

    # Añadir un elemento a la cola por orden de prioridad
    def anadir(self, objeto):
        self.colOrd.append(objeto)
        self.colOrd.sort(reverse = True, key = lambda x: x.prioridad)

    # Sacar el primer elemento de la cola y eliminarlo (FIFO)
    def sacar(self):
        return self.colOrd.pop(0)

    # Obtener el primer elemento de la cola (FIFO)
    def primero(self):
        return self.colOrd[0]

    # Obtener todos los elementos de la cola en orden (FIFO)
    def todos(self):
        return self.colOrd
