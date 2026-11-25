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
    def __init__(self,nombre,preciopasaje,precioKg):
        self.nombre = nombre
        self.preciopasaje = preciopasaje
        self.preciokg = precioKg
    def getnombre(self):
        return self.__nombre
    def getpreciopasaje(self):
        return self.__preciopasaje
    def getprecioKg(self):
        return self.__precioKg

class vuelo:
    def __init__(self,codigo,fecha,horario,estado,cargaActual):
        self.codigo = codigo
        self.fecha = fecha
        self.horario = horario
        self.estado = estado
        self.cargaActual = cargaActual
    def getcodigo(self):
        return self.__codigo
    def getfecha(self):
        return self.__fecha
    def gethorario(self):
        return self.__horario
    def getestado(self):
        return self.__estado
    def getcargaActual(self):
        return self.__cargaActual

class avion:
    def __init__(self,modelo,cantidadpasajeros,capacidadCarga):
        self.modelo = modelo
        self.cantidadpasajeros = cantidadpasajeros
        self.capacidadCarga = capacidadCarga
    def getmodelo(self):
        return self.__modelo
    def getcantidadpasajeros(self):
        return self.__cantidadpasajeros
    def getcapacidadCarga(self):
        return self.__capacidadCarga

class Asiento:
    def __init__(self,numero,ocupado):
        self.numero = numero
        self.ocupado = ocupado
    def getnumero(self):
        return self.__numero
    def getocupado(self):
        return self.__ocupado
    