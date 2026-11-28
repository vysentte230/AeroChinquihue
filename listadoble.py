from Nododoble import NodoDoble


class ListaDoble:

    def __init__(self):
        self.cabeza = None  # primer nodo
        self.cola = None    # último nodo

    def agregar(self, dato): # type: ignore

        nuevo = NodoDoble(dato) # type: ignore
        if self.cabeza is None: # Lista vacía, el nuevo nodo es a la vez el primero y el último.

            self.cabeza = self.cola = nuevo

        else: # Se une en las 2 direcciones (eso la hace "doble"):
            
            nuevo.anterior = self.cola    # type: ignore # nuevo <- cola
            self.cola.siguiente = nuevo   # type: ignore # cola  -> nuevo
            self.cola = nuevo             # ahora el nuevo es el último

    def recorrer(self):
        # Devuelve los datos en orden (cabeza -> cola), para listarlos en la GUI
        datos = []
        actual = self.cabeza
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def eliminar(self, dato):
        # Busca el nodo que contiene el dato y lo saca de la lista (True si lo encontró)
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                if actual.anterior is None:   # es la cabeza
                    self.cabeza = actual.siguiente
                else:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente is None:  # es la cola
                    self.cola = actual.anterior
                else:
                    actual.siguiente.anterior = actual.anterior
                return True
            actual = actual.siguiente
        return False
