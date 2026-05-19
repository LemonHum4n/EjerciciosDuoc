'''
Ejercicio python VIII
Ejercicio 1
Construya un programa en Python que permita gestionar un sistema simple de espacios de
almacenamiento para un almacén industrial por medio de un menú de opciones.
El programa debe comenzar con 60 espacios disponibles previamente cargados.
Interfaz del Programa
Bienvenida
¡Bienvenido al sistema de gestión de espacios del Almacén Industrial!
Menú Principal
El programa debe mostrar el siguiente menú:


Funcionalidades del Sistema




5. Salir del Sistema
Al seleccionar esta opción, el programa debe finalizar su ejecución mostrando el
mensaje:

Si el usuario desea ocupar espacios de almacenamiento, se debe validar que haya suficiente
capacidad disponible. En caso de que no haya suficientes, debe informarse al usuario. La
opción 4 debe mostrar el total de ocupaciones realizadas durante la sesión (contador
separado). El programa debe repetirse hasta que el usuario elija salir.
'''

espacioDisponible=60
cantidadOcupaciones=0
espacioOcupados=0

while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Espacios disponibles")
    print("2. Ocupar espacio")
    print("3. Liberar espacio")
    print("4. Historial de ocupaciones")
    print("5. Salir")
    while True:
        try:
            opc = int(input("--> "))
            if opc < 1 or opc > 5:
                print("Ingrese una opcion valida. Entre 1 al 5.")
                continue
            break
        except:
            print("Ingrese un dato numerico.")
    if opc==1:
        '''
        1. Espacios Disponibles
        ● Mostrar la cantidad de espacios disponibles en el almacén.
        ● Este valor debe actualizarse conforme se realicen ocupaciones o liberaciones de
        espacio.
        '''
        print("=======================")
        print("1. Espacios disponibles")
        print("=======================")
        print(f" Cantidad de espacios disponibles: {espacioDisponible} espacios.")
    
    elif opc==2:
        '''
        2. Ocupar Espacio
        ● Permite ocupar espacios de almacenamiento.
        ● Se debe solicitar la cantidad de espacios a ocupar.
        ● Este número debe cumplir las siguientes validaciones:
        o No puede ser menor o igual a 0.
        o No debe superar la cantidad de espacios de almacenamientos libres.
        '''
        print("=======================")
        print("2. Ocupar espacio")
        print("=======================")
        print("Ingrese cantidad de espacios a ocupar")
        
        if espacioDisponible==0:
            print("No hay espacios disponibles.")
        else:
            while True:
                try:
                    espaciosOcupar=int(input("-->"))
                    if espaciosOcupar<=0:
                        print("No puede ingresar un valor menor o igual a cero.")
                    elif espaciosOcupar>espacioDisponible:
                        print("La cantidad supera el almacenamiento disponible")
                    else:
                        break
                except:
                    print("Ingrese un valor numerico.")
            
            espacioOcupados+=espaciosOcupar
            cantidadOcupaciones+=1
            espacioDisponible=espacioDisponible-espaciosOcupar
            print(f"Se han ocupado {espaciosOcupar} espacios.")
            print(f"    Quedan {espacioDisponible} espacios disponibles.")

    
    elif opc==3:
        '''
        3. Liberar Espacio
        ● Permite liberar espacios de almacenamiento.
        ● Se debe solicitar la cantidad de espacios a liberar, validando que:
        ● Sea mayor a 0.
        ● No supere la capacidad máxima (60 espacios).
        ● Esta acción incrementará el número de espacios de almacenamiento disponibles.
        '''
        print("=======================")
        print("3. Liberar espacio")
        print("=======================")
        if espacioDisponible==60:
            print("No hay espacios ocupados.")
        else:
            print("¿Cuantos espacios desea liberar?")
            while True:
                try:
                    espaciosLiberar=int(input("-->"))
                    if espaciosLiberar>0:
                        if espaciosLiberar>espacioOcupados:
                            print("La cantidad de espacio a liberar es superior a los espacios ocupados.")
                        elif espaciosLiberar>60:
                            print("No se puede liberar más de 60 espacios")
                        else:
                            break
                    else:
                        print("El espacio a liberar debe ser mayor a cero.")

                    
                    
                except:
                    print("Ingrese un valor numerico.")

            espacioDisponible+=espaciosLiberar
            espacioOcupados -= espaciosLiberar
            
            print(f"Se han liberado {espaciosLiberar} espacios.")
            print(f"    Espacios ocupados: {espacioOcupados}")
            print(f"    Quedan {espacioDisponible} espacios disponibles.")
    elif opc==4:
        '''
        4. Historial de Ocupaciones
        ● Mostrar la cantidad de ocupaciones realizadas durante la sesión.
        ● Las liberaciones disminuyen el historial.
        ● Las ocupaciones aumentan el historial.
        '''
        print("=======================")
        print("4. Historial de ocupaciones")
        print("=======================")
        print(f"Total de ocupaciones : {cantidadOcupaciones}")
        print(f"Espacios actualmente ocupados : {espacioOcupados}")
        print(f"Espacios disponibles : {espacioDisponible}")

    elif opc==5:
        print("=======================")
        print("5. Salir")
        print("=======================")
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

