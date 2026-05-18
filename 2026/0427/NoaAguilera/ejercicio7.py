'''
Ejercicio 7
Pide 15 números al usuario y muestra cuántos son múltiplos de 3
'''

contadorMultiplos=0

for i in range(15):
    print(f"Ingrese el numero n°{i+1}")
    numero=int(input("-->"))
    if numero % 3 == 0:
        contadorMultiplos+=1

print("Cantidad de numeros multiplos de 3: ", contadorMultiplos)