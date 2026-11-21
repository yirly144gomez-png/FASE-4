
# ARCHIVO PRINCIPAL: main.py
# Sistema Integral de Gestion de Clientes, Servicios y Reservas
# Software FJ

import logging

from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipos, Asesoria
from reservas import Reserva


# LISTAS PARA ALMACENAR LA INFORMACION
clientes = []
servicios = []
reservas = []


# FUNCION PARA EJECUTAR Y CONTROLAR LAS OPERACIONES
def ejecutar_operacion(numero, descripcion, funcion):

    print("\n" + "=" * 55)
    print(f"OPERACION {numero}: {descripcion}")
    print("=" * 55)

    try:
        funcion()

    except Exception as error:
        logging.exception(f"Error en la operacion {numero}")
        print(f"Se presento un error: {error}")

    else:
        print("Operacion realizada correctamente.")

    finally:
        print("Fin de la operacion.")


# OPERACIONES DEL SISTEMA

def registrar_cliente():

    cliente = Cliente(
        "C001",
        "Maria Perez",
        "maria@gmail.com",
        "3001234567"
    )

    clientes.append(cliente)
    print(cliente.mostrar_informacion())


def registrar_cliente_invalido():

    cliente = Cliente(
        "C002",
        "Carlos Gomez",
        "correo incorrecto",
        "3009876543"
    )

    clientes.append(cliente)


def registrar_segundo_cliente():

    cliente = Cliente(
        "C003",
        "Ana Rodriguez",
        "ana@gmail.com",
        "3114567890"
    )

    clientes.append(cliente)
    print(cliente.mostrar_informacion())


def crear_servicio_sala():

    servicio = ReservaSala(
        "S001",
        "Sala de reuniones",
        50000
    )

    servicios.append(servicio)
    print(servicio.describir())


def crear_servicio_equipos():

    servicio = AlquilerEquipos(
        "S002",
        "Alquiler de computadores",
        30000
    )

    servicios.append(servicio)
    print(servicio.describir())


def crear_servicio_asesoria():

    servicio = Asesoria(
        "S003",
        "Asesoria en sistemas",
        80000
    )

    servicios.append(servicio)
    print(servicio.describir())


def crear_servicio_invalido():

    servicio = ReservaSala(
        "S004",
        "Sala no valida",
        -10000
    )

    servicios.append(servicio)


def crear_reserva():

    reserva = Reserva(
        "R001",
        clientes[0],
        servicios[0],
        2
    )

    reservas.append(reserva)
    print(reserva.mostrar_informacion())


def crear_reserva_duracion_invalida():

    reserva = Reserva(
        "R002",
        clientes[1],
        servicios[1],
        0
    )

    reservas.append(reserva)


def confirmar_reserva():

    reservas[0].confirmar()


def procesar_reserva():

    reservas[0].procesar(
        impuesto=19,
        descuento=5000
    )


def crear_segunda_reserva():

    reserva = Reserva(
        "R003",
        clientes[1],
        servicios[1],
        3
    )

    reservas.append(reserva)
    print(reserva.mostrar_informacion())


def procesar_reserva_pendiente():

    reservas[1].procesar()


def confirmar_segunda_reserva():

    reservas[1].confirmar()


def procesar_segunda_reserva():

    reservas[1].procesar(
        impuesto=19,
        descuento=0
    )


def cancelar_reserva():

    reservas[0].cancelar()


def confirmar_reserva_cancelada():

    reservas[0].confirmar()


def desactivar_servicio():

    servicios[1].cambiar_disponibilidad(False)
    print("El servicio fue desactivado.")


def reservar_servicio_no_disponible():

    reserva = Reserva(
        "R004",
        clientes[0],
        servicios[1],
        2
    )

    reservas.append(reserva)


def mostrar_resumen():

    print("\nCLIENTES REGISTRADOS:")

    for cliente in clientes:
        print(cliente.mostrar_informacion())

    print("\nSERVICIOS REGISTRADOS:")

    for servicio in servicios:
        print(servicio.describir())

    print("\nRESERVAS REGISTRADAS:")

    for reserva in reservas:
        print(reserva.mostrar_informacion())
        print("-" * 40)


# EJECUCION DE LAS PRUEBAS
if __name__ == "__main__":

    print("\nSISTEMA INTEGRAL SOFTWARE FJ")
    print("INICIO DE LAS PRUEBAS DEL SISTEMA")

    ejecutar_operacion(1, "Registrar cliente valido", registrar_cliente)

    ejecutar_operacion(2, "Registrar cliente con correo invalido", registrar_cliente_invalido)

    ejecutar_operacion(3, "Registrar segundo cliente", registrar_segundo_cliente)

    ejecutar_operacion(4, "Crear servicio de reserva de salas", crear_servicio_sala)

    ejecutar_operacion(5, "Crear servicio de alquiler de equipos", crear_servicio_equipos)

    ejecutar_operacion(6, "Crear servicio de asesoria", crear_servicio_asesoria)

    ejecutar_operacion(7, "Crear servicio con precio invalido", crear_servicio_invalido)

    ejecutar_operacion(8, "Crear una reserva valida", crear_reserva)

    ejecutar_operacion(9, "Crear reserva con duracion invalida", crear_reserva_duracion_invalida)

    ejecutar_operacion(10, "Confirmar primera reserva", confirmar_reserva)

    ejecutar_operacion(11, "Procesar primera reserva", procesar_reserva)

    ejecutar_operacion(12, "Crear segunda reserva", crear_segunda_reserva)

    ejecutar_operacion(13, "Procesar reserva pendiente", procesar_reserva_pendiente)

    ejecutar_operacion(14, "Confirmar segunda reserva", confirmar_segunda_reserva)

    ejecutar_operacion(15, "Procesar segunda reserva", procesar_segunda_reserva)

    ejecutar_operacion(16, "Cancelar primera reserva", cancelar_reserva)

    ejecutar_operacion(17, "Confirmar una reserva cancelada", confirmar_reserva_cancelada)

    ejecutar_operacion(18, "Desactivar servicio de equipos", desactivar_servicio)

    ejecutar_operacion(19, "Reservar un servicio no disponible", reservar_servicio_no_disponible)

    ejecutar_operacion(20, "Mostrar resumen del sistema", mostrar_resumen)

    print("\nFIN DE LAS PRUEBAS DEL SISTEMA SOFTWARE FJ")
