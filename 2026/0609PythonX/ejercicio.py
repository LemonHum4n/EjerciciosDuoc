inventario=[]
codigo=1000
def menu():
    print("==================")
    print("1. Agregar videojuego.")
    print("2. Registrar venta.")
    print("3. Mostrar inventario entero.")
    print("4. Buscar por género.")
    print("5. Salir.")
    print("==================")
    while True:
        try:
            opc=int(input("-->"))
            if opc <=0:
                print("No se permiten valores negativos o iguales a cero.")
            elif 5 < opc < 1:
                print("Valor invalido. Ingrese un valor entre el rango (1-5)")
            else:
                break
        except:
            print("Valor incorrecto. Ingrese un valor entero.")
    return opc

def validarStringDeTitulo():
    while True:
            try:
                tituloJuego=input("-->")
                if tituloJuego.replace(" ","")=="":
                    print("No se puede ingresar un titulo vacio.")
                elif tituloJuego[0].isdigit():
                    print("El titulo no puede comenzar por un numero.")
                else:
                    titulo=tituloJuego
                    break
            except:
                print("tituloJuego invalido.")
    return titulo

def validarStringDeGenero():
    while True:
            try:
                generoJuego=input("-->")

                contieneNumero=False
                for i in generoJuego:
                    if i.isdigit():
                        contieneNumero=True
                        break
                
                if generoJuego.replace(" ","")=="":
                    print("No se puede ingresar un genero vacio.")
                elif contieneNumero:
                    print("El genero no puede contener numeros.")
                else:
                    genero=generoJuego
                    break
            except:
                print("Valor invalido.")
    return genero

def validarStock():
    while True:
            try:
                stockJuego=int(input("-->"))
                if stockJuego<0:
                    print("No se puede ingresar un stock que sea menor a cero")
                else:
                    stock=stockJuego
                    break
            except:
                print("Valor invalido. Ingrese un valor entero.")
    return stock

def validarEnteroPositivo():
    while True:
        try:
            numero=int(input("-->"))
            if numero<0:
                print("No se pueden ingresar numeros negativos.")
            elif numero==0:
                print("No se puede ingresar el cero.")
            else:
                break
        except:
            print("Valor invalido. Ingrese un valor entero.")
    return numero



while True:
    opc = menu()

    if opc==1:
        print("==================")
        print("1. Agregar videojuego.")
        print("==================")
        print("Ingrese título del videojuego")
        titulo=validarStringDeTitulo()
        
        print("Ingrese género del videojuego")
        genero = validarStringDeGenero()

        print("Ingrese precio del videojuego")
        while True:
            try:
                precioJuego=float(input("-->"))
                if precioJuego<=0:
                    print("No se puede ingresar un precio que sea menor o igual a cero")
                else:
                    precio=precioJuego
                    break
            except:
                print("Valor invalido. Ingrese un valor entero.")

        print("Ingrese stock del videojuego")
        stock=validarStock()
        
        videojuego= {
            "codigo":codigo,
            "titulo":titulo,
            "genero":genero,
            "precio":precio,
            "stock":stock
        }

        inventario.append(videojuego)

        print("==================")
        print("Videojuego agregado.")
        print("==================")
        print(f"Codigo: {codigo}")
        print(f"Titulo: {titulo}")
        print(f"Genero: {genero}")
        print(f"Precio: ${precio}")
        print(f"Stock: {stock}")

        

        codigo+=1

    elif opc==2:
        print("==================")
        print("2. Registrar venta.")
        print("==================")
        print("Ingrese codigo del videojuego")
        codigoVenta=validarEnteroPositivo()
        videojuegoEncontrado=False
        for i in range(len(inventario)):
            if inventario[i]["codigo"]==codigoVenta:
                videojuegoEncontrado=True
                indiceVenta=i
        
        if videojuegoEncontrado:
            print("==================")
            print(f"Titulo:             {inventario[indiceVenta]["titulo"]}")
            print(f"Stock disponible:   {inventario[indiceVenta]["stock"]}")
            if inventario[indiceVenta]["stock"]==0:
                print("==================")
                print("El stock actual del producto es cero. No se puede vender.")
            else:
                print("==================")
                print("Ingrese cantidad a vender")
                while True:
                    cantidad=validarEnteroPositivo()
                    if cantidad>inventario[indiceVenta]["stock"]:
                        print("==================")
                        print("La cantidad a vender supera el stock disponible.")
                    else:
                        print("==================")
                        inventario[indiceVenta]["stock"]-=cantidad
                        print(f"Total de la venta: ${inventario[indiceVenta]["precio"]*cantidad}")
                        break
        else:
            print("No se encontro el videojuego")
        
        

        
    
    elif opc==3:
        print("==================")
        print("3. Mostrar inventario completo.")
        print("==================")
        if not inventario:
            print("No hay videojuegos en el inventario.")
        else:
            for i in inventario:
                valorTotal = i["precio"] * i["stock"]
                print("==================")
                print(f"Codigo:     {i["codigo"]}")
                print(f"Titulo:     {i["titulo"]}")
                print(f"Genero:     {i["genero"]}")
                print(f"Precio:     ${i["precio"]:.2f}")
                print(f"Stock:      {i["stock"]}")
                print(f"Valor Total: ${valorTotal:.2f}")
                print("==================")
                    
            
        
        
    
    elif opc==4:
        print("==================")
        print("4. Buscar por género.")
        print("==================")
        if not inventario:
            print("No hay videojuegos en el inventario.")
        else:
            print("Ingrese genero")
            genero=validarStringDeGenero()

            for i in inventario:
                if i["genero"].upper()==genero.upper():
                    print("==================")
                    print(f"Codigo:     {i["codigo"]}")
                    print(f"Titulo:     {i["titulo"]}")
                    print(f"Genero:     {i["genero"]}")
                    print(f"Precio:     {i["precio"]}")
                    print(f"Stock:      {i["stock"]}")
                    print("==================")
                    juegosEncontrados=True
            
            if not juegosEncontrados:
                print("==================")
                print(f"No se encontraron juegos del genero: {genero}")

    elif opc==5:
        print("==================")
        print("5. Salir.")
        print("==================")
        print("Hasta luego, Usuario.")
        break




