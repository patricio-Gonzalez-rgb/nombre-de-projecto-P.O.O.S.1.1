from datos.models import Noticia

class RepositorioNoticia:
    @staticmethod
    def listar_noticias():
        """Devuelve todas las noticias registradas en la base de datos."""
        return Noticia.select()

    @staticmethod
    def crear_noticia(titulo, contenido, id_periodista, id_editor=None):
        """Inserta una nueva noticia asociada al ID del periodista."""
        return Noticia.create(
            titulo=titulo,
            contenido=contenido,
            id_periodista=id_periodista,
            id_editor=id_editor,
            estado="Borrador"
        )