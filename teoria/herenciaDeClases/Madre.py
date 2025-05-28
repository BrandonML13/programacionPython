# Clase madre para todas las cuentas bancarias
class Cuenta:
    def __init__(self, titular, saldo=0):
        self.__titular = titular 
        self.__saldo = saldo
    
    # Decorador property para tener un codigo màs limpio
    @property
    def titular(self):
        return self.__titular  
    
    
    @property
    def saldo(self):
        return self.__saldo   
    def depositar(self, cantidad):
        if cantidad > 0:  # Validar que la cantidad sea positiva
            self.__saldo += cantidad  # Sumar al saldo actual
            return True  # Indicar éxito en la operación
        return False  # Indicar fallo en la operación
    
    
    def retirar(self, cantidad):
        # Valido que la cantidad sea positiva y que haya saldo suficiente
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad  # Restar del saldo actual
            return True 
        return False  
    
    
    def imprimir_detalles(self):
        print(f"Titular: {self.__titular}") 
        print(f"Saldo: ${self.__saldo:.2f}") 

