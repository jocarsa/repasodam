archivo = open("agenda.txt", "w")

contacto = ("Jose Vicente","Carratala","info@josevicentecarratala","620891718")
cadena = str(contacto)
archivo.write(cadena+"\n")

contacto = ("Juan","Lopez Martinez","info@josevicentecarratala","620891718")
cadena = str(contacto)
archivo.write(cadena+"\n")

archivo.close()