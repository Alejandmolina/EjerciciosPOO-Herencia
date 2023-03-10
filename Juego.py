class Juego:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def jugar(self):
        print(f"Comenzando juego entre {self.jugador1.nombre} y {self.jugador2.nombre}...")

        jugador_actual = self.jugador1
        jugador_siguiente = self.jugador2

        while True:
            # El jugador actual lanza un golpe al otro jugador
            jugador_siguiente.vida -= 30
            print(f"{jugador_actual.nombre} lanza un golpe a {jugador_siguiente.nombre}! Ahora {jugador_siguiente.nombre} tiene {jugador_siguiente.vida}% de vida.")

            # Si el jugador siguiente se queda sin vida, el juego termina
            if jugador_siguiente.vida <= 0:
                print(f"{jugador_siguiente.nombre} ha sido derrotado. {jugador_actual.nombre} es el ganador!")
                break

            # Cambiar de jugador para el siguiente turno
            jugador_actual, jugador_siguiente = jugador_siguiente, jugador_actual
