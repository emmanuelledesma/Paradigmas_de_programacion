#Estudiante: Implementar la clase Estudiante con atributos como nombre,
#edad y calificaciones. Utilizar el encapsulamiento para proteger los
#datos que deban ser protegidos y proporcionar métodos públicos para
#obtener dichos datos.

class Estudiante:
    def __init__(self, nombre: str, edad: int, calificaciones: int):
        self._nombre = nombre
        self._edad = edad
        self._calificaciones = calificaciones

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def calificaciones(self):
        return self._calificaciones

    def promedio(self):
        return sum(self._calificaciones) / len(self._calificaciones)


estudiante = Estudiante("Pablo Escobedo", 31, [10, 9, 8])

print("El alumno se llama:", estudiante.nombre)
print("La edad del alumno es", estudiante.edad, "años.")
print("Las calificaciones del alumno son:", estudiante.calificaciones)
print("El promedio del alumno es:", estudiante.promedio())

#Code made by Emma Ledesma

