class Cliente:
    def __init__(self,nombre,direccion,edad):
        self.nombrePropietario = nombre
        self.direccionPropietario = direccion
        self.edadPropietario = edad
    def imprimirDetalles(self):
        print("La informacion del cliente es:")
        print("nombre:", self.nombrePropietario)
        print("edad:", self.edadPropietario)
        print("direccion:", self.direccionPropietario)
        print()

