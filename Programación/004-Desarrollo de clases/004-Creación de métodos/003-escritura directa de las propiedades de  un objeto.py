class Persona:
    def __init__(self,nombre=None, edad=None):
        self.nombre = nombre
        self.edad = edad
        self.apellidos = None
        self.altura = None
        self.peso = None
    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
    def despedirse(self):
        return f"Adiós, me despido de ti."

persona = Persona("Jose Vicente",47)
print(persona.nombre)
persona.nombre = "Juan"
print(persona.nombre)