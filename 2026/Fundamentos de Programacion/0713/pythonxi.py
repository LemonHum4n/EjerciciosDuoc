libros = { 
    'L001': ['Cien años de soledad', 'tapa dura', 'novela', 'A', True, 'Sudamericana'], 
    'L002': ['El principito', 'bolsillo', 'infantil', 'A', True, 'Salamandra'], 
    'L003': ['1984', 'tapa blanda', 'distopia', 'B', False, 'Debolsillo'] 
} 

inventario = { 
    'L001': [12, 15990], 
    'L002': [8, 8990], 
    'L003': [5, 10990] 
}

def validarNumeroEnteroPositivo(mensaje:str):
    print("=================")
    print(mensaje)
    while True:
        try:
            numero=int(input("-->"))
            if numero < 0:
                print("El numero no puede ser negativo.")
            else:
                break
        except:
            print("Valor invalido. Intente nuevamente")
    return numero

def validarString(mensaje:str, nombreVariable:str):
    print("=================")
    print(mensaje)
    while True:
        try:
            texto=input("-->")
            if texto.replace(" ","")=="":
                print(f"El {nombreVariable} no puede estar vacio.")
            else:
                break
        except:
            print("Valor invalido. Intente nuevamente.")
    return texto

def codigoLibro(mensaje:str):
    print("=================")
    print(mensaje)
    while True:
        try:
            codigo=input("-->")
            if codigo.replace(" ","")=="":
                print("El codigo no puede estar vacio.")
            else:
                codigoSinEspacio=True
                for i in codigo:
                    if i=="":
                        print("El codigo no puede contener espacios.")
                        codigoSinEspacio=False
                        break
                if codigoSinEspacio:
                    break
        except:
            print("Valor invalido. Intente nuevamente.")
    return codigo
            


def agregarLibro(dicLibros:dict, dicInv:dict):
    while True:
        codigo=codigoLibro("Ingrese codigo del libro a agregar.")
        if codigo in libros:
            print(f"El codigo {codigo} ya existe.")
        else:
            break
    titulo=validarString("Ingrese titulo del libro", "titulo")
    formato=validarString("Ingrese formato del libro", "formato")
    genero=validarString("Ingrese genero del libro","genero")
    clasificacion=validarString("Ingrese clasificacion del libro","clasificacion")
    print("=================")
    print(f"¿El libro {titulo} esta disponible para prestamo?")
    print("1- Si")
    print("2- No")
    while True:
        opcdispo=validarNumeroEnteroPositivo("Ingrese opcion.")
        if opcdispo==1:
            disponibilidad=True
            break
        elif opcdispo==2:
            disponibilidad=False
            break
        else:
            print("Esta opcion no existe.")
            print("Intente nuevamente.")
    editorial=validarString("Ingrese editorial del libro", "editorial")


    # Inventario

    stock=validarNumeroEnteroPositivo("Ingrese stock del libro.")
    precio=validarNumeroEnteroPositivo("Ingrese precio del libro.")

    dicLibros[codigo] = [titulo,formato,genero,clasificacion,disponibilidad,editorial]
    dicInv[codigo] = [stock,precio]


def buscarLibro(dicLibros:dict,dicInv:dict,codigo:str):
    if codigo in dicLibros:
        print("=================")
        print(f"Codigo: {codigo}")
        print(f"Titulo: {dicLibros[codigo][0]}")
        print(f"Formato: {dicLibros[codigo][1]}")
        print(f"Genero: {dicLibros[codigo][2]}")
        print(f"Clasificacion: {dicLibros[codigo][3]}")
        print(f"Disponibilidad para prestamo: {dicLibros[codigo][4]}")
        print(f"Editorial: {dicLibros[codigo][5]}")
        print(f"\nStock: {dicInv[codigo][0]}")
        print(f"Precio: ${dicInv[codigo][1]}")
    else:
        print(f"El libro con codigo {codigo} no existe.")

