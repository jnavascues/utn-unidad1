import shelve


# ##################################################################
# Defino base de datos
# ##################################################################
with shelve.open("temas/OpcionTemas") as db:
    db["tema1"] = "#222"
    db["tema2"] = "blue"
    db["tema3"] = "OrangeRed"

# ##################################################################
# Defino comando para modificar propiedades de los temas
# ##################################################################


def eleccion_tema(variable):
    """
    Funcion para eleccion de temas
    :param variable:
    :return:
    """
    with shelve.open("temas/OpcionTemas") as datab:
        print(variable)
        print(type(variable))
        if variable == 0:
            variable = "tema1"
            print(variable)
        elif variable == 1:
            variable = "tema2"
            print(variable)
        elif variable == 2:
            variable = "tema3"
            print(variable)
        tema_seleccionado = datab[variable]
        return tema_seleccionado
