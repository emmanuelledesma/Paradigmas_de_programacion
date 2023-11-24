#Diseña un sistema de comercio electrónico para una tienda en línea. Debes
#implementar las siguientes clases:
#Producto: Una clase que representa un producto con atributos como nombre,
#precio, cantidad en stock, etc.
#CarritoCompra: Una clase que representa el carrito de compras de un cliente.
#Debe permitir agregar, eliminar y calcular el total de los productos en el carrito.
#Cliente: Una clase que representa a un cliente con atributos como nombre,
#dirección, carrito de compra, etc.
#Crea instancias de estas clases y demuestra cómo un cliente puede agregar
#productos a su carrito, realizar una compra y calcular el total

class Producto:
    def __init__(self, nombre, precio, cantidad_stock):
        self.nombre = nombre
        self.precio = precio
        self._cantidad_stock = cantidad_stock

    @property
    def cantidad_stock(self):
        return self._cantidad_stock

    def movimiento_stock(self, cantidad, tipo):

        if tipo == "entrada":
            self._cantidad_stock += cantidad
            print(f"Stock de {self.nombre} aumentado en {cantidad}. Nuevo stock: {self.cantidad_stock}")
        elif tipo == "salida":
            if cantidad <= self._cantidad_stock:
                self._cantidad_stock -= cantidad
                print(f"Stock de {self.nombre} reducido en {cantidad}. Nuevo stock: {self.cantidad_stock}")
            else:
                raise StockInsuficienteError(self, cantidad) 

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Stock: {self.cantidad_stock}"

class StockInsuficienteError(Exception):
    
    def __init__(self, producto, cantidad_requerida):
        self.producto = producto
        self.cantidad_requerida = cantidad_requerida
        super().__init__(f"No hay suficiente stock de {producto.nombre}. Stock actual: {producto.cantidad_stock}")

class CarritoCompra:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto, cantidad):

        try:
            producto.movimiento_stock(cantidad, "salida")
            self._productos.append({"producto": producto, "cantidad": cantidad})
            print(f"{cantidad} {producto.nombre}(s) agregado(s) al carrito.")
        except StockInsuficienteError as e:
            print(f"Error: {e}")

    def eliminar_producto(self, producto, cantidad):
        for item in self._productos:
            if item["producto"] == producto:
                if item["cantidad"] >= cantidad:
                    item["cantidad"] -= cantidad
                    producto.movimiento_stock(cantidad, "entrada")
                    if item["cantidad"] == 0:
                        self._productos.remove(item)
                    print(f"{cantidad} {producto.nombre}(s) eliminado(s) del carrito.")
                else:
                    print(f"No hay suficientes {producto.nombre}(s) en el carrito.")
                return
        print(f"{producto.nombre} no encontrado en el carrito.")

    def calcular_total(self):
        total = sum(item["producto"].precio * item["cantidad"] for item in self._productos)
        return total

    def __str__(self):
        return f"Carrito de Compra - Total: ${self.calcular_total()}"


    def __str__(self):
        return f"Carrito de Compra - Total: ${self.calcular_total()}"

class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.carrito = CarritoCompra()

    def continuar_compra(self):
        respuesta = input("¿Desea continuar con la compra? (S/N): ").upper()
        return respuesta == "S"

    def __str__(self):
        return f"Cliente: {self.nombre} - Dirección: {self.direccion}\n{self.carrito}"

producto1 = Producto("Remera", 20000.0, 10)
producto2 = Producto("Camisa", 50000.0, 6)
producto3 = Producto("Jean", 30.0, 4)

cliente1 = Cliente("Emmanuel Ledesma", "Guemes 4331, CABA")
cliente2 = Cliente("Luca D'Allessandro", "Charcas 2020, CABA")

cliente1.carrito.agregar_producto(producto1, 4)
cliente1.carrito.agregar_producto(producto1, 6)
cliente2.carrito.agregar_producto(producto2, 7)
cliente2.carrito.agregar_producto(producto3, 7)

cliente1.carrito.eliminar_producto(producto1, 1)

#Code made by Emma Ledesma

"""Este código implementa un sistema de carrito de compras y gestión de stock. 
La clase Producto modela un artículo con nombre, precio y cantidad en stock. 
La excepción StockInsuficienteError se utiliza para manejar casos en los que 
la cantidad solicitada supera el stock disponible. 
La clase CarritoCompra administra productos, permite agregar o eliminar del carrito, 
y calcula el total de la compra. 
La clase Cliente tiene un carrito y puede decidir continuar o cancelar la compra. 
Se crean instancias para representar productos y clientes, se realizan operaciones de compra 
y se manejan posibles errores de stock insuficiente., asi como eliminar productos del carrito.

Los principios de poo aplicados son, la herencia con las clases como Producto, StockInsuficienteError,
CarritoCompra y Cliente, estableciendo una jerarquía que permite compartir y especializar comportamientos. 
El encapsulamiento se ve aplicado en la declaracion de los detalles internos que solamente se pueden acceder
con metodos internos tmb, como en el caso de movimiento_stock. 
El polimorfismo en la gestión de excepciones muestra cómo diferentes tipos de errores pueden ser manejados 
de manera uniforme."""