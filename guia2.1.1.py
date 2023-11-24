#1.1. Hacer un decorador para registrar las llamadas a una función, junto con
#sus argumentos y resultados.

def funcion_externa(funcion_parametro):
    def funcion_interna(a, b):
        print('Llamando a la funcion:\n')
        print(f'Parametros: {a}, {b}')
        return funcion_parametro(a, b)
    return funcion_interna

@funcion_externa
def multiplicacion(a, b):
    print(f'Resultado: {str(a * b)}')
    
multiplicacion(12, 13)

#Code Made by Emma Ledesma