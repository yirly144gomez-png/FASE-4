
# ARCHIVO: entidades.py
# Clases generales y gestion de clientes.

from abc import ABC, abstractmethod
from excepciones import (
    DatoInvalidoError,
    ParametroFaltanteError
)


# CLASE ABSTRACTA ENTIDAD
class Entidad(ABC):

    def __init__(self, codigo):
        if not codigo or not str(codigo).strip():
            raise ParametroFaltanteError(
                "El codigo de la entidad es obligatorio"
            )

        self._codigo = codigo

    @abstractmethod
    def mostrar_informacion(self):
        pass


# CLASE CLIENTE
class Cliente(Entidad):

    def __init__(self, codigo, nombre, correo, telefono):
        super().__init__(codigo)

        if not nombre or not nombre.strip():
            raise ParametroFaltanteError(
                "El nombre del cliente es obligatorio"
            )

        if not correo or not correo.strip():
            raise ParametroFaltanteError(
                "El correo del cliente es obligatorio"
            )

        if "@" not in correo or "." not in correo:
            raise DatoInvalidoError(
                "El correo electronico no es valido"
            )

        if not telefono or not telefono.isdigit():
            raise DatoInvalidoError(
                "El telefono debe contener solo numeros"
            )

        # Encapsulacion de los datos personales
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        return (
            f"Codigo: {self._codigo} | "
            f"Nombre: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )
