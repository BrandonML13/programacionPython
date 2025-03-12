class Cuenta:
    def __init__(self,valor,tipo):
        self.saldo = valor
        self.tipo = tipo
  
    def imprimirDetalles(self):
        print("Saldo: ", self.saldo)
        print("Tarjeta tipo: ", self.tipo)
       

    def retirar(self,cantidad):
        self.saldo = self.saldo - cantidad
        
    def depositar(self,cantidad):
        self.saldo = self.saldo + cantidad
        
