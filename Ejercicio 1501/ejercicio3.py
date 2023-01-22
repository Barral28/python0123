###Luis Elias Barral Larios
def mayor(x1,x2):
    if x1>x2:
        return x1
    elif x2>x1:
        return x2

n1 = int(input('Ingrese un numero: '))
n2 = int(input('Ingrese otro numero: '))

print('El numero mayor es ',mayor(n1,n2))