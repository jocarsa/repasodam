from typing import final

class Base:
    @final
    def metodo_final(self):
        print("Este método no debería ser sobrescrito.")

class Subclase(Base):
    # def metodo_final(self):  # ⚠️ Esto no lanza error, pero IDEs o mypy lo advertirán
    #     print("Intento de sobrescribir")
    pass
