#Animal: Utilizar la clase Animal del ejercicio de herencia y aplicar
#polimorfismo para realizar el sonido característico del animal. Luego,
#crear una lista de animales de diferentes tipos y utilizar el polimorfismo
#para hacer que emiten sus sonidos.

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

    @abc.abstractmethod
    def emitir_sonido(self):
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

    def emitir_sonido(self):
        return "Ladrido = ¡Guau!"

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
    
    def emitir_sonido(self):
        return "Maullido: ¡Miau!"

class Pajaro(Animal):
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def alimento(self):
        return f"Semillas"
    
    def actividad(self):
        return f"Volar"  

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Alimento: " + self.alimento() +   f", Actividad: " + self.actividad()

    def emitir_sonido(self):
        return "Graznido = ¡Arc Arc Arc!"

animales = [Perro("Toby", 5), Gato("Michi", 7), Pajaro("Raven", 1)]

for animal in animales:
    print(animal.mostrar_info())
    print(animal.emitir_sonido())

#Code made by Emma Ledesma    