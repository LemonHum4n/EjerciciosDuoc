'''
Ejercicio 9
Genera 60 números aleatorios entre 1 y 100.
Clasifica cada número en:
● Zona baja: 1 a 33
● Zona media: 34 a 66
● Zona alta: 67 a 100
Debes:
● Contar cuántos números cayeron en cada zona
'''
import random

contadorBaja=0
contadorMedia=0
contadorAlta=0

for i in range(60):
    numero=random.randint(1,100)
    if numero>=1 and numero<=33:
        contadorBaja+=1
    elif numero>=34 and numero<=66:
        contadorMedia+=1
    elif numero>=67 and numero<=100:
        contadorAlta+=1

print("Zona baja: ", contadorBaja)
print("Zona media: ", contadorMedia)
print("Zona alta: ", contadorAlta)