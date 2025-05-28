class CuentaAhorro(Cuenta):
    # Constructor con parámetros adicionales específicos de ahorro
    def __init__(self, titular, saldo=0, interes=0.02):
        super().__init__(titular, saldo) 
        self.__interes = interes  # Atributo para la tasa de interés


    @property
    def interes(self):
        return self.__interes
    
    # Método para calcular el interés generado del saldo de la cuenta
    def calcular_interes(self):
        return self.saldo * self.__interes  
    
    # Sobreescritura del método para mostrar detalles
    def imprimir_detalles(self):
        super().imprimir_detalles()  
        print(f"Tipo de cuenta: Ahorro")  
        print(f"Tasa de interés: {self.__interes*100}%")  # Mostrar tasa en porcentaje
