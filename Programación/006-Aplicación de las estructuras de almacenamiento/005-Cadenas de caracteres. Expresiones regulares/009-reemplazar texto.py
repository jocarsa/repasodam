import re
texto = "La fecha es 2025-05-28"
nuevo = re.sub(r"\d{4}-\d{2}-\d{2}", "XXXX-XX-XX", texto)
print(nuevo)  # La fecha es XXXX-XX-XX