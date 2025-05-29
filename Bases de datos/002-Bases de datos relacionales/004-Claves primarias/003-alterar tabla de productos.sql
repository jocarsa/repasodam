-- 1. Crear la secuencia
CREATE SEQUENCE producto_id_seq
    START WITH 1
    INCREMENT BY 1
    OWNED BY producto.id_producto;

-- 2. Asignar la secuencia como valor por defecto
ALTER TABLE producto
    ALTER COLUMN id_producto SET DEFAULT nextval('producto_id_seq');

-- 3. Añadir la clave primaria
ALTER TABLE producto
    ADD PRIMARY KEY (id_producto);

-- 4. (Opcional) Ajustar la secuencia al máximo ID actual (por si ya hay datos)
SELECT setval('producto_id_seq', COALESCE(MAX(id_producto), 1)) FROM producto;
