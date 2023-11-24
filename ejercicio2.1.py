#Animal: Utilizar las clases Animal, Perro, Gato y Pájaro. Se debe incluir
#atributos como nombre y edad. Las subclases deben heredar y definir
#métodos y atributos relacionados con el comportamiento y
#características de cada tipo de animal.

import abc

class Animal(abc.ABC):

    @abc.abstractmethod
    def alimento(self):
        pass 

    @abc.abstractmethod
    def actividad(self):
        pass

    @abc.abstractmethod
    def mostrar_info(self):
        pass

class Perro(Animal):
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def alimento(self):
        return f"Hueso"
    
    def actividad(self):
        return f"Pasear"
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Alimento: " + self.alimento() +  f", Actividad: " + self.actividad()
    
class Gato(Animal):
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def alimento(self):
        return f"Pescado"
    
    def actividad(self):
        return f"Dormir" 

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Alimento: " + self.alimento() +  f", Actividad: " + self.actividad()  
    
class Pajaro(Animal):
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def alimento(self):
        return f"Semillas"
    
    def actividad(self):
        return f"Cantar"  

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Alimento: " + self.alimento() +   f", Actividad: " + self.actividad()
    
perro = Perro("Toby", 5)
gato = Gato("Michi", 7)
pajaro = Pajaro("Piolin", 1)

print(perro.mostrar_info())
print(gato.mostrar_info())
print(pajaro.mostrar_info())            

#Code made by Emma Ledesma