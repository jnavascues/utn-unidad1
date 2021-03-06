from tkinter import Toplevel, Button
from tkinter.messagebox import showerror
from modificar import crear_form_modificar, campos, imprimir
from base_datos import TablaProducto
import val


def show(variables, popup_modificar):
    """
    Funcion para imprimir variables en consola
    :param variables:
    :param popup_modificar:
    :return:
    """
    popup_modificar.destroy()
    imprimir(variables)


def modifica(variables, popup_modificar, elobjeto):
    """
    Funcion para modificar un registro
    :param variables: Titulo y descripcion
    :param popup_modificar: Popup TK
    :param elobjeto: objeto producto
    :return:
    """
    lista = []
    for variable in variables:
        lista.append(variable.get())
    validar = lista[1]
    if val.validar(validar) is True:
        popup_modificar.destroy()
        elid = lista[0]
        tit = lista[1]
        desc = lista[2]
        actualizar = TablaProducto.update(
            titulo=tit, descripcion=desc).where(TablaProducto.id == elid)
        actualizar.execute()
        elobjeto.set_event("Modificacion", tit)
        elobjeto.mostrar()
    else:
        showerror('Titulo No valido',
                  'El campo de título no cumple los requisitos, ingrese datos alfabéticos')


def modificar(objeto):
    """
    Funcion que se encarga de iniciar el nuevo popup(toplevel)
    :param objeto:
    :return:
    """
    popup_modificar = Toplevel()
    vars_modificar = crear_form_modificar(popup_modificar, campos)
    Button(popup_modificar, text='Modificar', command=(
        lambda: modifica(vars_modificar, popup_modificar, objeto))).pack()
    popup_modificar.grab_set()
    popup_modificar.focus_set()
    popup_modificar.wait_window()
