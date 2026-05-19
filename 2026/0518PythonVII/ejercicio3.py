'''
Desarrolle un programa en Python para un gimnasio que muestre un menú con las
siguientes opciones:
1. Registrar días de entrenamiento.
2. Ver resumen.
3. Salir.
'''
totalMinutos=0
contadorDiasMas60=0
contadorDiasMenos60=0
contadorMinutosMas60=0
contadorMinutosMenos60=0
totalDias=0

while True:
    print("-------------")
    print("1. Registrar dias de entrenamiento")
    print("2. Ver resumen")
    print("3. Salir")
    print("-------------")

    try:
        opc=int(input("-->"))
        if opc>3 or opc <1:
            print("Ingrese una opcion valida del 1 al 3.")
    except:
        print("Ingrese un valor numerico")
        continue

    if opc==1:
        print("-------------")
        print("1. Registrar dias de entrenamiento")
        print("-------------")

        '''
        En la opción 1, el usuario indicará cuántos días desea registrar. Luego, usando un ciclo for,
        en cada día deberá ingresar la cantidad de minutos entrenados. El programa debe validar
        con manejo de excepciones que el dato ingresado sea entero positivo.
        Durante el proceso, el programa debe:
        ● Acumular el total de minutos entrenados.
        ● Contar cuántos días entrenó 60 minutos o más.
        ● Contar cuántos días entrenó menos de 60 minutos.
        ● Acumular por separado los minutos de ambos grupos.
        '''
        print("Ingrese cantidad de dias a registrar")
        while True:
            try:
                cantidadDias=int(input("--> "))
                if cantidadDias>0:
                    break
                else:
                    print("Ingrese un valor positivo o distinto de cero.")
            except:
                print("Ingrese un valor valido")
        for i in range(cantidadDias):
            print(f"Ingrese minutos entrenados del dia n°{i+1}")
            while True:
                try:
                    minutos=int(input("--> "))
                    if minutos>=0:
                        break
                    else:
                        print("Los minutos no son validos.")
                except:
                    print("Ingrese un valor numerico.")
            totalMinutos+=minutos

            if minutos>=60:
                contadorDiasMas60+=1
                contadorMinutosMas60+=minutos
            else:
                contadorDiasMenos60+=1
                contadorMinutosMenos60+=minutos

            totalDias+=1


    '''
    En la opción 2, se debe mostrar la cantidad de días registrados, el total de minutos, el
    promedio de minutos por día y los contadores de días según su duración. El menú debe
    repetirse con while hasta que el usuario seleccione salir, y toda entrada inválida debe
    manejarse con captura de excepciones.
    '''
    if opc==2:
        print("-------------")
        print("2. Ver Resumen.")
        print("-------------")
        if totalDias==0:
            print("No hay dias registrados.")
        else:
            promedioMinutos = totalMinutos / totalDias
            print(f"Cantidad de dias registrados: {totalDias}")
            print(f"Total de minutos registrados: {totalMinutos}")
            print(f"Promedio de minutos por dia: {round(promedioMinutos,1)}")
            print(f"Dias con 60 minutos o más: {contadorDiasMas60}")
            print(f"Dias con menos de 60 minutos: {contadorDiasMenos60}")
            print(f"Minutos totales en dias de 60 o más: {contadorMinutosMas60}")
            print(f"Minutos totales en dias de menos de 60: {contadorMinutosMenos60}")

    if opc==3:
        print("-------------")
        print("3. Salir")
        print("-------------")
        print("Hasta luego, Usuario")