CREATE TABLE cliente (
    id_cliente        INTEGER,              -- ID numérico (entero)
    nombre            VARCHAR(100),         -- Texto variable
    direccion         TEXT,                 -- Texto largo
    telefono          VARCHAR(15),          -- Texto para números de teléfono
    email             VARCHAR(100),         -- Correo electrónico
    fecha_alta        DATE                  -- Fecha de alta (solo fecha)
);
