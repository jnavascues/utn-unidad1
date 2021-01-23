from peewee import *
from tkinter.messagebox import *

# ###########################################
try:
    db = SqliteDatabase('baseprueba3.db')
    
    class BaseModel(Model):
        class Meta:
            database = db
    class TablaProducto(BaseModel):
        titulo = CharField()
        descripcion = TextField()
    db.connect
    db.create_tables([TablaProducto])
    print("Base de datos con tabla creada")
except:
    print("Hubo un error en el ORM, contacte al desarrollador")
    showinfo('-', 'Hubo un error en el ORM, contacte al desarrollador')