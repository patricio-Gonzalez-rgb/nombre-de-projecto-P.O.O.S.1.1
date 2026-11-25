from datos.models import Noticia, Usuario
from auxiliares import estado_borrador, estado_publicada, estado_archivada


def _con_autor():
    return (Noticia
            .select(Noticia, Usuario.nombre.alias('autor'))
            .join(Usuario, on=(Noticia.id_periodista == Usuario.id))
            .objects())


class RepositorioNoticia:
    @staticmethod
    def listar_publicadas():
        return (_con_autor().where(Noticia.estado == estado_publicada)
                .order_by(Noticia.fecha.desc()))

    @staticmethod
    def listar_gestionables():
        return (_con_autor().where(Noticia.estado != estado_archivada)
                .order_by(Noticia.fecha.desc()))

    @staticmethod
    def obtener_detalle(id_noticia):
        return _con_autor().where(Noticia.id == id_noticia).first()

    @staticmethod
    def buscar_por_id(id_noticia):
        return Noticia.get_or_none(Noticia.id == id_noticia)

    @staticmethod
    def crear_noticia(titulo, contenido, id_periodista):
        return Noticia.create(titulo=titulo, contenido=contenido,
                              id_periodista=id_periodista, estado=estado_borrador)

    @staticmethod
    def guardar_noticia(noticia):
        return noticia.save()