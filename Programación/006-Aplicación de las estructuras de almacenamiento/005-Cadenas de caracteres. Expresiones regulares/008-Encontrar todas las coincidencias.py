import re
texto = "El número es 123 y el otro es 456"
numeros = re.findall(r"\d+", texto)
print(numeros)  # ['123', '456']