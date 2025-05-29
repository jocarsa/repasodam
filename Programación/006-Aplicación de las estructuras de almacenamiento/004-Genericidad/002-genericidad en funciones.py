from typing import TypeVar

T = TypeVar('T')

def devolver_doble(valor: T) -> tuple[T, T]:
    return (valor, valor)

print(devolver_doble("Hola"))   # ('Hola', 'Hola')
print(devolver_doble(5))