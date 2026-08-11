import os
contador = 0
contador2 = 0
ESPACIO = 60
utilizar = 0
liberar = 0

while True:
    print("===Menu Principal===")
    print("1. Espacios Disponibles")
    print("2. Ocupar Espacios")
    print("3. Liberar Espacio")
    print("4. Historial De Ocupaciones")
    print("5. Salir")
    opc = int(input("ingrese una opcion: "))
    if opc <1 or opc >=6 :
        os.system ("cls")
        print("Ingrese una opcion valida, Intente nuevamente")
    if opc == 1:
        os.system ("cls")
        print("Quedan",ESPACIO,"Espacios","Disponibles")   
    if opc == 2:
        while True:
            os.system ("cls")
            utilizado = int(input("ingrese la cantidad de espacios a ocupar: "))
            if utilizado <=0:
                print("debe de ingresar un valor mayor a 0")
                continue
            if utilizado > ESPACIO:
                print("debe de utilizar un valor no mayor al disponible")
                continue
            else:
                utilizar += utilizado
                contador+1
                ESPACIO -= utilizado
                break
    if opc ==3:
        while True:
            os.system ("cls")
            try:
                desocupar = int(input("ingrese la cantidad de espacios a desocupar: "))
                if desocupar > utilizado:
                    print("debe de ingresar un valor no mayor al ocupado ")
                    continue
                if desocupar <=0:
                    print("ingrese un valor mayor a 0")
                    continue
                else:
                    liberar += desocupar
                    ESPACIO += desocupar
                    break
            except ValueError as e:
                print("Solo se pueden utilizar numeros enteros",e)
    if opc ==4:
        print("==Historial De Ocupaciones==")
    if opc == 5:
        print("Operacion Finalizada")
        break