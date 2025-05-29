-- Ya está UNIQUE, pero por claridad:
CREATE UNIQUE INDEX idx_cliente_email ON cliente(email);

-- Búsquedas frecuentes por teléfono
CREATE INDEX idx_cliente_telefono ON cliente(telefono);

-- Si se busca por nombre con frecuencia
CREATE INDEX idx_cliente_nombre ON cliente(nombre);

-- Para acelerar ordenamientos por fecha de alta
CREATE INDEX idx_cliente_fecha_alta ON cliente(fecha_alta);

