CREATE DATABASE IF NOT EXISTS noticias
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE noticias;

CREATE TABLE usuario (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  contrasena VARCHAR(255) NOT NULL,
  habilitado TINYINT(1) NOT NULL DEFAULT 1
);

CREATE TABLE lector (
  id_usuario INT PRIMARY KEY,
  FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

CREATE TABLE periodista (
  id_usuario INT PRIMARY KEY,
  biografia TEXT,
  FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

CREATE TABLE editor (
  id_usuario INT PRIMARY KEY,
  nivel VARCHAR(50),
  FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

CREATE TABLE categoria (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255)
);

CREATE TABLE etiqueta (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL
);

CREATE TABLE noticia (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(200) NOT NULL,
  contenido TEXT NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  estado ENUM('Borrador','EnRevision','Aprobado','Publicado','Rechazado','Archivado')
    NOT NULL DEFAULT 'Borrador',
  id_periodista INT NOT NULL,
  id_editor INT,
  FOREIGN KEY (id_periodista) REFERENCES periodista(id_usuario),
  FOREIGN KEY (id_editor) REFERENCES editor(id_usuario)
);

CREATE TABLE noticia_categoria (
  id_noticia INT,
  id_categoria INT,
  PRIMARY KEY (id_noticia, id_categoria),
  FOREIGN KEY (id_noticia) REFERENCES noticia(id) ON DELETE CASCADE,
  FOREIGN KEY (id_categoria) REFERENCES categoria(id) ON DELETE CASCADE
);

CREATE TABLE noticia_etiqueta (
  id_noticia INT,
  id_etiqueta INT,
  PRIMARY KEY (id_noticia, id_etiqueta),
  FOREIGN KEY (id_noticia) REFERENCES noticia(id) ON DELETE CASCADE,
  FOREIGN KEY (id_etiqueta) REFERENCES etiqueta(id) ON DELETE CASCADE
);

CREATE TABLE imagen (
  id INT AUTO_INCREMENT PRIMARY KEY,
  url VARCHAR(255) NOT NULL,
  fecha DATE,
  id_noticia INT NOT NULL,
  FOREIGN KEY (id_noticia) REFERENCES noticia(id) ON DELETE CASCADE
);

CREATE TABLE comentario (
  id INT AUTO_INCREMENT PRIMARY KEY,
  texto TEXT NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  id_lector INT NOT NULL,
  id_noticia INT NOT NULL,
  FOREIGN KEY (id_lector) REFERENCES lector(id_usuario) ON DELETE CASCADE,
  FOREIGN KEY (id_noticia) REFERENCES noticia(id) ON DELETE CASCADE
);

CREATE TABLE interes (
  id_lector INT,
  id_noticia INT,
  fecha_guardado DATE,
  PRIMARY KEY (id_lector, id_noticia),
  FOREIGN KEY (id_lector) REFERENCES lector(id_usuario) ON DELETE CASCADE,
  FOREIGN KEY (id_noticia) REFERENCES noticia(id) ON DELETE CASCADE
);
