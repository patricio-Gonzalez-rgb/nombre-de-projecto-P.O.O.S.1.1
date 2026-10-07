from peewee import *
from datos.conexion import database

class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    contrasena = CharField(max_length=255)
    email = CharField(max_length=100, unique=True)
    nombre = CharField(max_length=100)

    class Meta:
        table_name = 'usuario'

class Lector(BaseModel):
    id_usuario = ForeignKeyField(column_name='id_usuario', model=Usuario, primary_key=True)

    class Meta:
        table_name = 'lector'

class Periodista(BaseModel):
    id_usuario = ForeignKeyField(column_name='id_usuario', model=Usuario, primary_key=True)
    biografia = TextField(null=True)

    class Meta:
        table_name = 'periodista'

class Editor(BaseModel):
    id_usuario = ForeignKeyField(column_name='id_usuario', model=Usuario, primary_key=True)
    nivel = CharField(max_length=50, null=True)

    class Meta:
        table_name = 'editor'

class Categoria(BaseModel):
    descripcion = CharField(max_length=255, null=True)
    nombre = CharField(max_length=100)

    class Meta:
        table_name = 'categoria'

class Etiqueta(BaseModel):
    nombre = CharField(max_length=50)

    class Meta:
        table_name = 'etiqueta'

class Noticia(BaseModel):
    contenido = TextField()
    estado = CharField(constraints=[SQL("DEFAULT 'Borrador'")], null=True)
    fecha = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id_editor = ForeignKeyField(column_name='id_editor', model=Editor, null=True)
    id_periodista = ForeignKeyField(column_name='id_periodista', model=Periodista)
    titulo = CharField(max_length=200)

    class Meta:
        table_name = 'noticia'

class NoticiaCategoria(BaseModel):
    id_categoria = ForeignKeyField(column_name='id_categoria', model=Categoria)
    id_noticia = ForeignKeyField(column_name='id_noticia', model=Noticia)

    class Meta:
        table_name = 'noticia_categoria'
        indexes = ((('id_noticia', 'id_categoria'), True),)
        primary_key = CompositeKey('id_categoria', 'id_noticia')

class NoticiaEtiqueta(BaseModel):
    id_etiqueta = ForeignKeyField(column_name='id_etiqueta', model=Etiqueta)
    id_noticia = ForeignKeyField(column_name='id_noticia', model=Noticia)

    class Meta:
        table_name = 'noticia_etiqueta'
        indexes = ((('id_noticia', 'id_etiqueta'), True),)
        primary_key = CompositeKey('id_etiqueta', 'id_noticia')

class Imagen(BaseModel):
    fecha = DateField(null=True)
    id_noticia = ForeignKeyField(column_name='id_noticia', model=Noticia)
    url = CharField(max_length=255)

    class Meta:
        table_name = 'imagen'

class Comentario(BaseModel):
    fecha = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id_lector = ForeignKeyField(column_name='id_lector', model=Lector)
    id_noticia = ForeignKeyField(column_name='id_noticia', model=Noticia)
    texto = TextField()

    class Meta:
        table_name = 'comentario'

class Interes(BaseModel):
    fecha_guardado = DateField(null=True)
    id_lector = ForeignKeyField(column_name='id_lector', model=Lector)
    id_noticia = ForeignKeyField(column_name='id_noticia', model=Noticia)

    class Meta:
        table_name = 'interes'
        indexes = ((('id_lector', 'id_noticia'), True),)
        primary_key = CompositeKey('id_lector', 'id_noticia')