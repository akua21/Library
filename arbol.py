# Estructura de datos: ÁRBOL

class ObjetoArbol:
    def __init__(self, obj, id, padre, hijos):
        self.obj = obj
        self.id = id
        self.padre = padre
        self.hijos = hijos

contador = 0
class Arbol:
    arb = []


    # Métodos

    # Añadir un elemento al ÁRBOL
    def anadir(self, objeto, padre = None):
        if padre == None:
            if len(self.arb) == 0:
                nuevoObj = ObjetoArbol(objeto, 0, None, [])
                self.arb.append(nuevoObj)
            else:
                print("ERROR - Ya existe una raíz")
                return print("No se ha podido añadir el objeto")
        else:
            global contador
            contador += 1
            nuevoObj = ObjetoArbol(objeto, contador, padre, [])
            self.arb.append(nuevoObj)

            for elem in self.arb:
                if elem.id == padre:
                    elem.hijos.append(contador)

        return nuevoObj.id

    # Sacar elemento sin hijos (nodos hoja) y eliminarlo
    def sacar(self, id):

        for i, elem in enumerate(self.arb):
            if elem.id == id:
                if elem.hijos == []:
                    for item in self.arb:
                        if item.id == elem.padre:
                            for identif in item.hijos:
                                if identif == elem.id:
                                    item.hijos.remove(identif)
                    return self.arb.pop(i)
                else:
                    return print("No puedes sacar este elemento porque tiene hijos")
        return ("No se ha encontrado ningún elemento con el id: ", id, " en el árbol")



    # Obtener hijo/s del elemento
    def obtenerHijo(self, id):
        for elem in self.arb:
            if elem.id == id:
                if elem.hijos == []:
                    return print("El elemento no tiene hijos")
                else:
                    return elem.hijos
        return ("No se ha encontrado ningún elemento con el id: ", id, " en el árbol")

    # Obtener padre del elemento
    def obtenerPadre(self, id):
        for elem in self.arb:
            if elem.id == id:
                if elem.padre != None:
                    return elem.padre
                else:
                    return print("El elemento es la raíz por lo que no tiene padre")
        return ("No se ha encontrado ningún elemento con el id: ", id, " en el árbol")


    # Obtener todos los elementos del árbol en profundidad
    def todos(self):
        arbolP = []
        for elem in self.arb:
            if elem.id == 0:
                arbolP.append(elem)
                h = self.obtenerHijo(elem.id)

                if h == []:
                    return arbolP
                else:
                    for hijoId in h:
                        hijos = self.obtenerHijo(hijoId)
                        if hijos != None and hijoId > 0:
                            elems = self.obtenerR(hijoId)

                            for e in elems:
                                arbolP.append(e)
                        elif hijos == None and hijoId > 0:
                            elem = self.obtenerElem(hijoId)
                            arbolP.append(elem)
        return arbolP


    def obtenerElem(self, elemId):
        for elem in self.arb:
            if elem.id == elemId:
                return elem

    def obtenerR(self, id):
        elemHijos = []
        h = self.obtenerHijo(id)
        if h == None:
            e = self.obtenerElem(id)
            return elemHijos.append(e)
        else:
            elemHijos.append(self.obtenerElem(id))

            for i in h:
                elemHijos.append(self.obtenerElem(i))
                self.obtenerR(i)

        return elemHijos
