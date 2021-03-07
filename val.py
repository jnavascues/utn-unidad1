import re


def validar(cad):
    """
    Funcion para validacion del campo Titulo
    :param cad: String a validar
    :return: True/False
    """
    patron = "^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
    try:
        print("------------------")
        print(cad)
        re.match(patron, cad)
        if(re.match(patron, cad)):
            return True
        else:
            return False
    except:
        return False
