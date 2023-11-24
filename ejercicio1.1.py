#Ejercicio 1.1
#FiguraGeometrica: Utilizar clases FiguraGeometrica, Circulo, Rectangulo
#y Triangulo y que contenga métodos y atributos relacionados con el
#cálculo del área y perímetro de una figura geométrica. Definan los
#métodos y atributos necesarios para calcular el área y el perímetro de
#cada tipo de figura utilizando los conceptos de abstracción.

import abc
import math

class Figurageometrica:
    def area(self):
        pass

    def perimetro(self):
        pass

class Circulo(Figurageometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(Figurageometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(Figurageometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
circulo = Circulo(10)
print("El Circulo solicitado tiene un área de ", circulo.area()," y su perímetro es ", circulo.perimetro(),".")

rectangulo = Rectangulo(5, 10)
print("El Rectangulo solicitado tiene un área de ", rectangulo.area()," y su perímetro es ", rectangulo.perimetro(),".")

triangulo = Triangulo(12, 10, 12)
print("El Triangulo solicitado tiene un área de ", triangulo.area()," y su perímetro es ", triangulo.perimetro(),".")

#Code made by Emma Ledesma