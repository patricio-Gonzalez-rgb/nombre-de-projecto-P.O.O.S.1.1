from prettytable import PrettyTable

from datos.repositorio.repositorio_usuario import RepositorioUsuario
from auxiliares import mensaje_error, rol_lector, rol_editor


def puede_gestionar_usuarios(rol):
    return rol == rol_editor


def registrar_usuario(nombre, email, contrasena, rol=rol_lector, biografia=None, nivel=None):
    try:
        email = email.strip().lower()
        if RepositorioUsuario.buscar_por_email(email):
            return False, 'El correo electrónico ya está registrado.'
        usuario = RepositorioUsuario.crear_usuario(
            nombre.strip().title(), email, contrasena, rol, biografia, nivel)
        return True, f"Usuario '{usuario.nombre}' registrado con éxito como {rol}."
    except Exception as error:
        return False, f'{mensaje_error}{error}'


def iniciar_sesion(email, contrasena):
    """Siempre devuelve (exito, usuario o mensaje, rol)."""
    try:
        usuario = RepositorioUsuario.buscar_por_email(email.strip().lower())
        if not usuario or not usuario.habilitado or usuario.contrasena != contrasena:
            return False, 'Correo o contraseña incorrectos.', None
        return True, usuario, RepositorioUsuario.obtener_rol_usuario(usuario)
    except Exception as error:
        return False, f'{mensaje_error}{error}', None


def procesar_listado_usuarios(tabla: PrettyTable):
    tabla.field_names = ['Id', 'Nombre', 'Correo', 'Rol']
    try:
        for usuario in RepositorioUsuario.listar_usuarios():
            tabla.add_row([
                usuario.id,
                usuario.nombre,
                usuario.email,
                RepositorioUsuario.obtener_rol_usuario(usuario)
            ])
    except Exception as error:
        print(f'{mensaje_error}{error}')
    return tabla


def modificar_usuario(id_usuario, nombre, email, usuario_actual, rol_actual):
    try:
        if not puede_gestionar_usuarios(rol_actual):
            return False, 'Solo un Editor puede modificar usuarios.'
        usuario = RepositorioUsuario.buscar_por_id(id_usuario)
        if not usuario or not usuario.habilitado:
            return False, 'No existe un usuario habilitado con ese Id.'
        if email != '' and email.lower() != usuario.email:
            if RepositorioUsuario.buscar_por_email(email.lower()):
                return False, 'El correo electrónico ya está registrado.'
            usuario.email = email.lower()
        if nombre != '' and nombre.title() != usuario.nombre:
            usuario.nombre = nombre.title()
        RepositorioUsuario.guardar_usuario(usuario)
        return True, 'Usuario actualizado con éxito.'
    except Exception as error:
        return False, f'{mensaje_error}{error}'


def deshabilitar_usuario(id_usuario, usuario_actual, rol_actual):
    try:
        if not puede_gestionar_usuarios(rol_actual):
            return False, 'Solo un Editor puede eliminar usuarios.'
        if id_usuario == usuario_actual.id:
            return False, 'No puede eliminar su propio usuario.'
        usuario = RepositorioUsuario.buscar_por_id(id_usuario)
        if not usuario or not usuario.habilitado:
            return False, 'No existe un usuario habilitado con ese Id.'
        usuario.habilitado = 0
        RepositorioUsuario.guardar_usuario(usuario)
        return True, 'Usuario eliminado (deshabilitado) con éxito.'
    except Exception as error:
        return False, f'{mensaje_error}{error}'