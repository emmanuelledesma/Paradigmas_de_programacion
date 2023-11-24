#Libro: Crear las clases Libro y Libreria. La clase Libro debe incluir
#atributos como titulo, autor y precio. La clase Libreria debe contener una
#lista de objetos Libro y métodos para calcular el precio total de todos
#los libros en la librería.

import abc

class Libreria(abc.ABC):
    def __init__(self):
        self.listadelibros =[]

@abc.abstractmethod 
def agregas_libro(self, libro: None):
    pass

@abc.abstractmethod
def calcular_precio_total(self):
    pass

class GuardarLibreria(Libreria):
    def agregar_libro(self, libro: None):
        self.listadelibros.append(libro)

    def calcular_precio_total(self):
        precio_total = 0
        for libro in self.listadelibros:
            precio_total += libro.precio
        return precio_total

class Libro():
    def __init__(self, titulo: str, autor:str , precio: float):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

libro1 = Libro("Rayuela","Julio Cortázar", 4999.99)
libro2 = Libro("Drácula","Bram Stoker", 7000)

guardar_libro = GuardarLibreria()
guardar_libro.agregar_libro(libro1)
guardar_libro.agregar_libro(libro2)

print(f"El precio total de los libros en la Libreria es de $: "+ str(guardar_libro.calcular_precio_total()))

#Code made by Emma Ledesma
