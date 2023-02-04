
import os
from ejercicio2 import e2
from ejercicio3 import e3
from ejercicio4 import e4
from ejercicio5 import e5
from ejercicio6 import e6
from ejercicio7 import e7

class main:
    def nameFile():
      if __name__=='__main__':
            print("archivo principal")
      else:
        print("dependencia")
main.nameFile()

print("""
1) Ejercicio 2
2) Ejercicio 3
3) Ejercicio 4
4) Ejercicio 5
5) Ejercicio 6
6) Ejercicio 7
""")
opc=input("Ingrese la opcion deseada: ")
if opc=='1':
      print("Ejercicio 2")
      e2.ejer2()
      
elif opc=='2':
      print("Ejercicio 3")
      e3.ejer3()
      
elif opc=='3':
      print("Ejercicio 4")
      e4.ejer4()
      
elif opc=='4':
      print("Ejercicio 2")
      try:
            e5.ejer5()
      except:
            print("Error")
      else:
            print("Imprimiendo directorio")
            print(os.getcwd())
      finally:
            print("Proceso terminado")
    
elif opc=='5':
      print("Ejercicio 2")
      e6.ejer6()
      
elif opc=='6':
      print("Ejercicio 2")
      e7.ejer7()
else:
      print("Error")
