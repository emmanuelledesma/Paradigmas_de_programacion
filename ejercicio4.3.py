#Empleado: Utilizar la clase Empleado del ejercicio de herencia y aplicar
#polimorfismo para calcular el salario de acuerdo con las reglas
#específicas de cada tipo de empleado. Luego, crear una lista de
#empleados de diferentes tipos y utilizar el polimorfismo para calcular
#sus salarios.

class Empleado:
    def __init__(self, nombre: str, salario: int, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def fichadeempleado(self):
        return f"IBMer {self.nombre} con el sueldo de {self.salario} del área de {self.departamento}"    

    def calcular_salario(self):
        salario_calculado = self.salario

        if salario_calculado > 750000:
            impuesto = 0.35  
            salario_calculado -= impuesto * (salario_calculado - 750000)

        return salario_calculado

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, personasacargo: int):
        super().__init__(nombre, salario, departamento)
        self.personasacargo = personasacargo

    def fichadeempleado(self):
        return super().fichadeempleado() + f" es Gerente y tiene {self.personasacargo} personas en su equipo."

class Trabajador(Empleado):
    def __init__(self, nombre, salario, departamento, tareas: str):
        super().__init__(nombre, salario, departamento)
        self.tareas = tareas

    def fichadeempleado(self):
        return super().fichadeempleado() + f" que trabaja de {self.tareas}."

def calcular_salarios(empleados):
    for empleado in empleados:
        salario_calculado = empleado.calcular_salario()
        print(f"{empleado.fichadeempleado()} - Siendo su Salario real: {salario_calculado}")


empleados = [
    Gerente("Gabriel Librante", 1000000, "Contabilidad", 12),
    Trabajador("Emmanuel Ledesma", 250000, "Contabilidad", "hacer reconciliaciones y meter asientos"),
]

calcular_salarios(empleados)

#Code made by Emma Ledesma