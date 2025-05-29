import pickle

archivo = open("frutas.dat", "rb")  
frutas = pickle.load(archivo)  # Serializa la lista de frutas y la escribe en el archivo
print(frutas)
archivo.close()  # Cierra el archivo
