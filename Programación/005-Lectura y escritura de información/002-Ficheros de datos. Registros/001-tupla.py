archivo = open("agenda.txt", "w")

contacto = ("Jose Vicente","Carratala","info@josevicentecarratala" "620891718")
cadena = str(contacto)
archivo.write(cadena)

archivo.close()