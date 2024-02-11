class Producto:
    def __init__(self, nombre, precio, año, marca):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.marca = marca
    def __str__(self):
        return f"Producto: {self.nombre}, Marca: {self.marca}, Precio: {self.precio}, Año: {self.año}"
class Catalogo:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            print("Lista de productos en el catálogo:")
            for producto in self.productos:
                print(producto)
    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if not productos_filtrados:
            print(f"No hay productos para el año {año}.")
        else:
            print(f"Productos para el año {año}:")
            for producto in productos_filtrados:
                print(producto)
    def filtrar_por_precio_maximo(self, precio_max):
        productos_filtrados = [producto for producto in self.productos if producto.precio <= precio_max]
        if not productos_filtrados:
            print(f"No hay productos con precio igual o inferior a {precio_max}.")
        else:
            print(f"Productos con precio igual o inferior a {precio_max}:")
            for producto in productos_filtrados:
                print(producto)
if __name__ == '__main__':
    catalogo = Catalogo()
    while True:
        nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        precio = float(input("Ingrese el precio del producto: "))
        año = int(input("Ingrese el año del producto: "))
        marca = input("Ingrese la marca del producto: ")
        producto = Producto(nombre, precio, año, marca)
        catalogo.agregar_producto(producto)
    catalogo.mostrar_productos()
    año_filtro = int(input("Ingrese el año para filtrar los productos: "))
    catalogo.filtrar_por_año(año_filtro)
    precio_max_filtro = float(input("Ingrese el precio máximo para filtrar los productos: "))
    catalogo.filtrar_por_precio_maximo(precio_max_filtro)
