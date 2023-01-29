##Barral Larios Luis Elias
##Ejercicio 6
def ejer6():
    def nameFile():
        if __name__=='__main__':
            print("archivo principal")
        else:
            print("dependencia")
    nameFile() 
    
    import sys
    n=sys.argv[0]
    print("\n")
    print(n)