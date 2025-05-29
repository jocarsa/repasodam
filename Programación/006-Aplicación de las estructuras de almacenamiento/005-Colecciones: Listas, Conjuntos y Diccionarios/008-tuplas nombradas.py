from collections import namedtuple

Punto = namedtuple("Punto", ["x", "y"])
p = Punto(10, 20)
print(p.x)  # 10