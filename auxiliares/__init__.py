from auxiliares.datos_app import (
    nombre_app,
    version_app,
    mensaje_error,
    mensaje_error_opcion,
    rol_lector, rol_periodista, rol_editor,
    estado_borrador, estado_publicada, estado_archivada)
from auxiliares.menu_app import (
    menu_principal, diccionario_menu_principal,
    menu_sesion, diccionario_menu_sesion,
    menu_noticias, diccionario_menu_noticias,
    menu_usuarios, diccionario_menu_usuarios)
from auxiliares.validaciones import (
    validar_largo_string,
    validar_correo,
    validar_contrasena)