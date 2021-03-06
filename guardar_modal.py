from tkinter import Toplevel, Button
from tkinter.messagebox import showerror
from guardar import crear_form_guardar, campos, imprimir
from base_datos import TablaProducto
import val


def show(variables, popup_guardar):
    """
    funcion debug para imprimir los datos en consola
    :param variables:
    :param popup_guardar:
    :return:
    """
    popup_guardar.destroy()
    imprimir(variables)


def guarda(variables, popup_guardar, elobjeto):
    """
    Funcion para altas de nuevos registros
    :param variables:
    :param popup_guardar:
    :param elobjeto: objeto de producto
    :return:
    """
    lista = []
    for variable in variables:
        lista.append(variable.get())
    validar = lista[0]
    if val.validar(validar) is True:
        popup_guardar.destroy()
        TablaProducto.create(titulo=lista[0], descripcion=lista[1])
        elobjeto.set_event("Alta", lista[0])
        elobjeto.mostrar()
    else:
        showerror('Titulo No valido',
                  'El campo de título no cumple los requisitos, ingrese datos alfabéticos')


def guardar(objeto):
    """
    funcion encargada de crear el nuevo popup
    :param objeto: Objeto producto
    :return:
    """
    popup_guardar = Toplevel()
    vars_guardar = crear_form_guardar(popup_guardar, campos)
    Button(popup_guardar, text='Guardar', command=(
        lambda: guarda(vars_guardar, popup_guardar, objeto))).pack()
    popup_guardar.grab_set()
    popup_guardar.focus_set()
    popup_guardar.wait_window()
