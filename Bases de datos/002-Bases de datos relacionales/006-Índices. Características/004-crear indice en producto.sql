-- Búsqueda rápida de productos disponibles
CREATE INDEX idx_producto_disponible ON producto(disponible);

-- Acelerar filtros por precio
CREATE INDEX idx_producto_precio ON producto(precio);

-- Índice GIN para búsquedas en arrays
CREATE INDEX idx_producto_etiquetas ON producto USING GIN (etiquetas);

-- Índice GIN para consultas sobre JSONB
CREATE INDEX idx_producto_datos_extra ON producto USING GIN (datos_extra);

-- Opcional: ordenamiento por fecha de creación
CREATE INDEX idx_producto_creado_el ON producto(creado_el);

