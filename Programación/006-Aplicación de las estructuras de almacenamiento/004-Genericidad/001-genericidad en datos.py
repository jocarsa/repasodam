from typing import TypeVar, Generic

T = TypeVar('T')  # T es un tipo genérico

class Caja(Generic[T]):
    def __init__(self, contenido: T):
        self.contenido = contenido

    def obtener(self) -> T:
        return self.contenido
    
caja_texto = Caja[str]("Hola")
print(caja_texto.obtener())  # 'Hola'

caja_numero = Caja 
print(caja_numero.obtener())  # 123