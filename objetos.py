class personaje:
    def __init__(self, nombre, vida, fuerza_base, mana, defensa):
        if vida < 0:
            raise ValueError("La vida no puede ser negativa.")
        self.__nombre = nombre
        self.__vida = vida
        self.__vida_maxima = vida
        self.__fuerza_base = fuerza_base
        self.__mana = mana
        self.__defensa = defensa
        self.__item = None

    def getnombre(self):
        return self.__nombre
class cliente:
    def __init__(self, nombre, cantidadvuelos, estadoemergencia):
        self.__nombre = nombre
        self.__cantidadvuelos = cantidadvuelos
        self.__estadoemergencia = estadoemergencia
    def getnombre(self):
         return self.__nombre
    def getcantidadvuelos(self):
         return self.___cantidadvuelos
    def estadoemergencia(self):

class asistente:
    def __init__(self, codigoempleado):
        self.codigoempleado = codigoempleado
    def getcodigoempleado(self):
        return self.__codigoempleado


