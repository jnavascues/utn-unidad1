from tkinter import *
from modificar import *
from base_datos import *

def show(variables, popupModificar):
    popupModificar.destroy()
    imprimir(variables)
    print(type(variables))


def modifica(variables, popupModificar, elobjeto):
    lista = []
    for variable in variables:
        lista.append(variable.get())
    validar = lista[1]
    if (val.validar(validar)==True):
        popupModificar.destroy()
        print(lista)
        print(lista[0])
        print(lista[1])
        elid = lista[0]
        tit =lista[1]
        desc =lista[2]
        actualizar = TablaProducto.update(titulo = tit, descripcion = desc).where(TablaProducto.id == elid)
        actualizar.execute()
        print("-------objeto----------------------------")
        elobjeto.mostrar()
    else:
        showerror('Titulo No valido', 'El campo de título no cumple los requisitos, ingrese datos alfabéticos')

def modificar(objeto):
    print("------- ver objeto -----------")
    print(objeto)
    print("------- visto objeto -----------")
    popupModificar = Toplevel()
    vars_modificar = CrearFormModificar(popupModificar, campos)
    print(vars_modificar)
    Button(popupModificar, text='OK', command=(lambda: show(vars_modificar, popupModificar))).pack()
    Button(popupModificar, text='modificar', command=(lambda: modifica(vars_modificar, popupModificar, objeto))).pack()

    popupModificar.grab_set()
    popupModificar.focus_set()
    popupModificar.wait_window()