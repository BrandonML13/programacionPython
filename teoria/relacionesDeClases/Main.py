#Este es mi archivo de pruebas acerca de los codigos que hemos ido construyendo en clase 
#Autor: Brandon Martínez López   19-02-2025

from Cuenta.py import
from Cliente.py import
from MenuBanco.py import

class Main:
    pass




banco1 = MenuBanco("Banciencias")
banco1.darBienvenida()
cuenta1 = Cuenta(75300,"Debito")
cliente1 = Cliente("Brandon Marlo","Roma,La petit cita #59,C.P 08343",35,cuenta1)
banco1.realizarAccion()
