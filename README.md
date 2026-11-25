# Sistema de Gestión de Noticias - INACAP

Aplicación de consola en Python con Programación Orientada a Objetos y arquitectura por capas.
Usa el ORM Peewee para persistir en MySQL.

## Estructura del proyecto

```text
.
├── app.py                  # Punto de entrada
├── auxiliares/             # Textos, menús, roles, estados y validaciones
├── presentacion/           # Menús e interacción por consola
├── negocio/                # Reglas de negocio y permisos por rol
└── datos/
    ├── conexion.py         # Conexión MySQL (lee el archivo .env)
    ├── models.py           # Modelos de Peewee
    ├── repositorio/        # Consultas y operaciones de persistencia
    └── sql/                # Creación y carga de datos
```

1. **Presentación:** recibe opciones y datos del usuario y muestra resultados.
2. **Negocio:** valida permisos y coordina las operaciones.
3. **Datos:** modelos, repositorios y conexión con MySQL.

## Roles

| Rol | Puede |
| --- | --- |
| Lector | Ver y leer noticias publicadas |
| Periodista | Lo anterior + crear sus noticias (quedan en Borrador), modificarlas y eliminarlas |
| Editor | Lo anterior + publicar, modificar o eliminar cualquier noticia y gestionar usuarios |

El registro público permite crear Lectores y Periodistas. Los Editores se crean por SQL.
Eliminar es lógico: las noticias pasan a "Archivado" y los usuarios quedan deshabilitados.

## Requisitos

- Python 3.10 o superior
- MySQL Server en ejecución

## Instalación

```powershell
python -m pip install -r requirements.txt
```

## Preparación de MySQL

Ejecuta en MySQL Workbench o phpMyAdmin, en este orden, los scripts de `datos/sql/`:

1. `2026.11.24_10.00_DDL_Noticias.sql`
2. `2026.11.24_10.10_CREATE_USER.sql` (cambia `CAMBIA_ESTA_CLAVE` por tu clave antes de ejecutarlo)
3. `2026.11.24_10.20_Insert_usuarios.sql`

El archivo `2026.11.24_10.05_Alter_noticias.sql` es solo para quien ya tenga la base
creada con una versión anterior (agrega la columna `habilitado` y el estado "Archivado").
Si ejecutas el DDL actual, no es necesario.

La aplicación no debe usar la cuenta `root`.

## Configuración

Crea un archivo `.env` en la raíz del proyecto (está excluido de git, no lo publiques):

```dotenv
db=noticias
host=localhost
port=3306
user=noticias_app
password=<tu_clave_mysql>
```

## Ejecución

```powershell
python app.py
```

Usuarios de demostración (del script de inserts):

| Rol | Correo | Contraseña |
| --- | --- | --- |
| Editor | editor@noticias.cl | Editor#2026 |
| Periodista | periodista@noticias.cl | Periodista#2026 |
| Lector | lector@noticias.cl | Lector#2026 |

## Convenciones

- Cada función o clase va en el módulo de su responsabilidad.
- Sin consultas a la base de datos en la capa de presentación.
- Sin contraseñas ni credenciales en el código.