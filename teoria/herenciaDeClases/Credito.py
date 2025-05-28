From Madre.py import

class CuentaCredito(Cuenta):
    # Constructor con parámetros específicos de crédito
    def __init__(self, titular, limite_credito=5000, tasa_interes=0.15):
        super().__init__(titular, 0)  # Saldo inicia en 0 (sin fondos propios)
        self.__limite_credito = limite_credito  
        self.__tasa_interes = tasa_interes    
        self.__saldo_disponible = limite_credito  # Crédito disponible
    
    @property
    def limite_credito(self):
        return self.__limite_credito
    
    @property
    def saldo_disponible(self):
        return self.__saldo_disponible
    
    @property
    def tasa_interes(self):
        return self.__tasa_interes
    
    # Sobreescritura del método retirar para usar crédito
    def retirar(self, cantidad):
        # Validar que haya crédito disponible
        if cantidad > 0 and cantidad <= self.__saldo_disponible:
            self._Cuenta__saldo -= cantidad  # Aumenta la deuda se permite saldo negativo
            self.__saldo_disponible -= cantidad  # Reducir crédito disponible
            return True  
        return False  
    
    # Sobreescritura del método depositar para pagar deuda
    def depositar(self, cantidad):
        if cantidad > 0:  
            self._Cuenta__saldo += cantidad  # Reduce la deuda
            # Recalcular crédito disponible (sin exceder el límite)
            self.__saldo_disponible = min(
                self.__limite_credito, 
                self.__saldo_disponible + cantidad
            )
            return True   
        return False   
    
    # Método para calcular interés mensual sobre la deuda
    def calcular_interes_mensual(self):
        if self.saldo < 0:  # Solo si hay deuda
            return abs(self.saldo) * (self.__tasa_interes / 12)  # Interés mensual
        return 0  # Sin deuda, sin interés


    def imprimir_detalles(self):
        super().imprimir_detalles()    
        print(f"Tipo de cuenta: Crédito")    
        print(f"Límite de crédito: ${self.__limite_credito:.2f}")  # Límite total
        print(f"Saldo disponible: ${self.__saldo_disponible:.2f}")  # Crédito disponible
        print(f"Tasa de interés anual: {self.__tasa_interes*100}%")  # Tasa de interés
        # Mostrar interés mensual solo si hay deuda
        if self.saldo < 0:
            print(f"Interés mensual estimado: ${self.calcular_interes_mensual():.2f}")
