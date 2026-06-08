diccionario = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "juegos_favoritos": ["Minecraft", "Roblox"],
    "edad": 12,
    "casado": False,
    "hermanos":[
        {
            "nombre": "Diego",
            "apellido": "Perez"
        },
        {
            "nombre":"Pedrito",
            "apellido":"Perez"
        }
    ]
}

print(diccionario["hermanos"][1]["nombre"])
# Pedrito

for i in diccionario["hermanos"]:
    print(i["Nombre"])

print(diccionario.get("nombree")) #No da excepciones si la clave no existe
print(diccionario["nombree"]) #Da excepcion si la clave no existe