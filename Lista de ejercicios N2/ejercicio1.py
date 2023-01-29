###Luis Elias Barral Larios
print("         MENU")
while True:
    print("""Escribe una opción
    1)  Realizar un programa que dibuje un cuadrado en consola con *, usando bucles
    2)  Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e
imprimir el número
    3)Iterar una lista de elementos que contengan nombre y edad e imprimir solo los
mayores de edad.
    4) Salir""")

    opcion = input() # me devuelve un string ''
    if opcion == '1':
        n=int(input("Ingresar el numero de lados: "))
        for i in range(1,n+1):
            for i in range(1,n+1):
                print("*",end=" ")
            print(" ")
       
    
    elif opcion == '2':
        n = int(input("Introduce el numero de elementos: "))
        l=[]
        l1=[]
        for i in range(n):
            print("Ingrese el elemento de la posicion ",i)
            l.append(int(input()))
            if l[i]%2==0:
                l1.append(l[i])
        print (l1)
        

    elif opcion =='3':
        n = int(input("Introduce el numero de elementos: "))
        nombres=[]
        edades=[]
        for x in range(n):
            nom=input("Ingrese el nombre de la persona:")
            nombres.append(nom)
            ed=int(input("Ingrese la edad de dicha persona:"))
            edades.append(ed)

        print("Nombre de las personas mayores de edad:")
        for x in range(n):
            if edades[x]>=18:
                print(nombres[x],edades[x])
    else:
        print("Comando desconocido, vuelve a intentarlo")
        break;