import ast
archivo = open("agenda.txt", "r")

lineas = archivo.readlines()
for linea in lineas:
    tupla = ast.literal_eval(linea)
    print(tupla)
archivo.close()