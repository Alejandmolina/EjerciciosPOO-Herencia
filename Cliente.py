from Pelicula import Pelicula

class Cliente(Pelicula):
    def __init__(self, categoria_elegida):
        self.categoria_elegida = categoria_elegida

        # Acción
        if self.categoria_elegida == "Acción":
            print("Películas de acción disponibles:")
            print("1. Misión imposible")
            print("2. John Wick")
            print("3. The Avengers")

        # Comedia
        elif self.categoria_elegida == "Comedia":
            print("Películas de comedia disponibles:")
            print("1. ¿Qué pasó ayer?")
            print("2. La boda de mi mejor amigo")
            print("3. Ted")

        # Terror
        elif self.categoria_elegida == "Terror":
            print("Películas de terror disponibles:")
            print("1. El conjuro")
            print("2. La noche del demonio")
            print("3. El exorcismo de Emily Rose")

        else:
            print(f"No hay películas disponibles para la categoría {self.categoria_elegida}")


cliente = Cliente("Acción")