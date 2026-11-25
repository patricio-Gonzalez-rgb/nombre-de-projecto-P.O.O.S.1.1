USE noticias;

INSERT INTO usuario (nombre, email, contrasena, habilitado) VALUES
('Patricio González', 'editor@noticias.cl',     'Editor#2026',     1),
('Ana Periodista',    'periodista@noticias.cl', 'Periodista#2026', 1),
('Luis Lector',       'lector@noticias.cl',     'Lector#2026',     1);

INSERT INTO editor (id_usuario, nivel)
VALUES ((SELECT id FROM usuario WHERE email = 'editor@noticias.cl'), 'Senior');

INSERT INTO periodista (id_usuario, biografia)
VALUES ((SELECT id FROM usuario WHERE email = 'periodista@noticias.cl'), 'Periodista de demostración');

INSERT INTO lector (id_usuario)
VALUES ((SELECT id FROM usuario WHERE email = 'lector@noticias.cl'));
