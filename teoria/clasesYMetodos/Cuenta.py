class Cuenta:
    def __init__(self,valor,tipo,nombre):
        self.saldo = valor
        self.tipo = tipo
        self.nombrePropietario = nombre
    def imprimirDetalles(self):
        print("El estado actual de su cuenta es:")
        print("Saldo: ", self.saldo)
        print("tipo: ", self.tipo)
        print("Nombre: " , self.nombrePropietario)
        print()
    def retirar(self,cantidad):
        self.saldo = self.saldo - cantidad
        print("Usted ha hecho un retiro de", cantidad)
        print()
    def depositar(self,cantidad):
        self.saldo = self.saldo + cantidad
        print("Usted ha hecho un deposito de", cantidad)
        print()