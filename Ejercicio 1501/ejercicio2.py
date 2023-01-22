###Luis Elias Barral Larios
Biblioteca={
    'categoria':["Drama","Terror","Satira",],
   
    'estado':["activo","prestamo"],
   
    'alumnos':{
        "0001":{"nombre":"juan",
                "apellido":"rodriguez",
                "libro":[],
                },

        "0002":{"nombre":"juan",
                "apellido":"rodriguez",
                "libro":[],
                },

        "0003":{"nombre":"juan",
                "apellido":"rodriguez",
                "libro":[],
                },
            },

    'libro': {
        "1000":{"nombre_libro":"Don quijote",
                "nombre_autor":"Miguel cervantes",
                "categoria":"Satira",
                "estado":"prestado",
                },

        "1001":{"nombre_libro":"Divina comedia",
                "nombre_autor":"Dante aliguieri",
                "Estado":"prestado",
                "categoria":"Drama",
                },

        "1002":{"nombre_libro":"Edgar Alan Poe",
                "apellido":"El gato negro",
                "estado":"activo",
                "categoria":"Terror",
                },
            },
}

print("""Escribe una opción
        1) Obtener la lista de categorías de libros.
        2) Obtener nombres de los libros y autores.
        3) poder cambiar el estado de un libro a prestado
        4) Lista de usuarios de la biblioteca.
        5) Salir""")
opcion=input()

if opcion == '1':
    print(Biblioteca["categoria"])
            
elif opcion == '2':
    codigo=input("Ingrese el codigo del libro: ")
    listalibros=list(Biblioteca["libro"].keys())
    if codigo in listalibros:
        print("Libro encontrado")
        titulo=Biblioteca["libro"][codigo]["nombre_libro"]
        autor=Biblioteca["libro"][codigo]["nombre_autor"]
        print(Biblioteca["libro"])
            # print(nombre_libro)
            # print(nombre_autor)
        
elif opcion =='3':
    codigo=input("Ingrese el codigo del libro: ")
    listalibros=list(Biblioteca["libro"].keys())
    if codigo in listalibros:
        print("Libro encontrado")
        titulo=Biblioteca["libro"]["estado"]="prestado"
        cambio=Biblioteca["libro"][codigo]["estado"]
        print("Cambiado a ",cambio)
    else:
        print("Libro no encontrado")
elif opcion =='4':  
    lista=list()
    lista.append(Biblioteca["alumnos"])
    print(lista)
else:
    print("Comando desconocido, vuelve a intentarlo")
       
        



