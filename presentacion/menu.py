from negocio.servicio import iniciar_sesion, registrar_usuario, listar_noticias_publicadas, crear_noticia

def mostrar_menu_principal():
    usuario_actual = None
    rol_actual = None

    while True:
        print("\n" + "="*40)
        print("    SISTEMA DE NOTICIAS - INACAP    ")
        print("="*40)
        
        if usuario_actual:
            print(f"Sesión activa: {usuario_actual.nombre} ({rol_actual})")
            print("-" * 40)
            print("1. Ver noticias publicadas")
            if rol_actual in ["Periodista", "Editor"]:
                print("2. Crear nueva noticia")
            print("0. Cerrar sesión")
        else:
            print("1. Iniciar sesión")
            print("2. Registrarse")
            print("3. Ver noticias publicadas (invitado)")
            print("0. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if not usuario_actual:
            if opcion == "1":
                email = input("Correo: ")
                password = input("Contraseña: ")
                exito, res, rol = iniciar_sesion(email, password)
                if exito:
                    usuario_actual = res
                    rol_actual = rol
                    print(f"\n¡Bienvenido/a {usuario_actual.nombre}!")
                else:
                    print(f"\nError: {res}")
            elif opcion == "2":
                nombre = input("Nombre completo: ")
                email = input("Correo electrónico: ")
                password = input("Contraseña: ")
                print("Roles: 1. Lector | 2. Periodista | 3. Editor")
                rol_opc = input("Seleccione rol (1-3): ").strip()
                roles = {"1": "Lector", "2": "Periodista", "3": "Editor"}
                rol = roles.get(rol_opc, "Lector")
                
                biografia = None
                nivel = None
                if rol == "Periodista":
                    biografia = input("Biografía: ")
                elif rol == "Editor":
                    nivel = input("Nivel (Ej: Senior/Junior): ")

                exito, msg = registrar_usuario(nombre, email, password, rol, biografia, nivel)
                print(f"\n{msg}")
            elif opcion == "3":
                noticias = listar_noticias_publicadas()
                print("\n--- NOTICIAS PUBLICADAS ---")
                if not noticias:
                    print("No hay noticias publicadas aún.")
                for n in noticias:
                    print(f"\n[ID: {n.id_noticia}] {n.titulo}")
                    print(f"{n.contenido}")
            elif opcion == "0":
                print("\n¡Hasta luego!")
                break
        else:
            if opcion == "1":
                noticias = listar_noticias_publicadas()
                print("\n--- NOTICIAS PUBLICADAS ---")
                if not noticias:
                    print("No hay noticias publicadas aún.")
                for n in noticias:
                    print(f"\n[ID: {n.id_noticia}] {n.titulo}")
                    print(f"{n.contenido}")
            elif opcion == "2" and rol_actual in ["Periodista", "Editor"]:
                titulo = input("Título de la noticia: ")
                contenido = input("Contenido: ")
                
                # Obtener id de periodista
                id_p = usuario_actual.id
                exito, msg = crear_noticia(titulo, contenido, id_p)
                print(f"\n{msg}")
            elif opcion == "0":
                usuario_actual = None
                rol_actual = None
                print("\nSesión cerrada con éxito.")