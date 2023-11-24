#Empleado: Crear las clases Empleado, Gerente y Trabajador. Se debe
#tener atributos como nombre, salario y departamento. Las subclases
#deben heredar y definir los métodos y atributos necesarios para
#representar cada tipo de empleado.

class Empleado:
    def __init__(self, nombre: str, salario: int, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def fichadeempleado(self):
        return f"IBMer {self.nombre} con el sueldo de {self.salario} del área de {self.departamento}"    

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, personasacargo: int):
        super().__init__(nombre, salario, departamento)
        self.personasacargo = personasacargo

    def fichadeempleado(self):
        return super().fichadeempleado() + f" es Gerente y su equipo esta formado por {self.personasacargo} integrantes."

class Trabajador(Empleado):
    def __init__(self, nombre, salario, departamento, tareas: str):
        super().__init__(nombre, salario, departamento)
        self.tareas = tareas

    def fichadeempleado(self):
        return super().fichadeempleado() + f" que trabaja de {self.tareas}."

gerente = Gerente("Gabriel Librante", 1000000, "Contabilidad", 12)
trabajador = Trabajador("Emmanuel Ledesma", 250000, "Contabilidad", "hacer reconciliaciones y meter asientos")

print(gerente.fichadeempleado())
print(trabajador.fichadeempleado())

#Code made by Emma Ledesma
