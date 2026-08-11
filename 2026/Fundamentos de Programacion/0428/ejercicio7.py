'''
Ejercicio 7
Genera números aleatorios entre 1 y 20 hasta que aparezca el número 13.
● Muestra cuántos intentos fueron necesarios
● Acumula la suma de todos los números generados antes de terminar
'''
import random

contadorIntentos=0
suma=0

while (True):
    numero=random.randint(1,20)
    
    if numero==18:
        break
    
    contadorIntentos+=1
    suma+=numero

print("Intentos realizados: ", contadorIntentos)
print("Suma total: ", suma)
    