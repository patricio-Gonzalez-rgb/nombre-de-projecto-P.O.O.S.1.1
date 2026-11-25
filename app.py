from datos.conexion import database
from presentacion import cargar_menu

if __name__ == '__main__':
    try:
        database.connect()
        cargar_menu()
    except Exception as e:
        print(f'Error crítico al conectar o ejecutar la aplicación: {e}')
    finally:
        if not database.is_closed():
            database.close()