class Persona:
    def __init__(self,nombre=None, edad=None):
        self.nombre = nombre
        self.__edad = edad
        self.apellidos = None
        self.altura = None
        self.__peso = 0
    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
    def despedirse(self):
        return f"Adiós, me despido de ti."

persona = Persona("Jose Vicente",47)
print(persona.__edad)