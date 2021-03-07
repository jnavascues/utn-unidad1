from peewee import CharField, TextField, SqliteDatabase, Model
from tkinter.messagebox import showinfo

# ###########################################
try:
    db = SqliteDatabase('baseprueba3.db')

    class BaseModel(Model):
        """
        clase Base para peewee
        """
        class Meta:
            database = db

    class TablaProducto(BaseModel):
        """
        clase para la creacion de tabla productos
        Tabla Productos
        Titulo: titulo del producto
        descripcion: descrip. del producto
        """
        titulo = CharField()
        descripcion = TextField()

    class TablaRegistros(BaseModel):
        """
        clase para la creacion de tabla registros de logs
        Tabla registros
        timestamp: fecha
        event: tipo de evento (alta,baja,modificacion)
        titulo: titulo del producto afectado, en caso de baja ID afectado
        """
        timestamp = CharField()
        event = CharField()
        titulo = CharField()

    db.create_tables([TablaProducto, TablaRegistros])

    print("Base de datos con tabla creada")
except():
    print("Hubo un error en el ORM, contacte al desarrollador")
    showinfo('-', 'Hubo un error en el ORM, contacte al desarrollador')
