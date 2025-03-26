class Cuenta:
    def __init__(self,valor,tipo):
        self.__valor = valor
        self.__tipo = tipo
  
    def imprimirDetalles(self):
        print("Saldo: ", self.__valor)
        print("Tarjeta tipo: ", self.__tipo)
       

    def retirar(self,cantidad):
        self.__valor = self.__valor - cantidad
        
    def depositar(self,cantidad):
        self.__valor = self.__valor + cantidad

cuenta1 = Cuenta(75300,"Debito")
