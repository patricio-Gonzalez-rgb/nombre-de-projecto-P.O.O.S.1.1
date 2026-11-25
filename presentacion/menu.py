from auxiliares import (
    nombre_app, version_app, mensaje_error_opcion,
    menu_principal, diccionario_menu_principal,
    menu_sesion, diccionario_menu_sesion,
    menu_noticias, diccionario_menu_noticias,
    menu_usuarios, diccionario_menu_usuarios)
from negocio import puede_gestionar_noticias, puede_gestionar_usuarios
from presentacion.presentacion_usuario import (
    iniciar_sesion_usuario, registrar_nuevo_usuario,
    mostrar_listado_usuarios, modificar_usuario, eliminar_usuario)
from presentacion.presentacion_noticia import (
    mostrar_noticias_publicadas, mostrar_listado_noticias,
    crear_noticia, modificar_noticia, publicar_noticia, eliminar_noticia)


def mostrar_menu(titulo, opciones):
    print(titulo)
    print(f'{"=" * len(titulo)}\n')

    for clave, valor in opciones.items():
        print(f'[{clave}] - {valor}')


def cargar_menu_noticias(usuario, rol):
    while True:
        mostrar_menu(menu_noticias, diccionario_menu_noticias)
        opcion = input('Seleccione su opción: ')
        print()

        match opcion:
            case '1':
                mostrar_listado_noticias()
            case '2':
                crear_noticia(usuario, rol)
            case '3':
                modificar_noticia(usuario, rol)
            case '4':
                publicar_noticia(usuario, rol)
            case '5':
                eliminar_noticia(usuario, rol)
            case '0':
                print('Volviendo a Menú Sesión...\n')
                break
            case _:
                print(mensaje_error_opcion)


def cargar_menu_usuarios(usuario, rol):
    while True:
        mostrar_menu(menu_usuarios, diccionario_menu_usuarios)
        opcion = input('Seleccione su opción: ')
        print()

        match opcion:
            case '1':
                mostrar_listado_usuarios()
            case '2':
                modificar_usuario(usuario, rol)
            case '3':
                eliminar_usuario(usuario, rol)
            case '0':
                print('Volviendo a Menú Sesión...\n')
                break
            case _:
                print(mensaje_error_opcion)


def cargar_menu_sesion(usuario, rol):
    while True:
        print(f'Sesión activa: {usuario.nombre} ({rol})\n')
        mostrar_menu(menu_sesion, diccionario_menu_sesion)
        opcion = input('Seleccione su opción: ')
        print()

        match opcion:
            case '1':
                mostrar_noticias_publicadas()
            case '2':
                if puede_gestionar_noticias(rol):
                    cargar_menu_noticias(usuario, rol)
                else:
                    print('Solo Periodistas y Editores gestionan noticias.\n')
            case '3':
                if puede_gestionar_usuarios(rol):
                    cargar_menu_usuarios(usuario, rol)
                else:
                    print('Solo un Editor gestiona usuarios.\n')
            case '0':
                print('Sesión cerrada con éxito.\n')
                break
            case _:
                print(mensaje_error_opcion)


def cargar_menu():
    print(f'\n{nombre_app} - {version_app}')
    print(f'{"=" * (len(nombre_app) + len(version_app) + 3)}\n')

    while True:
        mostrar_menu(menu_principal, diccionario_menu_principal)
        opcion = input('Seleccione su opción: ')
        print()

        match opcion:
            case '1':
                usuario, rol = iniciar_sesion_usuario()
                if usuario:
                    cargar_menu_sesion(usuario, rol)
            case '2':
                registrar_nuevo_usuario()
            case '3':
                mostrar_noticias_publicadas()
            case '0':
                print('Saliendo...')
                break
            case _:
                print(mensaje_error_opcion)