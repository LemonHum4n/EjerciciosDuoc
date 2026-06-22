def menu():
    while True:
        print("=======================")
        print("1. Agregar tarea")
        print("2. Buscar tarea")
        print("3. Eliminar tarea")
        print("4. Actualizar estado de tarea")
        print("5. Mostrar tareas")
        print("6. Salir")
        print("=======================")
        print("     Ingrese una opcion.")
        try:
            opc=int(input("-->"))
            if opc<0:
                print("No se permiten valores negativos.")
            else:
                break
                
        except:
            print("Valor invalido.")
    return opc

def validarNumeroPositivo(mensaje:str):
    print(mensaje)
    while True:
        try:
            numero=int(input("-->"))
            if numero<0:
                print("No se permiten numeros negativos.")
            else:
                break
        except:
            print("Valor invalido.")
    return numero

def validarString(mensaje:str):
    print(mensaje)
    while True:
        try:
            palabra=input("-->")
            if palabra.replace(" ","")=="":
                print("No se puede ingresar un espacio vacio.")
            else:
                break
        except:
            print("Valor invalido.")

def validarEstado(mensaje:str):
    print(mensaje)
    while True:
        try:
            estado=input("-->")
            if estado.replace(" ","")=="":
                print("No se puede ingresar un espacio vacio.")
            else:
                estado=estado.replace(" ","").upper()
                if estado=="PENDIENTE" or estado=="ENPROCESO" or "COMPLETADA":
                    break
                
            
        except:
            print("Valor invalido.")







while True:
    opc=menu()

    if opc==1:
        print("=======================")
        print("1. Agregar tarea")
        print("=======================")
        idTarea=validarNumeroPositivo("Ingrese Id de la tarea.")
        print("=======================")
        nombre=validarString("Ingrese nombre o titulo de la tarea.")
        print("=======================")
        responsable=validarString("Ingrese responsable de la tarea.")
        print("=======================")
        



    elif opc==2:
        print("=======================")
        print("2. Buscar tarea")
        print("=======================")

    elif opc==3:
        print("=======================")
        print("3. Eliminar tarea")
        print("=======================")

    elif opc==4:
        print("=======================")
        print("4. Actualizar estado de tarea")
        print("=======================")

    elif opc==5:
        print("=======================")
        print("5. Mostrar tareas")
        print("=======================")
    
    elif opc==6:
        print("=======================")
        print("6. Salir")
        print("=======================")
        print("Hasta luego, Usuario.")
        break
    
    else:
        print(f"     ¡Opcion {opc} no existe! Ingrese una opcion valida.")