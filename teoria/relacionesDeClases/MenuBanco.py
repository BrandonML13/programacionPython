class MenuBanco:
    def __init__(self,banco,opcion=None):
        self.bienvenida = banco
        self.opcion = opcion
    def darBienvenida(self):
        print("Bienvenid@ a su banco de confianza, "+ banco1.bienvenida)
        print()
    def desplegarOpciones(self):
        print("¿Que le gustaria hacer?")
        print("1.- depositar")
        print("2.- retirar")
        self.opcion = input("ingrese el numero de la acción que desea realizar:")
    def realizaAccion(self):
        if self.opcion == "1":
          cuenta1.depositar(float(input()))
        if self.opcion == "2":
           cuenta1.retirar(float(input()))
        else:
          print("opcion no valida por favor vuelva a ingresar un numero valido")
