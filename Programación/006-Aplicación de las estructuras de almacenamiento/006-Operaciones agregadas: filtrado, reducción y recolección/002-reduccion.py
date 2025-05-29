from functools import reduce

numeros = [1, 2, 3, 4]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # 10