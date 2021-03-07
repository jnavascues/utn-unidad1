# Codigo Legacy de decoradores

from base_datos import TablaRegistros
from datetime import datetime


def deco_alta(funcion):
    def reportar(*args):
        funcion(*args)
        print("Ingreso de nuevo registro")
        TablaRegistros.create(timestamp=datetime.now(),
                              event="Alta", titulo="titulo")
    return reportar


def deco_modificar(funcion):
    def reportar(*args):
        funcion(*args)
        print("Actualizacion de registro")
    return reportar


def deco_eliminar(funcion):
    def reportar(*args):
        funcion(*args)
        print("Eliminacion de registro")
    return reportar
