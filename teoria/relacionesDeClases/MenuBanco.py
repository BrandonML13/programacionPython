#Las ultimas modificacones del codigo las realice el miercoles confio que me esta quedando bastante bien, lo ultimo que me falta es meter las conexiones logicas
#Para los metodos de depositar y retirar
#Autor: Brandon Martinez Lopez 
class MenuBanco:
    def __init__(self,banco,opcion=None):
        self.__bienvenida = banco
        self.opcion = opcion

    def darBienvenida(self):
        print("Bienvenid@ a su banco de confianza, "+ banco1.__bienvenida)
        print()
    def desplegarOpciones(self):
        MenuBanco.estadoCuenta(self)
        print("¿Que le gustaria hacer?")
        print("1.- Ver detalles de mi cuenta")
        print("2.- depositar")
        print("3.- retirar")
        print("4.- salir")
        self.opcion = input("ingrese el numero de la acción que desea realizar:")

    def realizarAccion(self):
        while True:
            self.desplegarOpciones()
          
            if self.opcion == "1":
                print()
                MenuBanco.imprimirDetalles(self)

            elif self.opcion == "2":
                print()
                MenuBanco.depositar(self)

            elif self.opcion == "3":
                print()
                MenuBanco.retirar(self)
          
            elif self.opcion == "4":
                print()
                print("Gracias por su confianza en Banciencias, vuelva pronto")
                break 
            else :
                print()
                print("opcion no valida por favor vuelva a ingresar un numero valido")
        
    def depositar(self):
          cuenta1.depositar(float(input("Introduzca la cantidad que desea depositar")))
          print("Su deposito se ha realizado con exito")
          print()

    def retirar(self):
          cuenta1.retirar(float(input("Introduzca la cantidad que desea retirar")))
          print("Su retiro se ha realizado con exito")
          print()

    def imprimirDetalles(self):
        cliente1.imprimirDetalles()
          
    def estadoCuenta(self):
        print("su saldo actual es de =",cuenta1.__valor)
    
banco1 = MenuBanco("Banciencias")
