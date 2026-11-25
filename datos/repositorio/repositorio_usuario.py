from datos.conexion import database
from datos.models import Usuario, Periodista, Editor, Lector
from auxiliares import rol_lector, rol_periodista, rol_editor


class RepositorioUsuario:
    @staticmethod
    def buscar_por_email(email):
        return Usuario.get_or_none(Usuario.email == email)

    @staticmethod
    def buscar_por_id(id_usuario):
        return Usuario.get_or_none(Usuario.id == id_usuario)

    @staticmethod
    def listar_usuarios():
        return Usuario.select().where(Usuario.habilitado == 1).order_by(Usuario.id)

    @staticmethod
    def obtener_rol_usuario(usuario):
        if Periodista.select().where(Periodista.id_usuario == usuario.id).exists():
            return rol_periodista
        if Editor.select().where(Editor.id_usuario == usuario.id).exists():
            return rol_editor
        if Lector.select().where(Lector.id_usuario == usuario.id).exists():
            return rol_lector
        return 'Desconocido'

    @staticmethod
    def crear_usuario(nombre, email, contrasena, rol, biografia=None, nivel=None):
        """Crea el usuario y su perfil de rol en una sola transacción."""
        with database.atomic():
            usuario = Usuario.create(nombre=nombre, email=email,
                                     contrasena=contrasena, habilitado=1)
            if rol == rol_periodista:
                Periodista.create(id_usuario=usuario.id, biografia=biografia)
            elif rol == rol_editor:
                Editor.create(id_usuario=usuario.id, nivel=nivel)
            else:
                Lector.create(id_usuario=usuario.id)
        return usuario

    @staticmethod
    def guardar_usuario(usuario):
        return usuario.save()