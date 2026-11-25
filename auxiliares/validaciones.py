import re


def validar_largo_string(valor, largo):
    valor = valor.strip()
    if valor == '':
        return '', 'El dato no puede quedar vacío, ingrese nuevamente...\n'
    if len(valor) > largo:
        return '', f'Su dato supera los {largo} caracteres permitidos, ingrese nuevamente...\n'
    return valor, 'Dato correcto\n'


def validar_correo(correo):
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron_correo, correo):
        mensaje = 'Formato de correo válido\n'
    else:
        mensaje = 'Correo Inválido, ingrese nuevamente...\n'
        correo = ''
    return correo, mensaje


def validar_contrasena(contrasena):
    errores = []

    if len(contrasena) < 8 or len(contrasena) > 15:
        errores.append('La contraseña debe tener entre 8 y 15 caracteres.')
    if not any(c.isupper() for c in contrasena):
        errores.append('La contraseña debe contener al menos una letra mayúscula.')
    if not any(c.islower() for c in contrasena):
        errores.append('La contraseña debe contener al menos una letra minúscula.')
    if not any(c.isdigit() for c in contrasena):
        errores.append('La contraseña debe contener al menos un número.')
    if not any(c in '!@#$%&/' for c in contrasena):
        errores.append('La contraseña debe contener al menos uno de estos caracteres: ! @ # $ % & /')

    if len(errores) > 0:
        contrasena = ''

    return contrasena, errores