def dividir(a, b):
    assert b != 0, "El divisor no puede ser cero"
    return a / b

print(dividir(10, 2))   # OK
print(dividir(10, 0))   # AssertionError
