


precioAuto=3000
precioMoto=1500
precioCamioneta=4000
aPagar=0


totalEstacionamientos=5
totalOcupados=0

totalAutos=0
totalMotos=0
totalCamionetas=0

totalVehiculos=0
totalPagado=0

while True:
    print("========================")
    print("1. Registrar entrada vehiculo")
    print("2. Registrar salida de vehiculo")
    print("3. Visualizar estado del estacionamiento")
    print("4. Reporte general del estacionamiento")
    print("5. Salir")
    print("========================")
    print("Ingrese la opcion.")
    while True:
        try:
            opc=int(input("--> "))
            if 1 <= opc <= 5:
                break
            elif opc==0:
                print("No se puede ingresar cero.")
            else:
                print("Valor fuera de rango. (1,2,3,4,5)")
        except:
            print("Valor incorrecto.")
    
    if opc==1:
        print("========================")
        print("1. Registrar entrada vehiculo")
        print("========================")
        if totalEstacionamientos>0:

            print("- Autos      ($3000/h)")
            print("- Motos      ($1500/h)")
            print("- Camionetas ($4000/h)")
            print("========================")
            print("Ingrese tipo de vehiculo.")
            while True:
                tipoVehiculo=input("--> ")
                tipoVehiculo= tipoVehiculo.upper()
                tipoVehiculo= tipoVehiculo.replace(" ","")

                if tipoVehiculo=="AUTO" or tipoVehiculo=="AUTOS":
                    totalAutos+=1
                    totalEstacionamientos-=1
                    
                    break
                elif tipoVehiculo=="MOTO" or tipoVehiculo=="MOTOS":
                    totalMotos+=1
                    totalEstacionamientos-=1
                    
                    break
                elif tipoVehiculo=="CAMIONETA" or tipoVehiculo=="CAMIONETAS":
                    totalCamionetas+=1
                    totalEstacionamientos-=1
                    
                    break
                else:
                    print("Tipo de vehiculo invalido. Intente nuevamente.")
            totalOcupados+=1
            totalVehiculos+=1
        else:
            print("No hay estacionamientos disponibles.")
        
        

    elif opc==2:
        print("========================")
        print("2. Registrar salida de vehiculo")
        print("========================")
        if totalOcupados>0:

            print("- Autos      ($3000/h)")
            print("- Motos      ($1500/h)")
            print("- Camionetas ($4000/h)")
            print("========================")
            print("Ingrese tipo de vehiculo a salir.")
            while True:
                tipoVehiculo=input("--> ")
                tipoVehiculo= tipoVehiculo.upper()
                tipoVehiculo= tipoVehiculo.replace(" ","")

                if (tipoVehiculo=="AUTO" or tipoVehiculo=="AUTOS") and totalAutos>0:
                    totalAutos-=1
                    aPagar=precioAuto
                    break
                elif (tipoVehiculo=="MOTO" or tipoVehiculo=="MOTOS") and totalMotos>0:
                    totalMotos-=1
                    aPagar=precioMoto
                    break
                elif (tipoVehiculo=="CAMIONETA" or tipoVehiculo=="CAMIONETAS") and totalCamionetas>0:
                    totalCamionetas-=1
                    aPagar=precioCamioneta
                    break
                elif totalAutos==0 or totalMotos==0 or totalCamionetas==0:
                    print("No hay estacionamientos ocupados para ese tipo de vehiculo.")
                else:
                    print("Tipo de vehiculo invalido. Intente nuevamente.")
            print("========================")
            print("Ingrese cantidad de horas de estacionamiento.")
            while True:
                try:
                    cantidadHoras=(int(input("-->")))
                    if cantidadHoras==0:
                        print("Las horas no pueden ser cero")
                    else:
                        break
                except:
                    print("Tipo de valor incorrecto, intente nuevamente.")
            
            totalAPagar=aPagar*cantidadHoras
            totalPagado+=totalAPagar
            print("========================")
            print(f"Tipo Vehiculo:                  {tipoVehiculo.capitalize()}")
            print(f"Total horas de estacionamiento: {cantidadHoras} horas.")
            print(f"Total a pagar:                  ${totalAPagar}")
            print("========================")
            totalEstacionamientos+=1
            totalOcupados-=1
        else:
            print("No hay estacionamientos ocupados.")



    elif opc==3:
        print("========================")
        print("3. Visualizar estado del estacionamiento")
        print("========================")
        print(f"Estacionamientos utilizados:            {totalOcupados} estacionamientos ocupados.")
        print(f"Estacionamientos disponibles:           {totalEstacionamientos} estacionamientos.")
        print(f"Capacidad maxima del estacionamiento:   5 Estacionamientos")
        print(f"Estacionamientos utilizados por: ")
        print(f"    Auto:       {totalAutos} Autos")
        print(f"    Moto:       {totalMotos} Motos")
        print(f"    Camionetas: {totalCamionetas} Camionetas")
        print("========================")

    elif opc==4:
        print("========================")
        print("4. Reporte general del estacionamiento")
        print("========================")
        print(f"Cantidad de vehiculos estacionados en el dia: {totalVehiculos} vehiculos.")
        print(f"Cantidad recaudado en el dia:                 ${totalPagado}")
        print("========================")
    
    elif opc==5:
        print("========================")
        print("5. Salir")
        print("========================")
        print("Hasta pronto, Usuario.")
        break
            
