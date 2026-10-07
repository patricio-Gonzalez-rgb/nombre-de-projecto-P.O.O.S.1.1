from peewee import MySQLDatabase
from decouple import config

database = MySQLDatabase(
    config('DB_NAME', default='noticias'),
    host=config('DB_HOST', default='localhost'),
    port=config('DB_PORT', default=3306, cast=int),
    user=config('DB_USER', default='patricio'),
    password=config('DB_PASSWORD', default='1234'),
    charset='utf8mb4'
)