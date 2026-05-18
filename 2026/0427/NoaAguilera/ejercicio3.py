'''
Ejercicio 3
Pide 8 números al usuario y muestra cuántos son pares
'''

contadorPares=0

for i in range(8):
    print("Ingrese un numero")
    numero=int(input("-->"))

    if numero%2 ==0:
        contadorPares+=1

print(f"Cantidad de numeros pares: {contadorPares}")