#Hacer un decorador para verificar que los argumentos de una función
#sean del tipo correcto.

def verificar_tipos(*tipos):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for arg, tipo in zip(args, tipos):
                if not isinstance(arg, tipo):
                    raise TypeError(f"El argumento {arg} no es del tipo {tipo.__name__}")
            
            for clave, valor in kwargs.items():
                if clave in tipos and not isinstance(valor, tipos[clave]):
                    raise TypeError(f"El argumento {clave}={valor} no es del tipo {tipos[clave].__name__}")

            resultado = func(*args, **kwargs)
            return resultado

        return wrapper
    return decorador


@verificar_tipos(int, int)
def producto(a, b):
    resultado = a * b
    return resultado


resultado_producto = producto("Manzanas", 3)
print(resultado_producto)

#Code made by Emma Ledesma

