'''
Ejercicio 10
Genera 100 monedas aleatorias usando 0 y 1.
● Considera 0 = sello, 1 = cara
● Cuenta cuántas caras y cuántos sellos salieron
● Acumula cuántos puntos gana un jugador si recibe 2 puntos por cada cara
'''

import random
contadorSello=0
contadorCara=0

for i in range(100):
    moneda=random.randint(0,1)
    if moneda==0:
        contadorSello+=1
    elif moneda==1:
        contadorCara+=1

puntaje=contadorCara*2
print("Cantidad sellos: ", contadorSello)
print("Cantidad caras: ", contadorCara)
print("Puntaje total: ", puntaje)