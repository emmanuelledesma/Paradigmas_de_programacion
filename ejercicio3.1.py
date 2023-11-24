#CuentaBancaria: Crear la clase CuentaBancaria con atributos privados y
#públicos para el saldo y titular. Definir métodos para depositar, retirar y
#consultar el saldo de la cuenta.

class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, cantidad: float):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se han depositado {cantidad} pesos en la cuenta. Saldo actual: {self.__saldo}.")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad: float):
        if cantidad > 0 and self.__saldo >= cantidad:
            self.__saldo -= cantidad
            print(f"Se han retirado {cantidad} pesos de la cuenta. Saldo actual: {self.__saldo}.")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que 0.")
        else:
            print("Saldo insuficiente para retirar la cantidad de pesos solicitada.")

    def consultar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.__titular} es: {self.__saldo} pesos.")


cuenta = CuentaBancaria("Leonel Nessi", 1000000)
cuenta.consultar_saldo()
cuenta.depositar(250000)
cuenta.retirar(200000)
cuenta.retirar(2000000)
cuenta.consultar_saldo()

#Code made by Emma Ledesma