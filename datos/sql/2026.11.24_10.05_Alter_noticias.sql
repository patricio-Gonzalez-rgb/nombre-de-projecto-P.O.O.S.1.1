USE noticias;

ALTER TABLE usuario
    ADD COLUMN habilitado TINYINT(1) NOT NULL DEFAULT 1;

ALTER TABLE noticia
    MODIFY estado ENUM('Borrador','EnRevision','Aprobado','Publicado','Rechazado','Archivado')
    NOT NULL DEFAULT 'Borrador';
