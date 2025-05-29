class SerVivo:
    def respirar(self):
        print("Respirando...")

class Animal(SerVivo):
    def moverse(self):
        print("El animal se mueve.")

class Pajaro(Animal):
    def volar(self):
        print("El pájaro vuela.")
