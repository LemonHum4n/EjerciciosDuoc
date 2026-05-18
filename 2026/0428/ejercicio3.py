'''
Ejercicio 3
Genera 100 números aleatorios entre 1 y 100 e indica cuántos fueron pares y cuántos
impares
'''
import random

contadorPar=0
contadorImpar=0

for i in range(100):
    numero=random.randint(1,100)
    if numero%2==0:
        contadorPar+=1
    else:
        contadorImpar+=1

print("Cantidad de pares: ", contadorPar)
print("Cantidad de impares: ", contadorImpar)