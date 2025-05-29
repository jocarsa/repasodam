class Animal:
    def hablar(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print("El perro ladra.")

a = Animal()
a.hablar()     # El animal hace un sonido.

p = Perro()
p.hablar()     # El perro ladra.  ← método sobrescrito
