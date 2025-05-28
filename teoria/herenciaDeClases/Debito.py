From Madre.py import

class CuentaDebito(Cuenta):
    # Constructor con parámetro adicional de sobregiro
    def __init__(self, titular, saldo=0, sobregiro=1000):
        super().__init__(titular, saldo)  
        self.__sobregiro = sobregiro  # Límite de sobregiro permitido
    
    @property
    def sobregiro(self):
        return self.__sobregiro
    
    # Sobreescritura del método retirar para permitir sobregiros
    def retirar(self, cantidad):
        # Validar cantidad positiva y que no exceda saldo + sobregiro
        if cantidad > 0 and cantidad <= (self.saldo + self.__sobregiro):
            self._Cuenta__saldo -= cantidad  # Acceder al saldo privado del padre
            return True    
        return False    
    
    # Sobreescritura del método para mostrar detalles
    def imprimir_detalles(self):
        super().imprimir_detalles()  
        print(f"Tipo de cuenta: Corriente")  # Tipo de cuenta
        print(f"Límite de sobregiro: ${self.__sobregiro:.2f}")  # Límite de sobregiro

