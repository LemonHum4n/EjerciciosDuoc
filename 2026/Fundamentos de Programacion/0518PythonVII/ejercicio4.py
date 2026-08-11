'''
Desarrolle un programa en Python que simule el control de consumo de agua de una
vivienda mediante un menú con estas opciones:
1. Registrar consumo mensual.
2. Mostrar informe.
3. Salir.
En la opción 1, el programa debe pedir cuántos meses desea registrar. Luego, con un ciclo
for, solicitará los litros consumidos en cada mes. Debe usar try y except para controlar
errores de ingreso y aceptar solo números positivos.


'''
litroTotal=0
contadorSuperior=0
contadorMenor=0
acumuladorLitroSuperior=0
acumuladorLitroMenor=0

while True:
    print("-------------")
    print("1. Registrar consumo mensual")
    print("2. Mostrar informe")
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
        print("1. Registrar consumo mensual")
        print("-------------")
        print("Ingrese cantidad de meses a registrar.")
        while True:
            try:
                cantidadMeses=int(input("--> "))
                if cantidadMeses>0:
                    break
                else:
                    print("Ingrese un valor positivo o distinto de cero.")
            except:
                print("Ingrese un valor valido")
        for i in range(cantidadMeses):
            print(f"Ingrese cantidad de litros consumidos del mes n°{i+1}")
            while True:
                try:
                    litro=int(input("--> "))
                    if 0<=litro:
                        break
                    else:
                        print("El litro no es valido.")
                except:
                    print("Ingrese un valor numerico.")
            '''
            El programa debe trabajar con:
            ● Un acumulador para el consumo total.
            ● Un contador para meses con consumo superior a 15000 litros.
            ● Un contador para meses con consumo menor o igual a 15000 litros.
            ● Acumuladores separados para ambos tipos de consumo.
            '''
            litroTotal+=litro

            if litro >15000:
                contadorSuperior+=1
                acumuladorLitroSuperior+=litro
            else:
                contadorMenor+=1
                acumuladorLitroMenor+=litro

            
            

    if opc==2:
        print("-------------")
        print("2. Mostrar Informe")
        print("-------------")
        '''
        En la opción 2, deberá mostrar el total consumido, el promedio mensual, cuántos meses
        superaron el límite indicado y cuántos no. El menú debe mantenerse en ejecución con while
        hasta la opción de salida.
        '''
        if (contadorMenor+contadorSuperior)==0:
            print("No hay litros registrados.")
        else:
            promedio=litroTotal/(contadorMenor+contadorSuperior)
            print(f"Litros total consumidos: {litroTotal}")
            print(f"Promedio mensual consumido: {promedio}")
            print(f"Meses que superaron el limite indicado: {contadorSuperior}")
            print(f"Meses que no se superaron el limite indicado: {contadorMenor}")


    if opc==3:
        print("-------------")
        print("3. Salir")
        print("-------------")
        print("Hasta luego, Usuario")
        break