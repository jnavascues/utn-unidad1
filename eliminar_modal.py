from tkinter import Toplevel, Button
from eliminar import imprimir, crear_form_eliminar, campos
from base_datos import TablaProducto


def show(variables, popup_eliminar):
    popup_eliminar.destroy()
    imprimir(variables)


def elimina(variables, popup_eliminar, elobjeto):
    popup_eliminar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
    temp_product = TablaProducto.get(TablaProducto.id == lista[0])
    temp_product.delete_instance()
    elobjeto.set_event("IDBaja", lista[0])
    elobjeto.mostrar()


def eliminar(objeto):
    popup_eliminar = Toplevel()
    vars_eliminar = crear_form_eliminar(popup_eliminar, campos)
    Button(popup_eliminar, text='Eliminar', command=(
        lambda: elimina(vars_eliminar, popup_eliminar, objeto))).pack()
    popup_eliminar.grab_set()
    popup_eliminar.focus_set()
    popup_eliminar.wait_window()
