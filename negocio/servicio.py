from datos.repositorio.repositorio_usuario import RepositorioUsuario
from datos.repositorio.repositorio_noticia import RepositorioNoticia
from datos.models import Usuario, Lector, Periodista, Editor

# --- AUTENTICACIÓN Y USUARIOS ---
def registrar_usuario(nombre, email, contrasena, rol="Lector", biografia=None, nivel=None):
    """Registra un usuario y su perfil específico según el rol usando el repositorio."""
    try:
        # Verificar si ya existe usando el repositorio
        usuario_existente = RepositorioUsuario.buscar_por_email(email)
        if usuario_existente:
            return False, "El correo electrónico ya está registrado."

        # Crear el usuario base
        nuevo_usuario = Usuario.create(
            nombre=nombre,
            email=email,
            contrasena=contrasena
        )

        # Crear el perfil según el rol correspondiente
        if rol == "Lector":
            Lector.create(id_usuario=nuevo_usuario)
        elif rol == "Periodista":
            Periodista.create(id_usuario=nuevo_usuario, biografia=biografia)
        elif rol == "Editor":
            Editor.create(id_usuario=nuevo_usuario, nivel=nivel)

        return True, f"Usuario '{nombre}' registrado con éxito como {rol}."
    except Exception as e:
        return False, f"Error al registrar usuario: {e}"

def iniciar_sesion(email, contrasena):
    """Verifica las credenciales y devuelve el usuario con su rol."""
    try:
        usuario = RepositorioUsuario.buscar_por_email(email)
        if not usuario:
            return False, "El correo no está registrado.", None

        if usuario.contrasena == contrasena:
            rol = RepositorioUsuario.obtener_rol_usuario(usuario)
            return True, usuario, rol
        else:
            return False, "Contraseña incorrecta.", None
    except Exception as e:
        return False, f"Error al iniciar sesión: {e}"

# --- NOTICIAS ---
def listar_noticias_publicadas():
    """Retorna todas las noticias publicadas llamando al repositorio."""
    return RepositorioNoticia.listar_noticias()

def crear_noticia(titulo, contenido, usuario_actual):
    """Crea una nueva noticia asegurando que se use el id_periodista correcto."""
    try:
        # Validar si el usuario actual tiene rol de Periodista
        periodista = RepositorioUsuario.obtener_id_periodista(usuario_actual.id)
        if not periodista:
            return False, "El usuario actual no tiene permisos de periodista para crear noticias."

        # Guardar la noticia usando el repositorio de noticias y el ID del periodista real
        RepositorioNoticia.crear_noticia(
            titulo=titulo,
            contenido=contenido,
            id_periodista=periodista.id_usuario
        )
        return True, "Noticia guardada como borrador con éxito."
    except Exception as e:
        return False, f"Error al crear la noticia: {e}"