from peewee import *
from datos.conexion import database

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Categoria(BaseModel):
    descripcion = CharField(null=True)
    nombre = CharField(max_length=100)

    class Meta:
        table_name = 'categoria'

class Comentario(BaseModel):
    fecha = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id_lector = IntegerField(index=True)
    id_noticia = IntegerField(index=True)
    texto = TextField()

    class Meta:
        table_name = 'comentario'

class Editor(BaseModel):
    id_usuario = IntegerField(primary_key=True)
    nivel = CharField(max_length=50, null=True)

    class Meta:
        table_name = 'editor'

class Etiqueta(BaseModel):
    nombre = CharField(max_length=50)

    class Meta:
        table_name = 'etiqueta'

class Imagen(BaseModel):
    fecha = DateField(null=True)
    id_noticia = IntegerField(index=True)
    url = CharField()

    class Meta:
        table_name = 'imagen'

class Interes(BaseModel):
    fecha_guardado = DateField(null=True)
    id_lector = IntegerField()
    id_noticia = IntegerField(index=True)

    class Meta:
        table_name = 'interes'
        indexes = (
            (('id_lector', 'id_noticia'), True),
        )
        primary_key = CompositeKey('id_lector', 'id_noticia')

class Lector(BaseModel):
    id_usuario = IntegerField(primary_key=True)

    class Meta:
        table_name = 'lector'

class Noticia(BaseModel):
    contenido = TextField()
    estado = CharField(constraints=[SQL("DEFAULT 'Borrador'")], null=True)
    fecha = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id_editor = IntegerField(index=True, null=True)
    id_periodista = IntegerField(index=True)
    titulo = CharField(max_length=200)

    class Meta:
        table_name = 'noticia'

class NoticiaCategoria(BaseModel):
    id_categoria = IntegerField(index=True)
    id_noticia = IntegerField()

    class Meta:
        table_name = 'noticia_categoria'
        indexes = (
            (('id_noticia', 'id_categoria'), True),
        )
        primary_key = CompositeKey('id_noticia', 'id_categoria')

class NoticiaEtiqueta(BaseModel):
    id_etiqueta = IntegerField(index=True)
    id_noticia = IntegerField()

    class Meta:
        table_name = 'noticia_etiqueta'
        indexes = (
            (('id_noticia', 'id_etiqueta'), True),
        )
        primary_key = CompositeKey('id_noticia', 'id_etiqueta')

class Periodista(BaseModel):
    biografia = TextField(null=True)
    id_usuario = IntegerField(primary_key=True)

    class Meta:
        table_name = 'periodista'

class Usuario(BaseModel):
    contrasena = CharField()
    email = CharField(max_length=100, unique=True)
    habilitado = IntegerField(constraints=[SQL("DEFAULT 1")])
    nombre = CharField(max_length=100)

    class Meta:
        table_name = 'usuario'      

