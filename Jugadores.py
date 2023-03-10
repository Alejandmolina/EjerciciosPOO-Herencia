from Juego import Juego
from Jugador import Jugador

class Jugadores(Jugador):
    def __init__(self, nombre1, nombre2):
        self.jugador1 = Jugador(nombre1)
        self.jugador1.vida = 100
        self.jugador2 = Jugador(nombre2)
        self.jugador2.vida = 100

jugadores = Jugadores("SUPERMAN", "HULK")
juego = Juego(jugadores.jugador1, jugadores.jugador2)
juego.jugar()