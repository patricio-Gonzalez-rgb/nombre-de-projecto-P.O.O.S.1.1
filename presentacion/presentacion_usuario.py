from getpass import getpass
from prettytable import PrettyTable

from auxiliares import (mensaje_error, rol_lector, rol_periodista,
                        validar_correo, validar_contrasena)
from negocio import (iniciar_sesion, registrar_usuario, procesar_listado_usuarios,
                     modificar_usuario as negocio_modificar_usuario,
                     deshabilitar_usuario)
from presentacion.entradas import pedir_texto, pedir_id


def iniciar_sesion_usuario():
    email = input('Correo: ')
    contrasena = getpass('Contraseña: ')
    exito, resultado, rol = iniciar_sesion(email, contrasena)
    if exito:
        print(f'\n¡Bienvenido/a {resultado.nombre}!\n')
        return resultado, rol
    print(f'\n{resultado}\n')
    return None, None


def registrar_nuevo_usuario():
    nombre = pedir_texto('Nombre completo: ', 100)

    correo = ''
    while correo == '':
        correo, mensaje = validar_correo(input('Correo electrónico: ').strip())
        if correo == '':
            print(mensaje)

    contrasena = ''
    while contrasena == '':
        contrasena, errores = validar_contrasena(getpass('Contraseña: '))
        for error in errores:
            print(error)

    print('Roles: [1] Lector | [2] Periodista')
    rol = rol_periodista if input('Seleccione rol (1-2): ').strip() == '2' else rol_lector
    biografia = None
    if rol == rol_periodista:
        biografia = pedir_texto('Biografía [o ENTER para omitir]: ', 500, opcional=True)

    _, mensaje = registrar_usuario(nombre, correo, contrasena, rol, biografia)
    print(f'\n{mensaje}\n')


def mostrar_listado_usuarios():
    try:
        print(procesar_listado_usuarios(PrettyTable()))
        print()
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_usuario(usuario_actual, rol_actual):
    id_usuario = pedir_id('Ingrese Id del usuario a actualizar: ')
    if id_usuario is None:
        print('Id inválido.\n')
        return
    nombre = pedir_texto('Nuevo nombre [o ENTER para conservar]: ', 100, opcional=True)
    correo = None
    while correo is None:
        valor = input('Nuevo correo [o ENTER para conservar]: ').strip()
        if valor == '':
            correo = ''
        else:
            correo, mensaje = validar_correo(valor)
            if correo == '':
                print(mensaje)
                correo = None
    _, mensaje = negocio_modificar_usuario(id_usuario, nombre, correo, usuario_actual, rol_actual)
    print(f'\n{mensaje}\n')


def eliminar_usuario(usuario_actual, rol_actual):
    id_usuario = pedir_id('Ingrese Id del usuario a eliminar: ')
    if id_usuario is None:
        print('Id inválido.\n')
        return
    if input('¿Está seguro? (s/n): ').strip().lower() != 's':
        print('Operación cancelada.\n')
        return
    _, mensaje = deshabilitar_usuario(id_usuario, usuario_actual, rol_actual)
    print(f'\n{mensaje}\n')