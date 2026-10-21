from datos.models import Usuario, Periodista, Editor, Lector

class RepositorioUsuario:
    @staticmethod
    def buscar_por_email(email):
        """Busca un usuario por su correo electrónico."""
        try:
            return Usuario.get(Usuario.email == email)
        except Usuario.DoesNotExist:
            return None

    @staticmethod
    def obtener_rol_usuario(usuario):
        """Determina si el usuario es Periodista, Editor o Lector según sus tablas asociadas."""
        if Periodista.select().where(Periodista.id_usuario == usuario.id).exists():
            return "Periodista"
        elif Editor.select().where(Editor.id_usuario == usuario.id).exists():
            return "Editor"
        elif Lector.select().where(Lector.id_usuario == usuario.id).exists():
            return "Lector"
        return "Desconocido"

    @staticmethod
    def obtener_id_periodista(id_usuario):
        """Obtiene el registro de periodista asociado a un usuario si existe."""
        try:
            return Periodista.get(Periodista.id_usuario == id_usuario)
        except Periodista.DoesNotExist:
            return None