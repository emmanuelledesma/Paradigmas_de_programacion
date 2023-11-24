#Vehiculo: Implementar las clases Vehiculo, Coche, Motocicleta y
#Bicicleta. La clase Vehiculo debe tener propiedades como marca,
#modelo y velocidad_maxima. Cada subclase debe definir sus métodos y
#atributos específicos relacionados con el comportamiento de cada tipo
#de vehículo.

import abc

class Vehiculo:
    def __init__(self, marca: str, modelo: str, velocidad_maxima: int):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

@property
def marca(self):
    return self.marca

@property
def modelo(self):
    return self.modelo

@property
def velocidad_maxima(self):
    return self.velocidad_maxima

@abc.abstractmethod
def tipodetraccion(self):
    pass

@abc.abstractmethod
def mostrar_info(self):
    pass

class Coche(Vehiculo):
    def tipodetraccion(self):
     return f"Este vehiculo tiene un motor de 4 tiempos."

    def mostrar_info(self):
     return f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad máxima: {self.velocidad_maxima} Km/h"    
    
class Motocicleta(Vehiculo):
    def tipodetraccion(self):
     return f"Este vehiculo tiene un motor de 2 tiempos."

    def mostrar_info(self):
     return f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad máxima: {self.velocidad_maxima} Km/h"    

class Bicicleta(Vehiculo):
    def tipodetraccion(self):
     return f"Este vehiculo no tiene motor, se impulsa a traves de tracción física pedaleando."

    def mostrar_info(self):
     return f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad máxima: {self.velocidad_maxima} km/h"

coche = Coche("Ferrari", "LaFerrari Aperta", 370)
print(coche.mostrar_info())
print(coche.tipodetraccion())

motocicleta = Motocicleta("Honda", "Motocros CRF250R", 135)
print(motocicleta.mostrar_info())
print(motocicleta.tipodetraccion())

bicicleta = Bicicleta("BMC", "BMC 18.8", 75)
print(bicicleta.mostrar_info())
print(bicicleta.tipodetraccion())

#Code made by Emma Ledesma