def modificarLibro(dicLibros:dict,dicInv:dict,codigo:str):
    if codigo in dicLibros:
        print(f"Titulo actual: {dicLibros[codigo][0]}")
        titulo=validarString("Ingrese titulo del libro", "titulo")
        print("=================")
        print(f"Formato actual: {dicLibros[codigo][1]}")
        formato=validarString("Ingrese formato del libro", "formato")
        print("=================")
        print(f"Genero actual: {dicLibros[codigo][2]}")
        genero=validarString("Ingrese genero del libro","genero")
        print("=================")
        print(f"Clasificacion actual: {dicLibros[codigo][3]}")
        clasificacion=validarString("Ingrese clasificacion del libro","clasificacion")
        print("=================")
        print(f"Disponibilidad actual: {dicLibros[codigo][4]}")
        print("=================")
        print(f"¿El libro {titulo} esta disponible para prestamo?")
        print("1- Si")
        print("2- No")
        while True:
            opcdispo=validarNumeroEnteroPositivo("Ingrese opcion.")
            if opcdispo==1:
                disponibilidad=True
                break
            elif opcdispo==2:
                disponibilidad=False
                break
            else:
                print("Esta opcion no existe.")
                print("Intente nuevamente.")
        print("=================")
        print(f"Editorial actual: {dicLibros[codigo][5]}")
        editorial=validarString("Ingrese editorial del libro", "editorial")


        # Inventario
        print("=================")
        print(f"Stock actual: {dicInv[codigo][0]}")
        stock=validarNumeroEnteroPositivo("Ingrese stock del libro.")
        print("=================")
        print(f"Stock actual: {dicInv[codigo][1]}")
        precio=validarNumeroEnteroPositivo("Ingrese precio del libro.")

        dicLibros[codigo] = [titulo,formato,genero,clasificacion,disponibilidad,editorial]
        dicInv[codigo] = [stock,precio]
    else:
        print(f"El libro con el codigo {codigo} no existe.")


def eliminarLibro(dicLibros:dict,dicInv:dict,codigo:str):
    if codigo in dicLibros:
        dicLibros.pop(codigo)
        dicInv.pop(codigo)
        print("El libro ha sido eliminado con exito.")
    else:
        print(f"No existe un libro con el codigo {codigo}")

def mostrarPorRango(minimo:int,maximo:int,dicLibros:dict,dicInv:dict):
    librosEncontrados=False
    for codigo in dicLibros:
        if maximo >= dicInv[codigo][1] >= minimo:
            buscarLibro(dicLibros,dicInv,codigo)
            librosEncontrados=True

    if not librosEncontrados:
        print(f"No existen libros con precios entre el rango ${minimo} - ${maximo}")




    









def menu():
    while True:
        print("=================")
        print("1. Agregar Libro.")
        print("2. Buscar libro por codigo.")
        print("3. Mostrar todos los libros.")
        print("4. Modificar libro.")
        print("5. Eliminar libro.")
        print("6. Mostrar libros por rango de precio.")
        print("7. Salir.")
        opc=validarNumeroEnteroPositivo("Ingrese opcion.")

        if opc==1:
            print("=================")
            print("1. Agregar libro.")
            agregarLibro(libros,inventario)

        elif opc==2:
            print("=================")
            print("2. Buscar libro por codigo.")
            codigo=codigoLibro("Ingrese codigo del libro a buscar")
            buscarLibro(libros,inventario,codigo)


        elif opc==3:
            print("=================")
            print("3. Mostrar todos los libros.")
            for codigo in libros:
                buscarLibro(libros,inventario,codigo)

        elif opc==4:
            print("=================")
            print("4. Modificar libro.")
            codigo=codigoLibro("Ingrese codigo del libro a modificar.")
            modificarLibro(libros,inventario,codigo)
        
        elif opc==5:
            print("=================")
            print("5. Eliminar libro.")
            codigo=codigoLibro("Ingrese codigo del codigo a eliminar.")
            eliminarLibro(libros,inventario,codigo)

        elif opc==6:
            print("=================")
            print("6. Mostrar libros por rango de precio.")
            minimo=validarNumeroEnteroPositivo("Ingrese valor minimo.")
            maximo=validarNumeroEnteroPositivo("Ingrese valor maximo.")
            mostrarPorRango(minimo,maximo,libros,inventario)

        elif opc==7:
            print("=================")
            print("7. Salir.")
            print("=================")
            print("Hasta luego, Usuario.")
            break

        else:
            print("=================")
            print("Esta opcion no existe.")
            print("Intente nuevamente.")


menu()