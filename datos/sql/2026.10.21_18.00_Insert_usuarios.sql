-- 1. Insertar el usuario Patricio en la tabla general de usuarios
INSERT INTO usuarios (rut, nombre, apellido, correo, pais, fecha_nacimiento, genero, fecha_incorporacion, habilitado) VALUES
(
    '12345678-9', 
    'Patricio', 
    'González', 
    'patricio.gonzalez@inacapmail.cl', 
    (SELECT id_pais FROM paises WHERE pais = 'Chile'), 
    '2000-01-01', 
    (SELECT id_parametro FROM parametros WHERE codigo = 'GENERO' AND parametro = 'Masculino' LIMIT 1), 
    CURDATE(), 
    1
);

-- 2. Asignarle el rol de bibliotecario/administrador con la contraseña '1234'
INSERT INTO bibliotecarios (usuario, tipo_usuario, contrasena, habilitado) VALUES
(
    LAST_INSERT_ID(), 
    (SELECT id_parametro FROM parametros WHERE codigo = 'CATLECTOR' AND parametro = 'Avanzado' LIMIT 1), 
    '1234', 
    1
);