from datos.models import Usuario, Periodista, Editor, Lector, Noticia, Categoria, Comentario

# --- AUTENTICACIÓN Y USUARIOS ---
def registrar_usuario(nombre, email, contrasena, rol="Lector", biografia=None, nivel=None):
    """Registra un usuario y su perfil específico según el rol."""
    try:
        if Usuario.select().where(Usuario.email == email).exists():
            return False, "El correo electrónico ya está registrado."

        nuevo_usuario = Usuario.create(
            nombre=nombre,
            email=email,
            contrasena=contrasena
        )

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
        usuario = Usuario.get(Usuario.email == email)
        if usuario.contrasena == contrasena:
            if Periodista.select().where(Periodista.id_usuario == usuario).exists():
                rol = "Periodista"
            elif Editor.select().where(Editor.id_usuario == usuario).exists():
                rol = "Editor"
            else:
                rol = "Lector"
            return True, usuario, rol
        else:
            return False, "Contraseña incorrecta.", None
    except Usuario.DoesNotExist:
        return False, "El correo no está registrado.", None

# --- NOTICIAS ---
def listar_noticias_publicadas():
    """Retorna todas las noticias cuyo estado sea 'Publicada'."""
    return Noticia.select().where(Noticia.estado == 'Publicada')

def crear_noticia(titulo, contenido, id_periodista):
    """Crea una nueva noticia en estado 'Borrador'."""
    try:
        Noticia.create(
            titulo=titulo,
            contenido=contenido,
            id_periodista=id_periodista,
            estado='Borrador'
        )
        return True, "Noticia guardada como borrador con éxito."
    except Exception as e:
        return False, f"Error al crear la noticia: {e}"