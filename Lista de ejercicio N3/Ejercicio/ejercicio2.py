#Barral Larios Luis Elias
def ejer2():
      def nameFile():
        if __name__=='__main__':
          print("archivo principal")
        else:
          print("dependencia")
      nameFile()

      texto = """Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
      Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
      impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos
      y los mezcló de tal manera que logró hacer un libro de textos especimen."""
    
      print("Usando split")
      print(texto.split(sep=" ", maxsplit=2))
      
      print("Usando join")
      print(" ".join(texto))
      
      print("Usando count")
      print(texto.count("Lore"))
      
      print("Usando find")
      print(texto.find("Ipsum"))
      
      print("Usando uppercase")
      print(texto.upper())
      
      print("Usando lowercase")
      print(texto.lower())
   
