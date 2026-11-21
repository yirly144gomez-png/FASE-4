class ErrorSistemaSoftwareFJ(Exception):
    """Excepción base para todos los errores del sistema de Software FJ."""

    def __init__(self, mensaje: str, codigo: str = "ERR_GENERAL"):
        self.codigo = codigo
        super().__init__(f"[{codigo}] {mensaje}")


class DatoInvalidoError(ErrorSistemaSoftwareFJ):
    """Se lanza cuando un dato no cumple con las reglas de validación."""

    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo="ERR_DATO_INVALIDO")


class ParametroFaltanteError(ErrorSistemaSoftwareFJ):
    """Se lanza cuando falta un parámetro obligatorio o está vacío."""

    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo="ERR_PARAMETRO_FALTANTE")


class OperacionNoPermitidaError(ErrorSistemaSoftwareFJ):
    """Se lanza cuando se intenta una acción no válida según el estado actual."""

    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo="ERR_OPERACION_NO_PERMITIDA")


class ReservaInvalidaError(ErrorSistemaSoftwareFJ):
    """Se lanza ante intentos de reserva incorrectos o inconsistentes."""

    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo="ERR_RESERVA_INVALIDA")


class ServicioNoDisponibleError(ErrorSistemaSoftwareFJ):
    """Se lanza cuando un servicio no está disponible para ser reservado."""

    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo="ERR_SERVICIO_NO_DISPONIBLE")


class CalculoInconsistenteError(ErrorSistemaSoftwareFJ):
    """Se lanza cuando el cálculo de costos o duraciones arroja valores inválidos."""

    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo="ERR_CALCULO_INCONSISTENTE")
