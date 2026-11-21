
# ARCHIVO: reservas.py
# Gestion de reservas de Software FJ.

import logging

from entidades import Cliente
from servicios import Servicio
from excepciones import (
    DatoInvalidoError,
    ParametroFaltanteError,
    OperacionNoPermitidaError,
    ReservaInvalidaError,
    CalculoInconsistenteError
)


# CONFIGURACION DEL ARCHIVO DE LOGS
logging.basicConfig(
    filename="registro_eventos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# CLASE RESERVA
class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion):

        if not codigo:
            raise ParametroFaltanteError(
                "El codigo de la reserva es obligatorio"
            )

        if not isinstance(cliente, Cliente):
            raise DatoInvalidoError(
                "El cliente registrado no es valido"
            )

        if not isinstance(servicio, Servicio):
            raise DatoInvalidoError(
                "El servicio seleccionado no es valido"
            )

        servicio.validar_disponibilidad()
        servicio.validar_parametros(duracion)

        self.codigo = codigo
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

        logging.info(f"Reserva {codigo} creada correctamente")

    # CONFIRMAR RESERVA
    def confirmar(self):

        if self.estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes"
            )

        self.estado = "Confirmada"

        logging.info(f"Reserva {self.codigo} confirmada")
        print(f"Reserva {self.codigo} confirmada")

    # CANCELAR RESERVA
    def cancelar(self):

        if self.estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada"
            )

        self.estado = "Cancelada"

        logging.info(f"Reserva {self.codigo} cancelada")
        print(f"Reserva {self.codigo} cancelada")

    # PROCESAR RESERVA Y CALCULAR COSTO
    def procesar(self, impuesto=0, descuento=0):

        try:
            if self.estado != "Confirmada":
                raise ReservaInvalidaError(
                    "La reserva debe estar confirmada"
                )

            if not isinstance(impuesto, (int, float)) or impuesto < 0:
                raise DatoInvalidoError(
                    "El impuesto no puede ser negativo"
                )

            if not isinstance(descuento, (int, float)) or descuento < 0:
                raise DatoInvalidoError(
                    "El descuento no puede ser negativo"
                )

            costo = self.servicio.calcular_costo(
                self.duracion,
                impuesto,
                descuento
            )

            if costo < 0:
                raise CalculoInconsistenteError(
                    "El costo calculado no puede ser negativo"
                )

        except (TypeError, ValueError) as error:
            logging.exception("Error en los datos de la reserva")
            raise DatoInvalidoError(
                "Los datos utilizados para calcular la reserva son incorrectos"
            ) from error

        except Exception as error:
            logging.exception(
                f"Error al procesar reserva {self.codigo}"
            )
            raise

        else:
            logging.info(
                f"Reserva {self.codigo} procesada. Costo: {costo}"
            )
            print(f"Costo total de la reserva: ${costo:,.0f}")
            print("Reserva procesada correctamente")

            return costo

        finally:
            print("Finalizo el procesamiento de la reserva")

    # MOSTRAR INFORMACION DE LA RESERVA
    def mostrar_informacion(self):

        return (
            f"Reserva: {self.codigo}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duracion: {self.duracion} horas\n"
            f"Estado: {self.estado}"
        )
