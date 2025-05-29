class Animal:
    def __init__(self, edad=0, nombre=None):
        self.edad = edad
        self.nombre = nombre

class Persona(Animal):
    def __init__(self, edad=0, nombre=None, apellidos=None):
        super().__init__(edad, nombre)
        self.apellidos = apellidos

class Perro(Animal):
    def __init__(self, edad=0, nombre=None, raza=None):
        super().__init__(edad, nombre)
        self.raza = raza

persona1 = Persona(30, "Jose Vicente", "Carratala")
print(persona1.edad)  # ✅ Ahora funciona correctamente
