from Categoria import Categoria

class Pelicula(Categoria):
    def __init__(self, nombre, categoria):
        super().__init__(categoria)
        self.nombre = nombre
        self.categoria = categoria
        print(f"La película {self.nombre} pertenece a la categoría {self.categoria}")