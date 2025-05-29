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
    def getEdad(self):
        return self.__edad
    def setEdad(self, edad):
        if edad == self.__edad + 1:
            self.__edad = edad
        else:
            print("Error: La edad solo puede incrementarse en 1 año.")

persona = Persona("Jose Vicente",47)
print(persona.getEdad())
persona.setEdad(50)
print(persona.getEdad())
