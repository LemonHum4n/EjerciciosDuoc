'''
Ejercicio 1
Genera 50 valores aleatorios entre 1 y 6 usando random.randint(1, 6) y muestra cuántas
veces salió cada cara
'''

import random

contador1=0
contador2=0
contador3=0
contador4=0
contador5=0
contador6=0

for i in range(50):
    valor= random.randint(1,6)

    if valor==1:
        contador1+=1
    elif valor==2:
        contador2+=1
    elif valor==3:
        contador3+=1
    elif valor==4:
        contador4+=1
    elif valor==5:
        contador5+=1
    elif valor==6:
        contador6+=1

print(f"1 = {contador1} veces")
print(f"2 = {contador2} veces")
print(f"3 = {contador3} veces")
print(f"4 = {contador4} veces")
print(f"5 = {contador5} veces")
print(f"6 = {contador6} veces")