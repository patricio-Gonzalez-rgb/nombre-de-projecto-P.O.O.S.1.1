from prettytable import PrettyTable

from auxiliares import mensaje_error
from negocio import (
    procesar_listado_noticias, obtener_noticia_publicada,
    crear_noticia as negocio_crear_noticia,
    modificar_noticia as negocio_modificar_noticia,
    publicar_noticia as negocio_publicar_noticia,
    archivar_noticia)
from presentacion.entradas import pedir_texto, pedir_id


def mostrar_noticias_publicadas():
    try:
        tabla = procesar_listado_noticias(PrettyTable(), solo_publicadas=True)
        if not tabla.rows:
            print('No hay noticias publicadas aún.\n')
            return
        print(tabla)
        id_noticia = pedir_id('\nIngrese Id para leer la noticia [o ENTER para volver]: ')
        if id_noticia is not None:
            noticia = obtener_noticia_publicada(id_noticia)
            if noticia:
                print(f'\n{noticia.titulo}\nPor {noticia.autor}\n')
                print(f'{noticia.contenido}\n')
            else:
                print('No existe una noticia publicada con ese Id.\n')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def mostrar_listado_noticias():
    try:
        tabla = procesar_listado_noticias(PrettyTable(), solo_publicadas=False)
        print(tabla if tabla.rows else 'No hay noticias registradas.')
        print()
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_noticia(usuario, rol):
    titulo = pedir_texto('Título de la noticia: ', 200)
    contenido = pedir_texto('Contenido: ', 5000)
    _, mensaje = negocio_crear_noticia(titulo, contenido, usuario, rol)
    print(f'\n{mensaje}\n')


def modificar_noticia(usuario, rol):
    id_noticia = pedir_id('Ingrese Id de la noticia a actualizar: ')
    if id_noticia is None:
        print('Id inválido.\n')
        return
    titulo = pedir_texto('Nuevo título [o ENTER para conservar]: ', 200, opcional=True)
    contenido = pedir_texto('Nuevo contenido [o ENTER para conservar]: ', 5000, opcional=True)
    _, mensaje = negocio_modificar_noticia(id_noticia, titulo, contenido, usuario, rol)
    print(f'\n{mensaje}\n')


def publicar_noticia(usuario, rol):
    id_noticia = pedir_id('Ingrese Id de la noticia a publicar: ')
    if id_noticia is None:
        print('Id inválido.\n')
        return
    _, mensaje = negocio_publicar_noticia(id_noticia, usuario, rol)
    print(f'\n{mensaje}\n')


def eliminar_noticia(usuario, rol):
    id_noticia = pedir_id('Ingrese Id de la noticia a eliminar: ')
    if id_noticia is None:
        print('Id inválido.\n')
        return
    if input('¿Está seguro? (s/n): ').strip().lower() != 's':
        print('Operación cancelada.\n')
        return
    _, mensaje = archivar_noticia(id_noticia, usuario, rol)
    print(f'\n{mensaje}\n')