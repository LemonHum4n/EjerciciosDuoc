contadorPositivo= 0

for i in range(10):
    print("Ingrese un numero")
    numero=int(input("-->"))
    if numero>=0:
        contadorPositivo+=1
    
print(f"La cantidad de numeros positivos registrados son {contadorPositivo}")
    