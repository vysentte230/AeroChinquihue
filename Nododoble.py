class NodoDoble:

    def __init__(self, dato): # type: ignore
        self.dato = dato
        self.siguiente = None  # nodo que viene después (None si es el último)
        self.anterior = None   # nodo que viene antes (None si es el primero)
