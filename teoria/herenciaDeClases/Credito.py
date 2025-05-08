From Madre.py import

class CuentaCredito(Madre):
    def __init__(self, valor, limite_credito):
        super().__init__(valor, "Crédito")
        self.__limite_credito = limite_credito
    
    def __str__(self): #reescribi el codigo str de esta manera porque lo vi correcto ya que las tarjetas de credito te deben enseñar mas datos ademas de solo tu saldo
        disponible = self.__limite_credito + self._Madre__valor  # Saldo + límite
        return (f" Cuenta de Crédito | "
                f"Saldo: ${self._Madre__valor:.2f} | "
                f"Límite: ${self.__limite_credito:.2f} | "
                f"Disponible: ${disponible:.2f}")
