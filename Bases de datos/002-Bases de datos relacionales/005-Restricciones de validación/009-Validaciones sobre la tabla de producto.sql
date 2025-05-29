-- 1. Asegurar que el precio no sea nulo ni negativo
ALTER TABLE producto
    ALTER COLUMN precio SET NOT NULL;

ALTER TABLE producto
    ADD CONSTRAINT precio_no_negativo CHECK (precio >= 0);

-- 2. Establecer valor por defecto para la fecha de creación
ALTER TABLE producto
    ALTER COLUMN creado_el SET DEFAULT CURRENT_TIMESTAMP;

-- 3. (Opcional) Validar que el JSON sea un objeto (no un array, número, etc.)
ALTER TABLE producto
    ADD CONSTRAINT datos_extra_objeto CHECK (
        jsonb_typeof(datos_extra) = 'object'
    );

-- 4. (Opcional) Limitar número de etiquetas a 10 (por ejemplo)
ALTER TABLE producto
    ADD CONSTRAINT max_etiquetas CHECK (
        etiquetas IS NULL OR array_length(etiquetas, 1) <= 10
    );

