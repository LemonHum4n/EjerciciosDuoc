'''
Ejercicio 4
Genera 40 números aleatorios entre 1 y 200 y suma únicamente los que sean múltiplos de
5
'''
import random
suma=0

for i in range(40):
    numero = random.randint(1,200)
    if numero % 5==0:
        suma+=numero

print("Suma total= ",suma)