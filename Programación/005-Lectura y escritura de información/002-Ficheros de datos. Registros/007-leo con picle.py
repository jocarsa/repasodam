import pickle

class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
contactos = []
contactos.append(Contacto("Juan", "123456789"))
contactos.append(Contacto("Ana", "987654321"))

archivo = open("agenda.dat", "wb")  
pickle.dump(contactos, archivo)  # Serializa la lista de frutas y la escribe en el archivo
archivo.close()  # Cierra el archivo
