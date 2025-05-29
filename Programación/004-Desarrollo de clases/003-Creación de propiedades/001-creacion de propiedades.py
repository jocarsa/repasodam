class Persona:
    def __init__(self,nombre=None, edad=None):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

persona = Persona("Jose Vicente",47)
persona.saludo = persona.saludar()
print(persona.saludo)