'''
Desarrolle un programa en Python que muestre un menú repetitivo con las siguientes
opciones:
1. Ingresar ventas de productos.
2. Mostrar reporte.
3. Salir.

'''

contadorMayor=0
contadorMenor=0
contadorTotal=0
totalVentas=0
totalMayor=0
totalMenor=0
while True:
    print("---------------------------")
    print("1. Ingresar ventas de productos.")
    print("2. Mostrar reporte.")
    print("3. Salir.")
    print("---------------------------")

    while True:
        try:
            opc = int(input("--> "))
            if opc < 1 or opc > 3:
                print("Ingrese una opcion valida. Entre 1 al 3.")
                continue
            break
        except:
            print("Ingrese un dato numerico.")
    
    if opc==1:

        '''
        Al elegir la opción 1, el programa debe pedir cuántas ventas desea registrar y luego, usando
        un ciclo for, solicitar el monto de cada venta una por una. Cada monto ingresado debe
        validarse con captura de excepciones para evitar errores cuando el usuario escriba texto u
        otro valor inválido en lugar de un número.
        Durante el ingreso de ventas, el programa debe:
        ● Acumular el total vendido.
        ● Contar cuántas ventas fueron mayores a 10000.
        ● Contar cuántas ventas fueron menores o iguales a 10000.|
        ● Acumular por separado el total de ventas mayores a 10000 y el total de ventas
        menores o iguales a 10000.
        '''
        print("---------------------------")
        print("1. Ingresar ventas de productos.")
        print("---------------------------")
        print("Ingrese la cantidad de ventas a registrar")
        while True:
            try:
                cantidadVentas=int(input("--> "))
                if cantidadVentas>0:
                    break
                else:
                    print("Ingrese un valor positivo o distinto de cero.")
            except:
                print("Ingrese un valor valido")
        for i in range(cantidadVentas):
            print(f"Ingrese el monto de la venta n°{i+1}")
            while True:
                try:
                    monto=int(input("--> "))
                    if monto>0:
                        break
                    else:
                        print("El monto no puede ser negativo.")
                except:
                    print("Ingrese un valor valido.")

            totalVentas += monto
            contadorTotal += 1

            if monto > 10000:
                contadorMayor += 1
                totalMayor += monto
            else:
                contadorMenor += 1
                totalMenor += monto


        '''
        Al elegir la opción 2, el programa debe mostrar:
        Cantidad total de ventas registradas.
        ● Monto total vendido.
        ● Cantidad de ventas mayores a 10000.
        ● Cantidad de ventas menores o iguales a 10000.
        ● Promedio general de ventas, solo si se ingresó al menos una venta.
        ● Promedio de las ventas mayores a 10000, solo si existe al menos una.
        ● Promedio de las ventas menores o iguales a 10000, solo si existe al menos una.
        '''

    elif opc==2:
        print("---------------------------")
        print("2. Mostrar Reporte")
        print("---------------------------")
        print(f"Cantidad total de ventas registradas: {contadorTotal}")
        print(f"Monto total vendido: {totalVentas}")
        print(f"Cantidad de ventas mayores a 10000: {contadorMayor}")
        print(f"Cantidad de ventas menores o iguales a 10000: {contadorMenor}")

        if contadorTotal > 0:
            promedioGeneral = totalVentas / contadorTotal
            print(f"Promedio general de ventas: {round(promedioGeneral,1)}")
            if contadorMayor > 0:
                promedioMayor = totalMayor / contadorMayor
                print(f"Promedio de las ventas mayores a 10000: {round(promedioMayor,1)}")

            if contadorMenor > 0:
                promedioMenor = totalMenor / contadorMenor
                print(f"Promedio de las ventas menores o iguales a 10000: {round(promedioMenor,1)}")
        else:
            print("No hay ventas registradas.")

        

    elif opc==3:
        print("---------------------------")
        print("3. Salir")
        print("---------------------------")
        print("Hasta pronto, Usuario.")
        break




