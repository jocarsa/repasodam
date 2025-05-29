class Cliente:
    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email

clientes = []
clientes.append(Cliente(1, 'Jose Vicente', 'info@jocarsa.com'))
clientes.append(Cliente(2, 'Maria', 'maria@jocarsa.com'))

