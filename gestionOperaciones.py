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