#Sistema de Gestión de Personal
#Diseña un sistema de gestión de personal para una empresa. Debes
#implementar las siguientes clases:
#Persona: Una clase base que representa a una persona con atributos como
#nombre, edad y DNI. Utiliza el encapsulamiento para proteger los datos
#sensibles.
#Empleado: Una subclase de Persona que agrega atributos como salario y
#cargo. Implementa el cálculo del salario en base al cargo y permite consultar el
#salario.
#Gerente: Una subclase de Empleado que agrega atributos específicos de un
#gerente, como departamento.
#Departamento: Una clase que contiene una lista de empleados y métodos
#para agregar, eliminar y consultar empleados.
#Crea instancias de estas clases y demuestra cómo agregar empleados a un
#departamento, calcular salarios y acceder a la información de las personas.

class Persona:
    def __init__(self, nombre: str, edad: int, dni: str):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def dni(self):
        return self._dni
    
class Empleado(Persona):
    def __init__(self, nombre, edad, dni, salario, cargo):
        super().__init__(nombre, edad, dni)
        self._salario = salario
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario

    @property
    def cargo(self):
        return self._cargo

    def calcular_salario(self):
        salario_calculado = self.salario

        if salario_calculado > 750000:
            impuesto = 0.35  
            salario_calculado -= impuesto * (salario_calculado - 750000)

        return salario_calculado

class Gerente(Empleado):
    def __init__(self, nombre, edad, dni, salario, cargo, departamento):
        super().__init__(nombre, edad, dni, salario, cargo)
        self._departamento = departamento

    @property
    def departamento(self):
        return self._departamento

class Departamento:
    def __init__(self):
        self._empleados = []

    def agregar_empleado(self, empleado):
        self._empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        self._empleados.remove(empleado)

    def consultar_empleados(self):
        return self._empleados

gerente = Gerente("Gabriel Librante", 45, "25.200.345", 1000000, "Gerente", "Contabilidad")
empleado1 = Empleado("Emmanuel Ledesma", 34, "34.600.730", 250000, "Analista Contable")
empleado2 = Empleado("Luca D'Alessandro", 23, "50.345.789", 275000,"Analista Contable" )

accounting = Departamento()

accounting.agregar_empleado(empleado1)
accounting.agregar_empleado(empleado2)

empleados_en_departamento = accounting.consultar_empleados()

accounting.eliminar_empleado(empleado2)

for empleado in empleados_en_departamento:
    print(f"Nombre: {empleado.nombre}, Edad: {empleado.edad}, Cargo: {empleado.cargo}, Salario: {empleado.salario}")

salario_empleado = empleado.calcular_salario()
print(f"El salario de {empleado1.nombre} es: {salario_empleado}")

salario_gerente = gerente.calcular_salario()
print(f"El salario de {gerente.nombre} es: {salario_gerente}")

# Code made by Emma Ledesma

"""Este codigo muestra un sistema de gestion de personal.
Donde las clases principales son Persona, Empleado y Gerente,
y tambien la clase adicional Departamento que administra la lista de empleados.
La clase Persona sirve como la clase padre, con atributos como nombre, edad y DNI. 
Empleado hereda de Persona y agrega detalles como salario y cargo. 
Gerente es una subclase de Empleado con atributos específicos de un gerente, como el departamento que supervisa.
La clase Departamento gestiona empleados y ofrece métodos para agregar, eliminar y consultar empleados.
Se crean instancias de estas clases para representar un gerente, empleados y un departamento. 
Luego, se realizan acciones como agregar empleados, consultar la lista y calcular salarios. 

El código muestra principios de la programación orientada a objetos, 
como la herencia (con las subclases), encapsulamiento (propiedades privadas), y 
polimorfismo (aplicado en el metodo calcular_salario que afecta a las clases si el salario base del empleado
es o no alcanzado por el impuesto a la ganancias que tiene un topo de $750.000.
"""
