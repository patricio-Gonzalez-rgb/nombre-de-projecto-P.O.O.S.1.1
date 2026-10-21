# nombre-de-projecto-P.O.O.S.1.1
Plataforma de Noticias

# Sistema de Gestión de Noticias - INACAP

Aplicación desarrollada en Python aplicando el paradigma de Programación Orientada a Objetos (POO) y Arquitectura por Capas, utilizando el ORM Peewee para la interacción y persistencia con la base de datos MySQL.

---

## Arquitectura del Proyecto

El sistema aplica el principio de Separación de Responsabilidades estructurándose en 3 capas principales:

1. Capa de Presentación (presentacion/)
   - Maneja la interacción directa con el usuario a través de la consola.
   - menu.py: Muestra las opciones del sistema, recibe las entradas de teclado y presenta las respuestas sin ejecutar lógica de negocio ni consultas directas a la base de datos.

2. Capa de Negocio (negocio/)
   - Contiene la lógica central del sistema y las reglas de negocio.
   - servicio.py: Valida permisos, procesa inicios de sesión y coordinaciones entre entidades. Se comunica con la capa de datos exclusivamente a través de la capa de repositorios.

3. Capa de Datos (datos/)
   - conexion.py: Configura la conexión local hacia el motor MySQL.
   - models.py: Define los modelos ORM de Peewee (Usuario, Periodista, Editor, Lector, Noticia, etc.).
   - repositorio/: Contiene clases desacopladas (repositorio_usuario.py, repositorio_noticia.py) que encapsulan todas las consultas SQL/ORM a la base de datos.
   - sql/: Scripts de migración, inserción de parámetros y scripts DDL.

---

## Conceptos de POO Aplicados

- Encapsulamiento y Módulos: Cada capa oculta sus detalles internos. La presentación desconoce cómo se guardan los datos, y el servicio no maneja entradas directas por teclado.
- Herencia: Los modelos ORM extienden de BaseModel (de Peewee) para compartir configuraciones de conexión y metadatos comunes.
- Abstracción: Los métodos estáticos dentro de la capa repositorio/ abstraen las consultas complejas de base de datos exponiendo solo funciones claras (buscar_por_email, crear_noticia).
- Desacoplamiento (Patrón Repositorio): Separa la lógica de acceso a datos de las reglas de negocio, permitiendo un código mantenible y escalable.

---

## Instrucciones de Ejecución

### 1. Requisitos Previos
- Python 3.10+
- Servidor MySQL activo (WampServer / XAMPP)

### 2. Instalación de Dependencias
Ejecuta en la terminal del proyecto:
```bash
pip install peewee pymysql
