from tkinter import Tk, Button, Frame, X, TOP, StringVar, Entry, Label, CENTER, RAISED, W, E, Radiobutton, IntVar
from tkinter.messagebox import showerror, askquestion, showinfo
from datetime import datetime
from tkinter import ttk

from base_datos import TablaProducto, TablaRegistros, db
from temas.opcion_temas import eleccion_tema
from eliminar_modal import eliminar
from modificar_modal import modificar
import val


class DefaultClass:
    """
    Clase default permite agregar observadores a clases hijas
    """
    observadores = []

    def add(self, obj):
        """
        Metodo para registrar Observadores
        :param obj: Objeto Observador
        :return:
        """
        self.observadores.append(obj)

    def notify(self):
        """
        Metodo de notificacion de cambios, notifica a cada observador registrado
        :return:
        """
        for observador in self.observadores:
            observador.update()


class Observer:
    """
    Clase obsevadora padre, handlea si los obsevadores no implementaron el metodo update correctamente
    """
    def update(self):
        raise NotImplementedError("Observador no implementado correctamente.")


class Logueador(Observer):
    """
    Clase observadora
    """
    def __init__(self, obj):
        """
        Contructor
        :param obj: Objeto Producto
        """
        self.logueador = obj
        self.eventdata = None
        self.logueador.add(self)

    def update(self):
        """
        Metodo para registrar un nuevo Log en la tabla registros
        :return:
        """
        self.eventdata = self.logueador.get_event()
        TablaRegistros.create(timestamp=datetime.now(),
                              event=self.eventdata[0], titulo=self.eventdata[1])


class Producto(DefaultClass):
    """
    Clase Productos, Hereda los observadores de la clase Default
    """
    event = None
    titulo = None

    def __init__(self, ventana):
        # base_datos.crearbd()
        # Ventana principal
        self.root = ventana
        self.root.title("Tarea POO")

        titulo = Label(self.root, text="Ingrese sus datos",
                       bg="DarkOrchid3", fg="thistle1", height=1, width=60)
        titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

        Label(self.root, text="Título").grid(row=1, column=0, sticky=W)
        Label(self.root, text="Descripción").grid(row=2, column=0, sticky=W)

        # Defino variables para tomar valores de campos de entrada
        self.a_val, self.b_val = StringVar(), StringVar()
        w_ancho = 20

        self.entrada_nombre = Entry(
            self.root, textvariable=self.a_val, width=w_ancho)
        self.entrada_nombre.grid(row=1, column=1)
        self.entrada_descripcion = Entry(
            self.root, textvariable=self.b_val, width=w_ancho)
        self.entrada_descripcion.grid(row=2, column=1)

        self.tree = ttk.Treeview(height=10, columns=3)
        self.tree["columns"] = ("one", "three")
        self.tree.grid(row=7, column=0, columnspan=3)
        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("one", text='Título', anchor=CENTER)
        self.tree.heading("three", text='Descripción', anchor=CENTER)
        Button(self.root, text="Alta", command=lambda: self.alta()).grid(
            row=6, column=1)

        Button(self.root, text='Eliminar',
               command=lambda: self.pasar_objeto_eliminar()).grid(row=11, column=2)
        Button(self.root, text='Modificar',
               command=lambda: self.pasar_objeto_modificar()).grid(row=11, column=0)

        # #####################################################
        # ################ TEMAS #############3#################
        # #####################################################3
        self.temas_opciones = Frame(
            self.root, bg="red", borderwidth=2, relief=RAISED)
        self.temas_opciones.grid(
            row=12, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)
        ancho_boton = 10
        self.temas = StringVar()
        self.temas.set("tema1")
        # Agrego variables de contorl para eleccion de tema
        self.tema_option = IntVar(value=0)
        Label(self.temas_opciones, borderwidth=4, relief=RAISED,
              text="Temas", bg="#222", fg="OrangeRed",).pack(fill=X)
        temas = ["tema1", "tema2", "tema3"]
        for opcion in temas:
            boton = Radiobutton(self.temas_opciones,
                                text=str(opcion), indicatoron=1, value=int(opcion[-1])-1, variable=self.tema_option,
                                bg="#222", fg="OrangeRed", command=self.bg_fg_option)
            boton["width"] = ancho_boton
            boton.pack(side=TOP)
        # #####################################################
        # ################ FIN DE TEMAS #######################
        # #####################################################

    def pasar_objeto_eliminar(self,):
        """
        Metodo helper para TK
        :return:
        """
        eliminar(self)

    def pasar_objeto_modificar(self,):
        """
        Metodo helper para TK
        :return:
        """
        modificar(self)

    def bg_fg_option(self):
        """
        Metodo para manejo de Temas
        :return:
        """
        self.temas_opciones["bg"] = eleccion_tema(self.tema_option.get())
        self.root["bg"] = eleccion_tema(self.tema_option.get())

    def mostrar(self,):
        """
        Funcion Mostrar, se encarga de Refrescar treeview
        :return:
        """
        # limpieza de tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Consiguiendo datos
        for producto in TablaProducto.select():
            self.tree.insert('', 0, text=producto.id, values=(
                producto.titulo, producto.descripcion))

    def alta(self,):
        """
        Alta para nuevos productos
        :return:
        """
        cadena = self.a_val.get()
        if val.validar(cadena) is True:
            TablaProducto.create(titulo=self.a_val.get(),
                                 descripcion=self.b_val.get())
            self.set_event("Alta", self.a_val.get())
        else:
            showinfo(
                'No Validado', 'El campo de título no cumple los requisitos, ingrese datos alfabéticos')
        self.mostrar()

    def crearbd(self,):
        """
        Metodo para Recrear la DB desde el boton CrearDB(legacy)
        :return:
        """
        try:
            res = askquestion(
                'Recrear BD', 'Si continua todos los productos guardados se perderan')
            if res == 'yes':
                db.drop_tables([TablaProducto])
                db.create_tables([TablaProducto])
                self.mostrar()

        except():
            showerror('Error', 'Error al Eliminar la base de datos.')

    def get_event(self,):
        """
        Metodo para obtener los datos del evento
        :return:
        """
        return self.event, self.titulo

    def set_event(self, event, titulo):
        """
        Metodo para reportar un evento de log
        :param event: Tipo de Evento puede ser Alta,BajaID,Modificacion
        :param titulo: Titulo del producto afectado por el evento, en caso de ser baja se mostrara el ID
        :return:
        """
        self.event = event
        self.titulo = titulo
        self.notify()


if __name__ == '__main__':
    window = Tk()
    application = Producto(window)
    logueador = Logueador(application)
    application.mostrar()
    window.mainloop()
