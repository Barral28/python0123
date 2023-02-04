## Luis Elias Barral Larios
print("\nEjercicio 8")
print('''
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin
tener en cuenta mayúsculas y minúsculas
'''
)
contra='contraseña'
n=input('\nIngrese la contraseña: ')
n=n.lower()
if n==contra:
    print('La contraseña es correcta')
else:
    print('Contraseña incorrecta')

