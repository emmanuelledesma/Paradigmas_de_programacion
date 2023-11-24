#Forma: Implementar las clases Forma, Circulo y Rectangulo. La o las
#clases deben contener atributos como color y dimensiones. Las
#subclases deben heredar y definir métodos y atributos para calcular el
#área y el perímetro de cada forma.

import math

class Forma:
    def __init__(self, color: str, dimensiones):
        self.color = color
        self.dimensiones = dimensiones

class Circulo(Forma):
    def __init__(self, color, radio):
        super().__init__(color, f"Radio: {radio}")
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(Forma):
    def __init__(self, color, base , altura):
        super().__init__(color, f"Base: {base}, Altura: {altura}")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
circulo = Circulo("azul", 10)
print(f"El Círculo de color {circulo.color} solicitado tiene un área de {circulo.calcular_area()} y su perímetro es {circulo.calcular_perimetro()}.")

rectangulo = Rectangulo("verde", 5, 10)
print(f"El Rectángulo de color {rectangulo.color} solicitado tiene un área de {rectangulo.calcular_area()} y su perímetro es {rectangulo.calcular_perimetro()}.")

#Code made by Emma Ledesma