class Cliente:
    def __init__(self):
        self.nombre = input('dime el nombre de usuario del registro: ')
        self.contraseña = input('Ponla contraseña del usuario: ')
        self.telefono = input('dime tu telefono: ')
        self.correo = input('dime tu correo: ')
        self.direccion = input('dime tu direcion: ')
        self.pais = input("El pais de residencia: ")


    def registrar(self):
        print(f"Registro exitoso. Bienvenido{self.nombre}")

    def imprimir_factura(self):
        print("La factura se ha impreso en pdf.")
        print("muchas gracias por tu compra")



cliente = Cliente()
cliente.registrar()
print('Estos son los productos: ')


precio=[10,20]
productoscomprados=[] 
lista=["pantalon","camiseta"]
precio1=0


class Pedidos:
    def __init__(self):

        self.lista=["pantalon","camiseta","abrigos","calcetines","gorro"]
        
        
        

    def agregar_producto(self):
            while True:
                pregunta=print('que quieres hacer: \n 1 - añadir productos \n 2 - elimanar producto: \n 3 - ver bolsa: \n 4 - salir  ')
                self.peticion=input()
                if self.peticion=="1":
                    print(f"estos son los productos: {self.lista}")
                    self.pedir=input('que producto quieres añadir: ')
                    productoscomprados.append(self.pedir)
                    print("producto añadido correctamente" )
                elif self.peticion=="2":
                    print("Que producto quieres eliminar: ")
                    self.eliminar=input()
                    productoscomprados.remove(self.eliminar)
                    print('producto eliminado correctamente')
                elif self.peticion=="3":
                    print(productoscomprados)
                    print(precio1)  
                elif self.peticion=="4":
                    break       
                else:
                    print("seleciona una opcion valida")   

   
pedido = Pedidos()

pedido.agregar_producto()
cliente.imprimir_factura()



#indice=lista.index(self.pedir) precios=precio[indice] precio1=precio1+precios
