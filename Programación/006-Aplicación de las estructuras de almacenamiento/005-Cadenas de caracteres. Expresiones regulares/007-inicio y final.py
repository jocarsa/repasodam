import re
texto = "python es genial"
print(bool(re.match("^python", texto)))  # True
print(bool(re.search("genial$", texto)))  # True