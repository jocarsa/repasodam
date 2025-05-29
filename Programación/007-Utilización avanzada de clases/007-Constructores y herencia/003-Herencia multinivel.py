class SerVivo:
    def __init__(self):
        print("Constructor de SerVivo")

class Animal(SerVivo):
    def __init__(self):
        super().__init__()
        print("Constructor de Animal")

class Perro(Animal):
    def __init__(self):
        super().__init__()
        print("Constructor de Perro")

p = Perro()
# Salida:
# Constructor de SerVivo
# Constructor de Animal
# Constructor de Perro
