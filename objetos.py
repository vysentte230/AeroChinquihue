class cliente:
    def __init__(self, nombre, cantidadvuelos, estadoemergencia):
        self.__nombre = nombre
        self.__cantidadvuelos = cantidadvuelos
        self.__estadoemergencia = estadoemergencia
    def getnombre(self):
        return self.__nombre
    def getcantidadvuelos(self):
        return self.__cantidadvuelos
         return self.__cantidadvuelos
    def estadoemergencia(self):
        return self.__estadoemergencia
    def setnombre(self, nombre):
        self.__nombre = nombre
    def setcantidadvuelos(self, cantidadvuelos):
        self.__cantidadvuelos = cantidadvuelos
    def setestadoemergencia(self, estadoemergencia):
        self.__estadoemergencia = estadoemergencia

class asistente:
    def __init__(self, codigoempleado):
        self.__codigoempleado = codigoempleado
    def getcodigoempleado(self):
        return self.__codigoempleado

class empleado:
    def __init__(self, nombre, rut):
        self.__nombre = nombre
        self.__rut = rut
    def getnombre(self):
        return self.__nombre
    def getrut(self):
        return self.__rut

class gerente:
    def __init__(self, codigoempleado):
        self.__codigoempleado = codigoempleado
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
    def setnombre(self, nombre):
        self.__nombre = nombre
    def setpreciopasaje(self, preciopasaje):
        self.__preciopasaje = preciopasaje
    def setprecioporkg(self, precioporkg):
        self.__precioporkg = precioporkg

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
        # Si no se entregan asientos, se crean según la capacidad del avión
        if asientos is None:
            self.__asientos = []
            for i in range(capacidadpasajeros):
                self.__asientos.append(asiento(i + 1))
        else:
            self.__asientos = asientos

    def getmodelo(self):
        return self.__modelo
    def getcapacidadpasajeros(self):
        return self.__capacidadpasajeros
    def getcapacidadcarga(self):
        return self.__capacidadcarga
    def getasientos(self):
        return self.__asientos

    def asientosdisponibles(self):
        disponibles = []
        for a in self.__asientos:
            if a.estadisponible():
                disponibles.append(a)
        return disponibles
        self.__asientos = asientos
    def getmodelo(self):
        return self.__modelo
    def getcapacidadpasajeros(self):
        return self.__capacidadpasajeros
    def getcapacidadcarga(self):
        return self.__capacidadcarga
    def getasientos(self):
        return self.__asientos

