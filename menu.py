class menu:
    def __init__(self, lista): # type: ignore
        self.lista = lista

    def mostrar_menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Elegir primera nave")
            print("2. Elegir segunda nave")
            print("3. Elegir tercera nave")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion in ("1", "2", "3"):
                self.mostrar_nave(int(opcion)) # type: ignore
            elif opcion == "4":
                print("Gracias por ver aerochinquiue. ¡Hasta luego!")
                return
            else:
                print("Opción inválida. Intente nuevamente.")

    def mostrar_nave(self, numero): # type: ignore
        actual = self.lista.cabeza # type: ignore
        posicion = 1
        while actual is not None:
            if posicion == numero:
                nave = actual.dato # type: ignore
                print(f"La nave {numero} es {nave.modelo} y tiene capacidad para {nave.capacidad} personas y una capacidad de peso de {nave.peso_kg} kg para los encargos") # type: ignore
                return
            actual = actual.siguiente # type: ignore
            posicion += 1