from abc import ABC, abstractmethod

class Reproductor(ABC):
    @abstractmethod
    def reproducir(self):
        pass

    @abstractmethod
    def pausar(self):
        pass

class MP3(Reproductor):
    def reproducir(self):
        print("Reproduciendo MP3")

    def pausar(self):
        print("Pausa en MP3")

class CD(Reproductor):
    def reproducir(self):
        print("Reproduciendo CD")

    def pausar(self):
        print("Pausa en CD")

def iniciar_reproduccion(reproductor: Reproductor):
    reproductor.reproducir()
    reproductor.pausar()

mp3 = MP3()
cd = CD()

iniciar_reproduccion(mp3)
iniciar_reproduccion(cd)