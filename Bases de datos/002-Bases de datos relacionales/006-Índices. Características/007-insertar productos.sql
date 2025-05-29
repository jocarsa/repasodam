INSERT INTO producto (nombre, descripcion, precio, disponible, creado_el, etiquetas, datos_extra) VALUES
('Teclado mecánico', 'Switches rojos, retroiluminado', 59.99, TRUE,  '2024-01-01 10:00:00',
    ARRAY['teclado', 'gaming'], '{"marca": "RedDragon", "color": "negro"}'),
('Ratón óptico',     'Sensor 16000 DPI',              29.50, TRUE,  '2024-02-15 15:30:00',
    ARRAY['raton', 'ergonomico'], '{"marca": "Logitech", "color": "gris"}'),
('Pantalla 24"',     'Full HD 1080p',                 129.00, FALSE, '2024-03-05 09:00:00',
    ARRAY['monitor', 'oficina'], '{"marca": "Samsung", "color": "negro"}'),
('Alfombrilla XL',   '90x40cm, base antideslizante',   12.00, TRUE,  CURRENT_TIMESTAMP,
    ARRAY['alfombrilla', 'gaming'], '{"marca": "SteelSeries", "color": "negro"}'),
('Auriculares BT',   'Bluetooth 5.0 con micrófono',    44.90, TRUE,  '2024-04-22 18:45:00',
    ARRAY['audio', 'inalambrico'], '{"marca": "Sony", "color": "blanco"}');

