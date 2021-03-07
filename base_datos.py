from peewee import CharField, TextField, SqliteDatabase, Model
from tkinter.messagebox import showinfo

# ###########################################
try:
    db = SqliteDatabase('baseprueba3.db')

    class BaseModel(Model):
        class Meta:
            database = db

    class TablaProducto(BaseModel):
        titulo = CharField()
        descripcion = TextField()

    class TablaRegistros(BaseModel):
        timestamp = CharField()
        event = CharField()
        titulo = CharField()

    db.create_tables([TablaProducto, TablaRegistros])

    print("Base de datos con tabla creada")
except():
    print("Hubo un error en el ORM, contacte al desarrollador")
    showinfo('-', 'Hubo un error en el ORM, contacte al desarrollador')
