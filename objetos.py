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
         return self.__estadoemergencia

class asistente:
    def __init__(self, codigoempleado):
        self.codigoempleado = codigoempleado
    def getcodigoempleado(self):
        return self.__codigoempleado
    
class empleado:
    def __init__(self, nombre,rut):
        self.nombre = nombre
        self.rut = rut
    def getnombre(self):
        return self.__nombre
    def getrut(self):
        return self.__rut
class gerente:
    def __init__(self,codigoempleado):
        self.codigoempleado = codigoempleado
    def getcodigoempleado(self):
        return self.__codigoempleado
    