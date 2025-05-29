class Animal:
    def comunicarse(self):
        print("El animal se comunica.")

class Mamifero(Animal):
    def amamantar(self):
        print("El mamífero amamanta a sus crías.")

class Perro(Mamifero):
    def comunicarse(self):
        print("El perro ladra.")

a = Animal()
a.comunicarse()  # El animal se comunica.

m = Mamifero()
m.comunicarse()  # Heredado de Animal
m.amamantar()

p = Perro()
p.comunicarse()  # Sobrescribe el método de Animal
p.amamantar()