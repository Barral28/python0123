###Luis Elias Barral Larios
import sys

n=int(input("Ingrese la cantidad de argumentos "))
lista=[]
def añadirArgu(op):
    for i  in range(0,n):
        lista.append(input(f"Argumento {i+1}: "))
    return lista

def argumentos(*args):
    for arg in args:
        print(arg)
argumentos(añadirArgu(n))

