From Madre.py import

class CuentaDebito(Madre):
    def __init__(self, valor):
        super().__init__(valor, "Débito")  
    
    def __str__(self):
        return f" Cuenta de Débito | Saldo disponible: ${self._Madre__valor:.2f}"
