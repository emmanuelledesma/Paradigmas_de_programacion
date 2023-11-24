#Ejercicio realizado en clase Lunes 13/11/2023

#Imagina que estás desarrollando un sistema de gestión para una biblioteca digital.
#Tu tarea es diseñar un conjunto de clases orientadas a objetos que permitan organizar 
#y manipular información sobre libros, autores, géneros y usuarios. Debes crear clases para 
#representar un 'Libro', 'Autor', 'Género' y 'Usuario'. Además, deberás implementar 
#herencia para diferentes tipos de usuarios, como 'Estudiante' y 'Profesor'. 
#Utiliza la composición para manejar relaciones entre libros, autores y géneros, 
#y asegúrate de que el diseño sea flexible y expansible para futuras funcionalidades 
#de la biblioteca digital. Describe las propiedades y métodos esenciales de cada clase 
#y cómo se relacionan entre sí en el contexto de la biblioteca. 
#Aplica al menos un ejemplo de cada pilar de la programación orientada a objetos (POO).

from abc import ABC, abstractmethod


class Libro:
    def __init__ (self, titulo, editorial, año_publicación):
        self.titulo = titulo
        self.editorial = editorial
        self.año_publicación = año_publicación
        self.autor = None
        self.genero = None

## Composición: de la clase específica libro Harry Potter
class HarryPotter(Libro):
    def __init__ (self, titulo, editorial, año_publicación):
        super().__init__(titulo, editorial, año_publicación)
        self.autor = Autor("nombre", "apellido", 1990, "ING")
        self.genero = Género("LITERATURA") 

class Autor:
    def __init__ (self, nombre, apellido, año_nacimiento, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        #atributo privado: encapsulamiento
        self._año_nacimiento = año_nacimiento if self.valido_año_nacimiento(año_nacimiento) else None
        self.nacionalidad = nacionalidad

    ## es un decorador: permite generar una función que pueda ser llamada como si fuera un atributo, actúa como un getter
    @property 
    def año_nacimiento(self):
        return self._año_nacimiento
    
    ## setter
    def valido_año_nacimiento(self, año_nacimiento):
        año_valida = False
        if año_nacimiento < 2020:
            año_valida = True
        return año_valida


class Género:
    LISTA_GENERO = ["TERROR", "LITERATURA", "NOVELA"]
    #atributo privado: encapsulamiento  
    def __init__ (self, genero):
        self._genero = genero if self.genero_valido(genero) else None

    @property
    def genero(self):
        return self._genero
    def genero_valido(self, genero):
        valido_genero = False
        if genero.upper() in self.LISTA_GENERO:
            valido_genero = True
            ## manejo de error, detiene la ejecución
        else: 
            raise ValueError("El genero no existe")
        return valido_genero
    
    ## método de clase que actualiza lista genero
    @classmethod
    def actualizar_genero(cls, nuevo_genero):
        cls.LISTA_GENERO.append(nuevo_genero.upper())


class Usuario(ABC):
    def __init__ (self, id, username):
        self.id = id
        self.username = username

## método abstracto    
    @abstractmethod
    def mostrar_info(self):
        pass

class Estudiante(Usuario):
    def __init__ (self, id, username):
        super().__init__ (id, username)
## Abstracción    
    def mostrar_info(self):
        return f"{self.id}, {self.username}"

## Heredo de Usuario
class Profesor(Usuario):
    def __init__ (self, id, username, catedra):
        super().__init__ (id, username)
        self.catedra = catedra

## Polimorfismo y abstracción
    def mostrar_info(self):
        return f"{self.id}, {self.username}, {self.catedra}"
     
     