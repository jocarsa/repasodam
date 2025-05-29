CREATE TABLE producto (
    id_producto       INTEGER,   -- Clave primaria auto-incremental
    nombre            VARCHAR(100) NOT NULL,
    descripcion       TEXT,
    precio            NUMERIC(10, 2),       -- Decimal con precisión y escala
    disponible        BOOLEAN DEFAULT TRUE, -- Disponible o no
    creado_el         TIMESTAMP,            -- Fecha y hora
    etiquetas         TEXT[],               -- Array de texto
    datos_extra       JSONB,                -- Campo JSON estructurado
    imagen            BYTEA                 -- Datos binarios (imagen)
);
