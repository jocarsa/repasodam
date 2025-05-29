class Animal:
    def hablar(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print("El perro dice guau.")

class Gato(Animal):
    def hablar(self):
        print("El gato dice miau.")

animales = [Perro(), Gato(), Animal()]

for animal in animales:
    animal.hablar()  # Polimorfismo: cada uno ejecuta su versión de 'hablar'