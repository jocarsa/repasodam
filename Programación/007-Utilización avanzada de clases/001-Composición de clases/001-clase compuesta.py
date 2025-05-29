class Motor:
    def arrancar(self):
        print("Motor arrancado.")

class Coche:
    def __init__(self):
        self.motor = Motor()  # Composición: el coche tiene un motor

    def encender(self):
        print("Encendiendo el coche...")
        self.motor.arrancar()

# Uso
mi_coche = Coche()
mi_coche.encender()