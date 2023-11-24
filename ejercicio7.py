#Sistema de Geometría 3D
#Diseña un sistema de geometría tridimensional que trabaje con figuras en el
#espacio 3D. Debes implementar las siguientes clases:
#Punto3D: Una clase que representa un punto en el espacio 3D con
#coordenadas x, y, y z.
#Figura3D: Una clase abstracta que representa una figura tridimensional y
#define métodos abstractos para calcular su volumen y área superficial.
#Cubo, Esfera y Cilindro: Subclases de Figura3D que implementan los métodos
#para calcular el volumen y área superficial específicos de cada figura.
#Crea instancias de estas clases y demuestra cómo calcular el volumen y área
#superficial de diferentes figuras tridimensionales.

from abc import ABC, abstractmethod
import math

class Punto3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Punto3D({self.x}, {self.y}, {self.z})"

class Figura3D(ABC):
    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_area_superficial(self):
        pass

class Cubo(Figura3D):
    def __init__(self, punto, lado):
        self.punto = punto
        self.lado = lado

    def calcular_volumen(self):
        return self.lado**3

    def calcular_area_superficial(self):
        return 6 * self.lado**2

class Esfera(Figura3D):
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_volumen(self):
        return (4/3) * math.pi * self.radio**3

    def calcular_area_superficial(self):
        return 4 * math.pi * self.radio**2

class Cilindro(Figura3D):
    def __init__(self, punto_base, radio, altura):
        self.punto_base = punto_base
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return math.pi * self.radio**2 * self.altura

    def calcular_area_superficial(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)


punto = Punto3D(1, 2, 3)
cubo = Cubo(punto, 4)
esfera = Esfera(punto, 3)
cilindro = Cilindro(punto, 2, 5)

print(f"Volumen del Cubo: {cubo.calcular_volumen()}")
print(f"Área Superficial del Cubo: {cubo.calcular_area_superficial()}")

print(f"Volumen de la Esfera: {esfera.calcular_volumen()}")
print(f"Área Superficial de la Esfera: {esfera.calcular_area_superficial()}")

print(f"Volumen del Cilindro: {cilindro.calcular_volumen()}")
print(f"Área Superficial del Cilindro: {cilindro.calcular_area_superficial()}")

#Code made by Emma Ledesma

"""Este código presenta un sistema de geometría tridimensional aplicando (POO). 
Las clases, como Punto3D, Figura3D, Cubo, Esfera y Cilindro, demuestran el uso de herencia y abstracción. 
La clase abstracta Figura3D establece un marco común con métodos abstractos para calcular el volumen 
y área superficial, en las clases concretas. 
Se ve aplicado el polimorfismo en cómo cada figura puede ser tratada en el calulo independiente de su forma.
"""