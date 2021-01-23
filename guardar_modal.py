from tkinter import *
from guardar import *
from base_datos import *
import val

def show(variables, popupGuardar):
    popupGuardar.destroy()
    imprimir(variables)


def guarda(variables, popupGuardar, elobjeto):
    lista = []
    for variable in variables:
        lista.append(variable.get())
    validar = lista[0]
    if (val.validar(validar)==True):
        popupGuardar.destroy()
        print("guardar------------")
        print("-----base----------------")
        TablaProducto.create(titulo=lista[0],descripcion=lista[1])
        print("-------objeto----------------------------")
        elobjeto.mostrar()
    else:
        showerror('Titulo No valido', 'El campo de título no cumple los requisitos, ingrese datos alfabéticos')



def guardar(objeto):
    print("------- ver objeto -----------")
    print(objeto)
    print("------- visto objeto -----------")
    popupGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popupGuardar, campos)
    
    Button(popupGuardar, text='OK', command=(lambda: show(vars_guardar, popupGuardar))).pack()
    Button(popupGuardar, text='guardar', command=(lambda: guarda(vars_guardar, popupGuardar, objeto))).pack()

    popupGuardar.grab_set()
    popupGuardar.focus_set()
    popupGuardar.wait_window()