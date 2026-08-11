'''
Ejercicio 2
Genera números aleatorios entre 10 y 50 y acumúlalos hasta que la suma total supere 500
'''
import random

suma=0

while suma<500:
    numero=random.randint(10,50)
    suma+=numero

print("Suma = ",suma)