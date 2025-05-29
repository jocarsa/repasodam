from queue import Queue

cola = Queue()
cola.put("tarea1")
cola.put("tarea2")
print(cola.get())  # tarea1