from prettytable import PrettyTable

from datos.repositorio.repositorio_noticia import RepositorioNoticia
from auxiliares import (mensaje_error, rol_periodista, rol_editor,
                        estado_publicada, estado_archivada)


def puede_gestionar_noticias(rol):
    return rol in (rol_periodista, rol_editor)


def _tiene_permiso_sobre(noticia, usuario, rol):
    if rol == rol_editor:
        return True
    return rol == rol_periodista and noticia.id_periodista == usuario.id


def procesar_listado_noticias(tabla: PrettyTable, solo_publicadas=True):
    tabla.field_names = ['Id', 'Título', 'Autor', 'Fecha', 'Estado']
    try:
        if solo_publicadas:
            noticias = RepositorioNoticia.listar_publicadas()
        else:
            noticias = RepositorioNoticia.listar_gestionables()
        for noticia in noticias:
            fecha = noticia.fecha.strftime('%d/%m/%Y') if noticia.fecha else ''
            tabla.add_row([noticia.id, noticia.titulo, noticia.autor, fecha, noticia.estado])
    except Exception as error:
        print(f'{mensaje_error}{error}')
    return tabla


def obtener_noticia_publicada(id_noticia):
    try:
        noticia = RepositorioNoticia.obtener_detalle(id_noticia)
        if noticia and noticia.estado == estado_publicada:
            return noticia
    except Exception as error:
        print(f'{mensaje_error}{error}')
    return None


def crear_noticia(titulo, contenido, usuario, rol):
    try:
        if rol != rol_periodista:
            return False, 'Solo un Periodista puede crear noticias.'
        RepositorioNoticia.crear_noticia(titulo, contenido, usuario.id)
        return True, 'Noticia guardada como borrador con éxito.'
    except Exception as error:
        return False, f'{mensaje_error}{error}'


def modificar_noticia(id_noticia, titulo, contenido, usuario, rol):
    try:
        noticia = RepositorioNoticia.buscar_por_id(id_noticia)
        if not noticia or noticia.estado == estado_archivada:
            return False, 'No existe una noticia activa con ese Id.'
        if not _tiene_permiso_sobre(noticia, usuario, rol):
            return False, 'No tiene permisos sobre esta noticia.'
        if titulo != '':
            noticia.titulo = titulo
        if contenido != '':
            noticia.contenido = contenido
        RepositorioNoticia.guardar_noticia(noticia)
        return True, 'Noticia actualizada con éxito.'
    except Exception as error:
        return False, f'{mensaje_error}{error}'


def publicar_noticia(id_noticia, usuario, rol):
    try:
        if rol != rol_editor:
            return False, 'Solo un Editor puede publicar noticias.'
        noticia = RepositorioNoticia.buscar_por_id(id_noticia)
        if not noticia or noticia.estado == estado_archivada:
            return False, 'No existe una noticia activa con ese Id.'
        noticia.estado = estado_publicada
        noticia.id_editor = usuario.id
        RepositorioNoticia.guardar_noticia(noticia)
        return True, 'Noticia publicada con éxito.'
    except Exception as error:
        return False, f'{mensaje_error}{error}'


def archivar_noticia(id_noticia, usuario, rol):
    try:
        noticia = RepositorioNoticia.buscar_por_id(id_noticia)
        if not noticia or noticia.estado == estado_archivada:
            return False, 'No existe una noticia activa con ese Id.'
        if not _tiene_permiso_sobre(noticia, usuario, rol):
            return False, 'No tiene permisos sobre esta noticia.'
        noticia.estado = estado_archivada
        RepositorioNoticia.guardar_noticia(noticia)
        return True, 'Noticia eliminada (archivada) con éxito.'
    except Exception as error:
        return False, f'{mensaje_error}{error}'