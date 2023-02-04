# Luis Elias Barral Larios
print("\nEjercicio 6.")
print("Realice un programa que calcule la suma de los números hasta el valor ingresado. \nEjemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5.")
sum=0
n=int(input("\nValor: "))
for i in range(1,n+1):
    sum=sum+(i)
print("La suma total es",sum)
