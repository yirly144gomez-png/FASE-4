
# ARCHIVO: servicios.py
# Gestion de los servicios de Software FJ.

from abc import ABC, abstractmethod
from excepciones import (
    DatoInvalidoError,
    ServicioNoDisponibleError,
    CalculoInconsistenteError
)


# CLASE ABSTRACTA SERVICIO
class Servicio(ABC):

    def __init__(self, codigo, nombre, precio):
        if not codigo or not nombre:
            raise DatoInvalidoError(
                "El codigo y el nombre son obligatorios"
            )

        if precio <= 0:
            raise DatoInvalidoError(
                "El precio debe ser mayor que cero"
            )

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.disponible = True

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.nombre} no esta disponible"
            )

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    def cambiar_disponibilidad(self, estado):
        if not isinstance(estado, bool):
            raise DatoInvalidoError(
                "La disponibilidad debe ser verdadera o falsa"
            )
        self.disponible = estado


# CLASE 1: RESERVA DE SALAS
class ReservaSala(Servicio):

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatoInvalidoError(
                "Las horas de reserva deben ser mayores que cero"
            )

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_parametros(duracion)

        subtotal = self.precio * duracion
        costo = subtotal + (subtotal * impuesto / 100) - descuento

        if costo < 0:
            raise CalculoInconsistenteError(
                "El costo de la sala no puede ser negativo"
            )

        return costo

    def describir(self):
        return (
            f"Reserva de salas: {self.nombre}. "
            f"Precio por hora: ${self.precio}"
        )


# CLASE 2: ALQUILER DE EQUIPOS
class AlquilerEquipos(Servicio):

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatoInvalidoError(
                "Las horas de alquiler deben ser mayores que cero"
            )

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_parametros(duracion)

        subtotal = self.precio * duracion
        costo = subtotal + (subtotal * impuesto / 100) - descuento

        if costo < 0:
            raise CalculoInconsistenteError(
                "El costo del equipo no puede ser negativo"
            )

        return costo

    def describir(self):
        return (
            f"Alquiler de equipos: {self.nombre}. "
            f"Precio por hora: ${self.precio}"
        )


# CLASE 3: ASESORIAS ESPECIALIZADAS
class Asesoria(Servicio):

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatoInvalidoError(
                "Las horas de asesoria deben ser mayores que cero"
            )

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_parametros(duracion)

        subtotal = self.precio * duracion
        costo = subtotal + (subtotal * impuesto / 100) - descuento

        if costo < 0:
            raise CalculoInconsistenteError(
                "El costo de la asesoria no puede ser negativo"
            )

        return costo

    def describir(self):
        return (
            f"Asesoria especializada: {self.nombre}. "
            f"Precio por hora: ${self.precio}"
        )
