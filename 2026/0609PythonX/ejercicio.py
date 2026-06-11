inventario=[]
codigoAsignar=1000

while True:
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

    if opc==1:
        print("==================")
        print("1. Agregar videojuego.")
        print("==================")
        print("Ingrese título del videojuego")
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
                print("Valor invalido.")
        
        print("Ingrese género del videojuego")
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

        {
            "codigo":codigo,
            "titulo":titulo,
            "genero":genero,
            "precio":precio,
            "stock":stock
        }

    elif opc==2:
        print("==================")
        print("2. Registrar venta.")
        print("==================")
    
    elif opc==3:
        print("==================")
        print("3. Mostrar inventario por género.")
        print("==================")
    
    elif opc==4:
        print("==================")
        print("4. Buscar por género.")
        print("==================")

    elif opc==5:
        print("==================")
        print("5. Salir.")
        print("==================")
        print("Hasta luego, Usuario.")
        break

    
        

