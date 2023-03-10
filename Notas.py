from Estudiantes import Estudiantes
from Materias import Materias

class Notas(Estudiantes, Materias):
    def __init__(self, nombre, edad, genero, matricula, nombre_materia, codigo_materia, nota_laboratorio, nota_parcial):
        Estudiantes.__init__(self, nombre, edad, genero, matricula)
        Materias.__init__(self, nombre_materia, codigo_materia)
        self.nota_laboratorio = nota_laboratorio
        self.nota_parcial = nota_parcial
        
    def promedio(self):
        prom = (self.nota_laboratorio + self.nota_parcial) / 2
        return prom
    
    def mostrar_notas(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Género: ", self.genero)
        print("Código de Estudiante: ", self.matricula)
        print("Materia: ", self.nombre_materia)
        print("Código: ", self.codigo_materia)
        print("Nota de laboratorio: ", self.nota_laboratorio)
        print("Nota de parcial: ", self.nota_parcial)
        print("Promedio: ", self.promedio())

estudiante1 = Notas("Juan Pérez", 20, "Masculino", "U20200401", "Programación Orientada a Objetos", "POO-101", 8.5, 9.0)
estudiante1.mostrar_notas()