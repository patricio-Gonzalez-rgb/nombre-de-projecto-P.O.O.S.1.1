CREATE USER 'noticias_app'@'localhost' IDENTIFIED BY 'CAMBIA_ESTA_CLAVE';
GRANT SELECT, INSERT, UPDATE, DELETE ON noticias.* TO 'noticias_app'@'localhost';
FLUSH PRIVILEGES;
