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
