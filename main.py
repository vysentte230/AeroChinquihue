from listadoble import ListaDoble 
import menu


class Nave:
    def __init__(self, modelo, capacidad, peso_kg): # type: ignore
        self.modelo = modelo
        self.capacidad = capacidad  # personas
        self.peso_kg = peso_kg      


class main:

    def __init__(self):
        self.lista = ListaDoble()
        self.lista.agregar(Nave("CESSNA 310", 5, 910)) # type: ignore
        self.lista.agregar(Nave("CESSNA 208 CARAVAN", 9, 1315)) # type: ignore
        self.lista.agregar(Nave("LET 410 UVP-E20", 19, 1800)) # type: ignore

    def mostrar_menu(self):
        menu_obj = menu.menu(self.lista) # type: ignore
        menu_obj.mostrar_menu() # type: ignore

if __name__ == "__main__":
    aplicacion = main()
    aplicacion.mostrar_menu()