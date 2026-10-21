from peewee import MySQLDatabase, OperationalError

# Configuración de conexión con tu usuario 'patricio' y contraseña '1234'
database = MySQLDatabase(
    'noticias',
    user='patricio',
    password='1234',
    host='localhost',
    port=3306,
    charset='utf8mb4'
)

def probar_conexion():
    """Realiza una prueba explícita de conexión a la base de datos."""
    try:
        database.connect()
        print("Conexión exitosa a la base de datos 'noticias' con el usuario patricio.")
        database.close()
    except OperationalError as e:
        print(f"Error al conectar a la base de datos: {e}")

if __name__ == '__main__':
    probar_conexion()