
import os
from Ejercicio.ejercicio2 import *
from Ejercicio.ejercicio3 import *
from Ejercicio.ejercicio4 import *
from Ejercicio.ejercicio5 import *
from Ejercicio.ejercicio6 import *
from Ejercicio.ejercicio7 import *

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
      ejer2()
elif opc=='2':
      ejer3()
elif opc=='3':
      ejer4()
elif opc=='4':
  try:
      ejer5()
  except:
    print("Error")
  else:
    print("Imprimiendo directorio")
    print(os.getcwd())
  finally:
    print("Proceso terminado")
elif opc=='5':
      ejer6()
elif opc=='6':
      ejer7()
else:
  print("Error")

    