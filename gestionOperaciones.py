class destino:
    def __init__(self, nombre: str, precioPasaje: int, precioKg):
        self.nombre = nombre
        self.precioPasaje = precioPasaje
        self.precioKg = precioKg

class RegistroPasaje:
    def __init__(self, pasajero: str, destino: destino, asiento: int, total: float, medioPago: str):
        self.pasajero = pasajero
        self.destino = destino
        self.asiento = asiento
        self.total = total
        self.medioPago = medioPago

class RegistroEncomienda:
    def __init__(self, remitente: str, destino: destino, pesoKg: float, total: float, medioPago: str):
        self.remitente = remitente
        self.destino = destino
        self.pesoKg = pesoKg
        self.total = total
        self.medioPago = medioPago

class GestorPasajesEncomiendas:
    def __init__(self):
        self.destinos = {
            "Cochamó": destino("Cochamó", 20000, 5000),
            "Puelo Bajo": destino("Puelo Bajo", 20000, 5000),
            "Contao": destino("Contao", 20000, 5000),
            "Río Negro": destino("Río Negro", 25000, 6000),
            "Pupelde": destino("Pupelde", 25000, 6000),
            "Chepu": destino("Chepu", 30000, 8000),
            "Ayacara": destino("Ayacara", 30000, 8000),
            "Pillán": destino("Pillán", 40000, 12000),
            "Reñihue": destino("Reñihue", 40000, 12000),
            "Isla Quenac": destino("Isla Quenac", 40000, 12000),
            "Palqui": destino("Palqui", 40000, 12000),
            "Chaitén": destino("Chaitén", 50000, 15000),
            "Santa Bárbara": destino("Santa Bárbara", 50000, 15000),
        }
        self.pasajes = []
        self.encomiendas = []

    def calcularTotal(self, montoBase: float, cantidadVuelos: int = 0, emergencia: bool = False) -> float:
            if emergencia:
                return 0.0
            if cantidadVuelos > 10:
                return montoBase * 0.90
            return montoBase

    def gestionarPasaje(
        self,
        pasajero: str,
        nombreDestino: str,
        asiento: int,
        medioPago: str,
        cantidadVuelos: int = 0,
        emergencia: bool = False,
    ) -> RegistroPasaje:
        if nombreDestino not in self.destinos:
            raise ValueError(f"Destino no válido: {nombreDestino}")
        if any(p.destino.nombre == nombreDestino and p.asiento == asiento for p in self.pasajes):
            raise ValueError(f"El asiento {asiento} ya está ocupado para {nombreDestino}.")

        destino = self.destinos[nombreDestino]
        total = self.calcularTotal(destino.precioPasaje, cantidadVuelos, emergencia)
        registro = RegistroPasaje(pasajero, destino, asiento, total, medioPago)
        self.pasajes.append(registro)
        return registro

    def gestionarEncomienda(
        self,
        remitente: str,
        nombreDestino: str,
        pesoKg: float,
        medioPago: str,
        cargaMaximaKg: float = 1800.0,
        cantidadVuelos: int = 0,
        emergencia: bool = False,
    ) -> RegistroEncomienda:
        if nombreDestino not in self.destinos:
            raise ValueError(f"Destino no válido: {nombreDestino}")
        if pesoKg <= 0:
            raise ValueError("El peso debe ser mayor a 0 kg.")

        cargaActual = sum(e.pesoKg for e in self.encomiendas if e.destino.nombre == nombreDestino)
        if cargaActual + pesoKg > cargaMaximaKg:
            raise ValueError("Se excede la capacidad máxima de carga disponible.")

        destino = self.destinos[nombreDestino]
        montoBase = pesoKg * destino.precioKg
        total = self.calcularTotal(montoBase, cantidadVuelos, emergencia)
        registro = RegistroEncomienda(remitente, destino, pesoKg, total, medioPago)
        self.encomiendas.append(registro)
        return registro
