notebooks = {}
bodega = {}

def validarString(mensaje:str):
    print("=================")
    print(mensaje)
    while True:
        try:
            texto=input("-->")
            if texto.replace(" ","")=="":
                print("El valor no puede estar vacio.")
            else:
                break

        except:
            print("Valor invalido.")
    return texto

def validarNumeroEntero(mensaje:str):
    print("=================")
    print(mensaje)
    while True:
        try:
            numero=int(input("-->"))
            if numero>=0:
                break
            else:
                print("El numero no puede ser menor a cero.")
        except:
            print("Valor invalido.")
    return numero

def validarNumeroDecimal(mensaje:str):
    print("=================")
    print(mensaje)
    while True:
        try:
            numero=float(input("-->"))
            if numero>=0.0:
                break
            else:
                print("El numero no puede ser menor a cero.")
        except:
            print("Valor invalido.")
    print (numero)
    return numero

def validarCodigo(mensaje:str):
    print("=================")
    print(mensaje)
    while True:
        try:
            codigo=input("-->")
            if codigo.replace(" ","")=="":
                print("El codigo no puede estar vacio.")
            
            contieneEspacio=False
            for i in codigo:
                if i==" ":
                    print("El codigo no puede tener espacios.")
                    contieneEspacio=True

            if not contieneEspacio:
                break
        except:
            print("Valor invalido.")
    return codigo






def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock de Notebook por código")
    print("2. Búsqueda de Notebooks por rango de precio")
    print("3. Actualizar precio de un Notebook")
    print("4. Agregar nuevo Notebook")
    print("5. Eliminar Notebook")
    print("6. Salir del programa")
    print("=====================================")
    