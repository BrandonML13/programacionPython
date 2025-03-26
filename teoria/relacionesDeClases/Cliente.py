class Cliente:
    def __init__(self,nombre,direccion,edad,c):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.cuenta = c #dejo este atributo publico porque se ingresa directamente en el main

    def imprimirDetalles(self):
        print("La informacion del cliente es:")
        print("nombre:", self.__nombre)
        print("edad:", self.__edad,"años")
        print("direccion:", self.__direccion)
        print(self.cuenta.imprimirDetalles())
        print()

cliente1 = Cliente("Brandon Marlo","Roma,La petit cita #59,C.P 08343",35,cuenta1)
