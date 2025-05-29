import pickle
frutas = ["manzana", "pera", "naranja", "plátano"]

archivo = open("frutas.dat", "wb")  
pickle.dump(frutas, archivo)  # Serializa la lista de frutas y la escribe en el archivo
archivo.close()  # Cierra el archivo
