#Coche: Crear la clase Coche con atributos privados y/o públicos según
#corresponda de velocidad y kilometraje. Definir métodos públicos para
#acelerar y registrar el kilometraje de manera segura.

class Coche:
    def __init__(self, velocidad_inicial=0, kilometraje_inicial=0):
        self.__velocidad = velocidad_inicial
        self.__kilometraje = kilometraje_inicial

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def kilometraje(self):
        return self.__kilometraje

    def contar_kilometros(self):
        self.__kilometraje += self.__velocidad

    def acelerar(self, velocidad):
        if velocidad > 0:
            self.__velocidad += velocidad
            self.contar_kilometros()
            print(f"Acelerando. Nueva velocidad: {self.__velocidad} km/h")
        else:
            print("La cantidad de aceleración debe ser mayor que cero.")

    def registrar_kilometraje(self, distancia):
        if distancia > 0:
            self.__kilometraje += distancia
            print(f"Kilometraje registrado. Nuevo total: {self.__kilometraje} km")
        else:
            print("La distancia registrada debe ser mayor que cero.")


audi = Coche()

audi.acelerar(150)

audi.registrar_kilometraje(175)

print(f"Velocidad actual: {audi.velocidad} km/h")
print(f"Kilometraje total: {audi.kilometraje} km")

#Code made by Emma Ledesma
