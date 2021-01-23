from tkinter import *
from eliminar import *
from base_datos import *

def show(variables, popupGuardar):
    popupGuardar.destroy()
    imprimir(variables)


def elimina(variables, popupEliminar, elobjeto):
    popupEliminar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
 
    print("-----base----------------")
    temp_product = TablaProducto.get(TablaProducto.id == lista[0])
    temp_product.delete_instance()

    print("Registro borrado")
    print("-------objeto----------------------------")
    elobjeto.mostrar()






    

def eliminar(objeto):
    print("------- ver objeto -----------")
    print(objeto)
    print("------- visto objeto -----------")
    popupEliminar = Toplevel()
    vars_eliminar = CrearFormEliminar(popupEliminar, campos)
    Button(popupEliminar, text='OK', command=(lambda: show(vars_eliminar, popupEliminar))).pack()
    Button(popupEliminar, text='eliminar', command=(lambda: elimina(vars_eliminar, popupEliminar, objeto))).pack()

    popupEliminar.grab_set()
    popupEliminar.focus_set()
    popupEliminar.wait_window()


