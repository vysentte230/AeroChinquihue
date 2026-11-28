class cliente:
    def __init__(self, nombre, cantidadvuelos, estadoemergencia):
        self.__nombre = nombre
        self.__cantidadvuelos = cantidadvuelos
        self.__estadoemergencia = estadoemergencia
    def getnombre(self):
         return self.__nombre
    def getcantidadvuelos(self):
         return self.__cantidadvuelos
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

class aerodromo:
    def __init__(self, nombre, preciopasaje, precioporkg):
        self.__nombre = nombre
        self.__preciopasaje = preciopasaje
        self.__precioporkg = precioporkg

    def getnombre(self):
        return self.__nombre
    def getobtenerpreciopasaje(self):
        return self.__preciopasaje
    def getobtenerprecioencomienda(self):
        return self.__precioporkg

class asiento:
    def __init__(self, numero, ocupado= False):
        self.__numero = numero
        self.__ocupado = ocupado

    def getnumero(self):
        return self.__numero

    def getestadisponible(self):
        return not self.__ocupado

    def getocupar(self):
        if self.__ocupado:
            return False
        self.__ocupado = True
        return True

    def getdesocupar(self):
        self.__ocupado = False

class avion:
    def __init__(self, modelo, capacidadpasajeros, capacidadcarga, asientos=None):
        self.__modelo = modelo
        self.__capacidadpasajeros = capacidadpasajeros
        self.__capacidadcarga = capacidadcarga
        self.__asientos = asientos
    def getmodelo(self):
        return self.__modelo
    def getcapacidadpasajeros(self):
        return self.__capacidadpasajeros
    def getcapacidadcarga(self):
        return self.__capacidadcarga
    def getasientos(self):
        return self.__asientos

