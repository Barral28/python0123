"""5.Crear un paquete de programas (módulo) que tenga las siguiente funciones
-Una función recursiva de suma de los n primeros números
-Una función que me permita dividir 2 números.
-importar esos módulos desde el archivo main"""
def ejer5():
    def nameFile():
        if __name__=='__main__':
            print("archivo principal")
        else:
            print("dependencia")
    nameFile()
    
    def recursivo(n):
        if n==1:
            return 1
        else:
            return n +recursivo(n)
    x=int(input("Ingrese un valor: "))
    print(recursivo(x))



    def division(n1,n2):
        if n2!=0:
            print("El division es ",x1/x2)
        else:
            print(" No se puede dividir")
            
    x1=int(input("Ingrese un valor: "))
    x2=int(input("Ingrese un valor: "))
    print(division(x1,x2)) 
        