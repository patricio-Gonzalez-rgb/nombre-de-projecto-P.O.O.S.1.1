from auxiliares import validar_largo_string


def pedir_texto(mensaje, largo, opcional=False):
    """Pide un texto hasta que sea válido. Si es opcional, ENTER devuelve ''."""
    while True:
        valor = input(mensaje)
        if opcional and valor.strip() == '':
            return ''
        valor, mensaje_validacion = validar_largo_string(valor, largo)
        if valor != '':
            return valor
        print(mensaje_validacion)


def pedir_id(mensaje):
    """Devuelve el número ingresado o None si no es un número."""
    valor = input(mensaje).strip()
    return int(valor) if valor.isdigit() else None