from tkinter import Tk, Button, Frame, LEFT, YES, X, RIGHT, TOP, StringVar, Entry, Label, SUNKEN

archivo = 'persona'
campos = 'id'


def imprimir(variables):
    for variable in variables:
        print('Input => "%s"' % variable.get())


def crear_form_eliminar(raiz, ):
    formulario = Frame(raiz)
    div1 = Frame(formulario, width=100)
    div2 = Frame(formulario, padx=7, pady=2)
    formulario.pack(fill=X)
    div1.pack(side=LEFT)
    div2.pack(side=RIGHT, expand=YES, fill=X)
    variables = []
    lab = Label(div1, width=10, text="id")
    ent = Entry(div2, width=30, relief=SUNKEN)
    lab.pack(side=TOP)
    ent.pack(side=TOP, fill=X)
    var = StringVar()
    ent.config(textvariable=var)
    var.set('---')
    variables.append(var)
    return variables


if __name__ == '__main__':
    root = Tk()
    vars_elimina = crear_form_eliminar(root,)
    Button(root, text='Imprimir', command=(
        lambda: imprimir(vars_elimina))).pack(side=LEFT)
    Button(root, text='Cerrar', command=(
        lambda: root.destroy())).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: imprimir(vars_elimina)))
    root.mainloop()
