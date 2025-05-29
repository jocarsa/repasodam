class Persona:
    def __init__(self,nombre=None, edad=None):
        self.nombre = nombre
        self.edad = edad

persona = Persona("Jose Vicente",47)
print(persona)