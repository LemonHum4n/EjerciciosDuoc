# Codigo de Noa Aguilera :v

mapasAmongUs = [
    {   "mapa": "The Skeld",
        "fecha_lanzamiento": "2018-06-15",
        "tamanio": "Pequeño",
        "numero_ubicaciones": 14,
        "numero_tareas": 17,
        "orden": 1
    },
    {   "mapa": "MIRA HQ",
        "fecha_lanzamiento": "2019-08-08",
        "tamanio": "Muy pequeño",
        "numero_ubicaciones": 14,
        "numero_tareas": 19,
        "orden": 2
    },
    {   "mapa": "Polus",
        "fecha_lanzamiento": "2019-11-12",
        "tamanio": "Grande",
        "numero_ubicaciones": 15,
        "numero_tareas": 24,
        "orden": 3
    },
    {   "mapa": "The Airship",
        "fecha_lanzamiento": "2021-03-31",
        "tamanio": "Muy grande",
        "numero_ubicaciones": 17,
        "numero_tareas": 22,
        "orden": 4
    },
    {   "mapa": "The Fungle",
        "fecha_lanzamiento": "2023-10-24",
        "tamanio": "Grande",
        "numero_ubicaciones": 18,
        "numero_tareas": 25,
        "orden": 5
    }
]

rolesAmongUs = [
    {   "rol": "Crewmate",
        "tipo": "Tripulación",
        "fecha_lanzamiento": "2018-06-15",
        "descripcion": "Completa tareas y vota para eliminar Impostores.",
    },
    {   "rol": "Impostor",
        "tipo": "Impostor",
        "fecha_lanzamiento": "2018-06-15",
        "descripcion": "Elimina tripulantes, sabotea el mapa y usa ventilaciones sin ser descubierto.",
    },
    {   "rol": "Scientist",
        "tipo": "Tripulación",
        "fecha_lanzamiento": "2021-11-09",
        "descripcion": "Puede ver los signos vitales de todos los jugadores desde cualquier lugar.",
    },
    {   "rol": "Engineer",
        "tipo": "Tripulación",
        "fecha_lanzamiento": "2021-11-09",
        "descripcion": "Puede usar ventilaciones como los Impostores para moverse rápido.",
    },
    {   "rol": "Guardian Angel",
        "tipo": "Tripulación (Fantasma)",
        "fecha_lanzamiento": "2021-11-09",
        "descripcion": "Al morir, puede escudar a un Crewmate vivo para protegerlo de ser asesinado.",
    },
    {   "rol": "Shapeshifter",
        "tipo": "Impostor",
        "fecha_lanzamiento": "2021-11-09",
        "descripcion": "Puede transformarse en la apariencia de cualquier otro jugador.",
    },
    {   "rol": "Tracker",
        "tipo": "Tripulación",
        "fecha_lanzamiento": "2024-06-18",
        "descripcion": "Puede rastrear la posición de un jugador en el minimapa.",
    },
    {   "rol": "Noisemaker",
        "tipo": "Tripulación",
        "fecha_lanzamiento": "2024-06-18",
        "descripcion": "Al ser asesinado, emite una alerta que revela la ubicación del crimen.",
    },
    {   "rol": "Phantom",
        "tipo": "Impostor",
        "fecha_lanzamiento": "2024-06-18",
        "descripcion": "Puede volverse invisible temporalmente para moverse sin ser visto.",
    },
    {   "rol": "Detective",
        "tipo": "Tripulación",
        "fecha_lanzamiento": "2025-09-09",
        "descripcion": "Puede inspeccionar cadáveres para obtener pistas sobre el asesino.",
    },
    {   "rol": "Viper",
        "tipo": "Impostor",
        "fecha_lanzamiento": "2025-09-09",
        "descripcion": "Puede envenenar a Crewmates para eliminarlos de forma diferida.",
    },
]

coloresAmongUsHIngles = [
    "Red", "Blue", "Green", "Pink", "Orange", "Yellow",
    "Black", "White", "Purple", "Brown", "Cyan", "Lime",
    "Maroon", "Rose", "Banana", "Coral", "Gray", "Tan",
]

coloresAmongUsEspanol = [
    "Rojo", "Azul", "Verde", "Rosa", "Naranja", "Amarillo",
    "Negro", "Blanco", "Morado", "Marrón", "Cian", "Lima",
    "Vino", "Rosaceo", "Banana", "Coral", "Gris", "Bronceado",
]



while True:
    print("==============")
    print("1. Mostrar mapas de Among Us")
    print("2. Mostrar roles de Among Us")
    print("3. Mostrar colores de Among Us")
    print("4. Salir")
    print("==============")
    while True:
        try:
            opc=int(input("-->"))
            if opc<0:
                print("La opcion no puede ser negativo.")
            elif opc==0:
                print("La opcion no puede ser cero.")
            elif opc>4:
                print("La opcion no puede ser mayor a 3.")
            else:
                break
        except:
            print("Valor incorrecto.")

    if opc==1:
        print("==============")
        print("1. Mostrar mapas de Among Us")
        for mapa in mapasAmongUs:
            print(f"Nombre:          {mapa["mapa"]}")
            print(f"Tamaño:          {mapa["tamanio"]}")
            print(f"Fecha salida:    {mapa["fecha_lanzamiento"]}")
            print(f"Numero de tareas:{mapa["numero_tareas"]}")
            print("==============")

    if opc==2:
        print("==============")
        print("2. Mostrar roles de Among Us")
        for i in rolesAmongUs:
            print(f"Tipo:        {i["rol"]}")
            print(f"Fecha:       {i["fecha_lanzamiento"]}")
            print(f"Rol:         {i["rol"]}")
            print(f"Descripcion: {i["descripcion"]}")
            print("==============")

    if opc==3:
        print("==============")
        print("3. Mostrar colores de Among Us")
        print("==============")
        for i in range(len(coloresAmongUsHIngles)):
            print(f"Color:      {coloresAmongUsHIngles[i]}")
            print(f"Traduccion: {coloresAmongUsEspanol[i]}")
            print("==============")

    if opc==4:
        print("==============")
        print("4. Salir")
        print("==============")
        break





