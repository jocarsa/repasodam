-- 1. Asegurar que los campos críticos no sean nulos
ALTER TABLE cliente
    ALTER COLUMN nombre SET NOT NULL;

ALTER TABLE cliente
    ALTER COLUMN telefono SET NOT NULL;

ALTER TABLE cliente
    ALTER COLUMN email SET NOT NULL;

-- 2. Asegurar que el correo sea único
ALTER TABLE cliente
    ADD CONSTRAINT email_unico UNIQUE (email);

-- 3. Validación básica de teléfono (solo dígitos, mínimo 9 y máximo 15)
ALTER TABLE cliente
    ADD CONSTRAINT telefono_formato_valido CHECK (
        telefono ~ '^\d{9,15}$'
    );

-- 4. Valor por defecto para la fecha de alta
ALTER TABLE cliente
    ALTER COLUMN fecha_alta SET DEFAULT CURRENT_DATE;
