class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, curso):
        super().__init__(nombre)  # Llamamos al constructor de Persona
        self.curso = curso
