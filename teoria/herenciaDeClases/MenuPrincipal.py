# Clase para el menú de selección de tipo de cuenta
class MenuTipoCuenta:
    def __init__(self, banco):
        self.__banco = banco  # Nombre del banco (privado)
        self.__cuenta = None  # Cuenta seleccionada (inicialmente None)
    
    # Método para mostrar las opciones del menú
    def mostrar_menu(self):
        print("Bienvenido a Banciencias")  # Mensaje de bienvenida
        print("Seleccione su tipo de cuenta:")  
        print("1. Cuenta de Ahorro")  
        print("2. Cuenta Corriente")  
        print("3. Cuenta de Crédito")  
        print("4. Salir")  
    
    # Método para procesar la selección del usuario
    def seleccionar_cuenta(self):
        while True:  # Bucle infinito hasta selección válida
            self.mostrar_menu()  
            opcion = input("Ingrese su opción: ")  
            
            if opcion == "1":  # Crear cuenta de ahorro
                titular = input("Ingrese su nombre: ")
                saldo = float(input("Ingrese saldo inicial: "))
                self.__cuenta = CuentaAhorro(titular, saldo)
                return self.__cuenta  # Retornar cuenta creada
            
            elif opcion == "2":  # Crear cuenta corriente
                titular = input("Ingrese su nombre: ")
                saldo = float(input("Ingrese saldo inicial: "))
                sobregiro = float(input("Ingrese límite de sobregiro (default $1000): ") or 1000)
                self.__cuenta = CuentaCorriente(titular, saldo, sobregiro)
                return self.__cuenta  # Retornar cuenta creada
            
            elif opcion == "3":  # Crear cuenta de crédito
                titular = input("Ingrese su nombre: ")
                limite = float(input("Ingrese límite de crédito (default $5000): ") or 5000)
                tasa = float(input("Ingrese tasa de interés anual (default 15%): ") or 0.15)
                self.__cuenta = CuentaCredito(titular, limite, tasa)
                return self.__cuenta  # Retornar cuenta creada
            
            elif opcion == "4":  # Salir del programa
                print("Gracias por visitarnos. ¡Hasta pronto!")
                return None  # Retornar None para indicar salida
            
            else:  # Opción no válida
                print("Opción no válida. Intente nuevamente.")








