#Este es mi archivo de pruebas acerca de los codigos que hemos ido construyendo en clase 
#Autor: Brandon Martínez López   19-02-2025

from Cuenta.py import
from Cliente.py import
from MenuBanco.py import

class Main:
    pass



banco1 = MenuBanco("Banciencias")
banco1.darBienvenida()
cliente1 = Cliente("Juan Bodoque","Iztapalapa,fresas #59",35)
cliente1.imprimirDetalles()
cuenta1 = Cuenta(80000,"debito","Juan Bodoque")
cuenta1.imprimirDetalles()
cuenta1.retirar(5000)
cuenta1.imprimirDetalles()
cuenta1.depositar(17000)
cuenta1.imprimirDetalles()
