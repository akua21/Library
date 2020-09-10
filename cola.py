# Estructura de datos: COLA
class Cola:
    col = []

    # Métodos

    # Añadir un elemento a la cola
    def anadir(self, objeto):
        self.col.append(objeto)

    # Sacar el primer elemento de la cola y eliminarlo (FIFO)
    def sacar(self):
        return self.col.pop(0)

    # Obtener el primer elemento de la cola (FIFO)
    def primero(self):
        return self.col[0]

    # Obtener todos los elementos de la cola en orden (FIFO)
    def todos(self):
        return self.col
