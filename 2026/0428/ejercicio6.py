'''
Ejercicio 6
Genera 80 números aleatorios entre 1 y 100 y cuenta cuántos quedaron entre 30 y 70
'''
import random

contador=0

for i in range(80):
    numero= random.randint(1,100)

    if numero>=30 and numero<=70:
        contador+=1

print("Cantidad de numeros entre 30 y 70 = ", contador)