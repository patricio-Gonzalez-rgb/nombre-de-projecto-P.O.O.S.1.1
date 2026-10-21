from peewee import MySQLDatabase
from decouple import config

database = MySQLDatabase(
    config('DB_NAME'),
    host=config('DB_HOST'),
    port=config('DB_PORT', cast=int),
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
    charset='utf8mb4'
)