'''
Ejercicio 2
Desarrolle un programa en Python que presente un menú con estas opciones:
● Registrar notas de estudiantes.
● Mostrar estadísticas.
● Salir.
En la opción 1, el usuario debe indicar cuántas notas ingresará. Luego, mediante un ciclo
for, el programa pedirá cada nota y deberá validar con excepciones que sea numérica.
Considere notas entre 1.0 y 7.0; si se ingresa un valor fuera de rango, debe mostrarse un
mensaje y no considerarse en los cálculos.
El programa debe usar contadores y acumuladores para determinar:
● Cantidad de notas aprobadas.
● Cantidad de notas reprobadas.
● Suma total de notas válidas.
● Nota mayor ingresada.
● Nota menor ingresada.

'''

contadorNotas=0
contadorAprobados=0
contadorReprobadas=0
notaMayor=1.0
notaMenor=7.0
sumaTotal=0
while True:
    print("-------------")
    print("1. Registrar notas de estudiantes")
    print("2. Mostrar estadisticas")
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
        print("1. Registrar notas de estudiantes.")
        print("-------------")
        print("Ingrese cantidad de notas a registrar")
        while True:
            try:
                cantidadNotas=int(input("--> "))
                if cantidadNotas>0:
                    break
                else:
                    print("Ingrese un valor positivo o distinto de cero.")
            except:
                print("Ingrese un valor valido")
        for i in range(cantidadNotas):
            print(f"Ingrese la nota n°{i+1}")
            print("Formato: x.x")
            while True:
                try:
                    nota=float(input("--> "))
                    if 1.0<=nota<=7.0:
                        break
                    else:
                        print("La nota no es valida.")
                except:
                    print("Ingrese un valor numerico.")

            sumaTotal+=nota

            contadorNotas+=1

            if nota>notaMayor:
                notaMayor=nota
            
            if nota<notaMenor:
                notaMenor=nota

            if nota >= 4.0:
                contadorAprobados += 1
            else:
                contadorReprobadas += 1
    
    elif opc==2:
        print("-------------")
        print("2. Mostrar estadisticas")
        print("-------------")
        '''
        En la opción 2, debe mostrar el total de notas válidas, el promedio general, la cantidad de
        aprobados y reprobados, y el porcentaje de aprobación. El menú debe mantenerse activo
        con while hasta seleccionar salir, controlando entradas inválidas con try y except.
        '''
        if contadorNotas==0:
            print("No hay notas ingresadas.")
        else:
            print(f"Total de notas válidas: {contadorNotas}")
            promedioGeneral=sumaTotal/contadorNotas
            print(f"Promedio general: {round(promedioGeneral,1)}")
            print(f"Cantidad aprobados: {contadorAprobados}")
            print(f"Cantidad reprobados: {contadorReprobadas}")
            porcentaje_aprobacion = (contadorAprobados / contadorNotas) * 100
            print(f"Porcentaje de aprobación: {round(porcentaje_aprobacion,1)}%")


    elif opc==3:
        print("-------------")
        print("3. Salir")
        print("-------------")
        print("Hasta luego, Usuario.")
        break

