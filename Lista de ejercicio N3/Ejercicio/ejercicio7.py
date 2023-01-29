"""7.Programa que tenga una clase Producto el cual solo tiene el atributo de nombre ,codigo
el cual tiene la siguiente estructura ‘PAIS-LOTE-AÑO’ ejemplo : ‘PERU-0001-2023’ crear un
método que permita imprimir el objeto de forma literal (__str__) y que me permita identificar
el país de origen , el numero de lote ."""
def ejer7():
    class main:
        def nameFile():
            if __name__=='__main__':
                print("archivo principal")
            else:
                print("dependencia")   
        nameFile()
    
    class Producto:
        def __init__(self,nombre,codigo):
            self.nombre=nombre
            self.codigo=codigo
        def __str__(self):
            cod=self.codigo.split(sep="-")
            pais=cod[0]
            lote=cod[1]
            return f"Nombre: {self.nombre} , Pais: {self.pais} , Lote: {self.lote}"
    x=input("Ingrese el nombre del producto: ")
    y=input("Ingrese el codigo del producto: ")
    n=Producto(x,y)
    print(n)