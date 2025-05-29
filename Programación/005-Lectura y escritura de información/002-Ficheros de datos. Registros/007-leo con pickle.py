import pickle

class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

archivo = open("agenda.dat", "rb")  
contactos = pickle.load(archivo)
print(contactos[0].nombre, contactos[0].telefono)  # Imprime el nombre y teléfono del primer contacto
archivo.close()  # Cierra el archivo
