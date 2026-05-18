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
while True:
    print("---------------------------")
    print("1. Ingresar ventas de productos.")
    print("2. Mostrar reporte.")
    print("3. Salir.")
    print("---------------------------")
    print("Ingrese una opcion.")
    try:
        opc=int(input("-->"))
        if opc>=1 or opc>=3:
            print("Ingrese una opcion valida. Entre 1 al 3.")
            
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
        while True:
            try:
                cantidadVentas=int(input("-->"))
                if cantidadVentas>=0:
                    break
                else:
                    print("Ingrese un valor positivo.")
            except:
                print("Ingrese un valor valido")
        for i in range(cantidadVentas):
            print(f"Ingrese la venta nº{}")
        

    elif opc==2:
        print("---------------------------")
        print("2. Mostrar Reporte")
        print("---------------------------")
    elif opc==3:
        print("---------------------------")
        print("3. Salir")
        print("---------------------------")
        print("Hasta pronto, Usuario.")
        break




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