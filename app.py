from datos.conexion import database
from presentacion.menu import mostrar_menu_principal

if __name__ == "__main__":
    try:
        # 1. Abrir la conexión con MySQL
        database.connect()
        print("Conexión a la base de datos establecida con éxito.")

        # 2. Iniciar el flujo de la aplicación
        mostrar_menu_principal()

    except Exception as e:
        print(f"Error crítico al conectar o ejecutar la aplicación: {e}")

    finally:
        # 3. Cerrar la conexión si sigue abierta
        if not database.is_closed():
            database.close()
            print("Conexión a la base de datos cerrada.")