class MenuBanco:
    def __init__(self,banco,opcion=None):
        self.bienvenida = banco
        self.opcion = opcion
    def darBienvenida(self):
        print("Bienvenid@ a su banco de confianza, "+ banco1.bienvenida)
        print()
    def desplegarOpciones(self):
        MenuBanco.estadoCuenta(self)
        print("¿Que le gustaria hacer?")
        print("1.- depositar")
        print("2.- retirar")
        print("3.- salir")
        self.opcion = input("ingrese el numero de la acción que desea realizar:")
    def realizarAccion(self):
        while True:
            self.desplegarOpciones()
          
            if self.opcion == "1":
                MenuBanco.depositar(self)
            elif self.opcion == "2":
                MenuBanco.retirar(self)
            elif self.opcion == "3":
                print()
                print("Gracias por su confianza en Banciencias, vuelva pronto")
                break 
            else :
                print()
                print("opcion no valida por favor vuelva a ingresar un numero valido")
        
    def depositar(self):
          cuenta1.depositar(float(input("Introduzca la cantidad que desea depositar")))

    def retirar(self):
          cuenta1.retirar(float(input("Introduzca la cantidad que desea retirar")))
          
    def estadoCuenta(self):
        print("su saldo actual es de =",cuenta1.saldo)
