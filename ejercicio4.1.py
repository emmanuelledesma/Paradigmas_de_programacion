#FiguraGeometrica: Utilizar la clase FiguraGeometrica del ejercicio de
#abstracción y crear un método muestre información específica de la
#figura utilizando polimorfismo. Luego, crear una lista de figuras
#geométricas de diferentes tipos y utilizar el polimorfismo para imprimir
#su información.

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

    def mostrar_informacion(self):
        return f"El Círculo de color {self.color} solicitado tiene un área de {self.calcular_area()} y su perímetro es {self.calcular_perimetro()}."

class Rectangulo(Forma):
    def __init__(self, color, base , altura):
        super().__init__(color, f"Base: {base}, Altura: {altura}")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def mostrar_informacion(self):
        return f"El Rectángulo de color {self.color} solicitado tiene un área de {self.calcular_area()} y su perímetro es {self.calcular_perimetro()}."


formas_geometricas = [Circulo("azul", 10), Rectangulo("verde", 5, 10)]

for forma in formas_geometricas:
    print(forma.mostrar_informacion())

#Code made by Emma Ledesma