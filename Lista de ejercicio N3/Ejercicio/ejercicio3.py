def ejer3(x):
    def nameFile():
        if __name__=='__main__':
            print("archivo principal")
        else:
            print("dependencia")
    nameFile()
    x=x*2
    print(x)
    
n=int(input("Ingrese un valor : "))
print(ejer3(n))
    