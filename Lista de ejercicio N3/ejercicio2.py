#Barral Larios Luis Elias
def ejer2():
  texto = """Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
      Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
      impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos
      y los mezcló de tal manera que logró hacer un libro de textos especimen."""
  while True:
    msg="""print("Elija una de las siguientes operaciones:")
          1) Split
          2) Join
          3) Count
          4) Find
          5) Uppercase
          6) Lowercase
          7) Salir"""
    print(msg)

    opc=input('Ingresar la opción: ')
    print('Opción elegida: ',opc)

    if opc=='1':
      lista=texto.split(sep=" ")
      print("Split: ",lista)
          
    elif opc=='2':
      lista=texto.split(sep=" ")
      print("JOIN: "," ".join(lista))
          
    elif opc=='3':
      n=input('\nIngresar palabra a contar: ')
      print("Count: ",texto.count(n))
          
    elif opc=='4':
      n=input('\nIngresar palabra a buscar: ')
      print("Find: ",texto.find(n))
          
    elif opc=='5':
      print("Uppercase: " ,texto.upper())
          
    elif opc=='6':
      print("Lowercase: ",texto.lower())
          
    elif opc=='7':
      print("Proceso terminado")
      break
          
    else:
      print('Opcion incorrecta')
          
