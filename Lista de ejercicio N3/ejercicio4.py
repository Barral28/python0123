"""4. Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
tener un método para agregar productos y otra para mostrar toda la lista de productos"""
def ejer4():
    class Catalogo:
        producto=[]
        def __init__(self,producto=[]):
            self.producto=producto
        def agregar(self,agre):
            self.producto.append(agre)
        def mostrar(self):
            for agre in self.producto:
                print(agre)    
        
    class Producto:
        def __init__(self,precio,descripcion,stock):
            self.precio=precio
            self.descripcion=descripcion
            self.stock=stock
        def __str__(self):
            return f"Precio:{self.precio} , Descripcion:{self.descripcion} , Stock :{self.descripcion}"