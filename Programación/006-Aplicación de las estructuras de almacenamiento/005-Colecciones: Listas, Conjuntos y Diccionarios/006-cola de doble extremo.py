from collections import deque

d = deque()
d.append("izquierda")
d.appendleft("derecha")
print(d)  # deque(['derecha', 'izquierda'])