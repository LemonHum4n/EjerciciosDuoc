productos = []
cantidades = []

while True:
    print("===================")
    print("1. Agregar producto y cantidad.")
    print("2. Mostrar la lista de compras completa.")
    print("3. Buscar un producto.")
    print("4. Modificar la cantidad de un producto.")
    print("5. Eliminar un producto de la lista.")
    print("6. Salir.")
    print("===================")
    while True:
        try:
            opc=int(input("-->"))
            if opc==0:
                print("No se puede ingresar cero.")
            elif opc<1 or opc>6:
                print("Ingrese una opcion dentro del rango (1-6)")
            else:
                break
        except:
            print("Valor invalido. Intente nuevamente")
    
    if opc==1:
        print("===================")
        print("1. Agregar producto y cantidad.")
        print("===================")
        print("Ingrese nombre del producto.")
        nombreProducto=input("-->")
        if nombreProducto.capitalize() in productos:
            print(f"Ya existe un producto llamado {nombreProducto}")
        else:
            print(f"Ingrese cantidad del producto: {nombreProducto}.")
            while True:
                try:
                    cantidadProducto=int(input("-->"))
                    if cantidadProducto<=0:
                        print("No se permiten ceros ni numeros negativos.")
                    else:
                        productos.append(nombreProducto.capitalize())
                        cantidades.append(cantidadProducto) 
                        break
                except:
                    print("Valor invalido. Intente nuevamente")
        
    
    elif opc==2:
        print("===================")
        print("2. Mostrar la lista de compras completa.")
        print("===================")
        print("=== LISTA DE COMPRAS ===")
        if len(productos)>0:

            print("Producto     |       Cantidad")
            print("========             ========")
            for i in range(len(productos)):
                print(f"{productos[i]}                      {cantidades[i]}")
            
            print(f"Total de productos: {len(productos)}")
        else:
            print("La lista de compras esta vacia.")

            


    elif opc==3:
        print("===================")
        print("3. Buscar un producto.")
        print("===================")
        print("Ingrese nombre del producto a buscar.")
        nombreABuscar=input("-->")
        productoEncontrado=False
        for i in range(len(productos)):
            if productos[i] == nombreABuscar.capitalize():
                print(f"Cantidad: {cantidades[i]}")
                productoEncontrado= True
        if not productoEncontrado:
            print("¡ERROR! Este producto no existe.")
        

    elif opc==4:
        print("===================")
        print("4. Modificar la cantidad de un producto.")
        print("===================")
        print("Ingrese nombre del producto a buscar.")
        nombreABuscar=input("-->")
        productoEncontrado=False
        for i in range(len(productos)):
            if productos[i] == nombreABuscar.capitalize():
                print("Ingrese cantidad a cambiar")
                while True:
                    try:
                        cantidadCambiarProducto=int(input("-->"))
                        if cantidadCambiarProducto<=0:
                            print("No se permiten ceros ni numeros negativos.")
                        else:
                            cantidades[i]=cantidadCambiarProducto
                            print(f"Cantidad del producto {nombreABuscar.capitalize()} cambiada.")
                            break
                    except:
                        print("Valor invalido. Intente nuevamente")
                productoEncontrado= True
        if not productoEncontrado:
            print("Este producto no existe.")


    elif opc==5:
        print("===================")
        print("5. Eliminar un producto de la lista.")
        print("===================")
        nombreABuscar=input("-->")
        productoEncontrado=False
        for i in range(len(productos)):
            if productos[i] == nombreABuscar.capitalize():
                productoAEliminar=i
                productoEncontrado= True
        if not productoEncontrado:
            print("¡ERROR! Este producto no existe.")
        else:
            productos.pop(productoAEliminar)
            cantidades.pop(productoAEliminar)
            print("El producto a sido eliminado.")


    elif opc==6:
        print("===================")
        print("6. Salir.")
        print("===================")
        print("Hasta luego Usuario.")
        break