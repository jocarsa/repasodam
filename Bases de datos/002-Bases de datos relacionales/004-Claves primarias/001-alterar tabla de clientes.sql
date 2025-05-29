ALTER TABLE cliente
    ADD PRIMARY KEY (id_cliente);

ALTER TABLE cliente
    ALTER COLUMN id_cliente SET DEFAULT nextval('cliente_id_seq');
