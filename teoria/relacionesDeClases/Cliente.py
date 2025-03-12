class Cliente:
    def __init__(self,nombre,direccion,edad,c):
        self.nombrePropietario = nombre
        self.direccionPropietario = direccion
        self.edadPropietario = edad
        self.cuenta = c
    def imprimirDetalles(self):
        print("La informacion del cliente es:")
        print("nombre:", self.nombrePropietario)
        print("edad:", self.edadPropietario,"años")
        print("direccion:", self.direccionPropietario)
        print(self.cuenta.imprimirDetalles())
        print()
     
