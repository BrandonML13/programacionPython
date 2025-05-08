class Madre:
    def __init__(self,valor,tipo):
        self.__valor = valor
        self.__tipo = tipo

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Error: La cantidad a retirar debe ser positiva.")  #Aun falta ajustar el codigo para que funcione bien en retirar 
        if self.__valor - cantidad < 0:
            print("Error: Saldo insuficiente.")
        self.__valor -= cantidad
        print(" Retiro exitoso. Saldo actual: $",self.__valor)
  
    def depositar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
        self.__valor += cantidad
        
    def __str__(self):
        return f"Cuenta tipo: {self.__tipo}, Saldo disponible: ${self.__valor:.2f}"


