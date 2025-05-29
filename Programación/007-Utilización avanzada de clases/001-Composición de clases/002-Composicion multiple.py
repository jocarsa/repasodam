class Rueda:
    def girar(self):
        print("La rueda está girando.")

class Coche:
    def __init__(self):
        self.ruedas = [Rueda() for _ in range(4)]

    def avanzar(self):
        print("El coche avanza.")
        for rueda in self.ruedas:
            rueda.girar()

# Uso
c = Coche()
c.avanzar()
