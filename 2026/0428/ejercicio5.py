'''
Ejercicio 5
Genera 30 temperaturas aleatorias entre -5 y 35 grados.
Luego muestra la suma total, cuántas fueron bajo 0 grados, cuántas fueron mayores a 25
grados y el promedio general usando acumulador y contadores.
'''

import random

suma=0
contadorBajocero=0
contadorSobre25=0

for i in range(30):
    numero=random.randint(-5,35)
    suma+=numero
    if numero<0:
        contadorBajocero+=1
    elif numero>25:
        contadorSobre25+=1
    
promedio=suma/30

print("Suma total= ",suma)
print("Temperaturas bajo cero= ", contadorBajocero)
print("Temperaturas sobre 25= ", contadorSobre25)
print("Promedio temperaturas= ", promedio)