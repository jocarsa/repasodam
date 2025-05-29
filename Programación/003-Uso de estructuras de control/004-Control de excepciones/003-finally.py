try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Este bloque se ejecuta siempre, independientemente de si hubo una excepción o no.")