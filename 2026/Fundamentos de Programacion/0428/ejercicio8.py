'''
Ejercicio 8
Genera 50 productos con puntajes aleatorios entre 1 y 100.
● Cuenta cuántos productos son “defectuosos” si su puntaje es menor a 40
● Cuenta cuántos son “aceptables” entre 40 y 79
● Cuenta cuántos son “excelentes” desde 80
● Acumula el total de puntajes
'''
import random

contadorDefectuoso=0
contadorAceptable=0
contadorExcelente=0
totalPuntajes=0

for i in range(50):
    puntaje=random.randint(1,100)

    if puntaje<40:
        contadorDefectuoso+=1
    elif puntaje>=40 or puntaje<=79:
        contadorAceptable+=1
    elif puntaje>=80:
        contadorExcelente+=1
    totalPuntajes+=puntaje

print("Cantidad productos defectuosos: ", contadorDefectuoso)
print("Cantidad productos aceptables: ", contadorAceptable)
print("Cantidad productos excelentes: ", contadorExcelente)
print("Total acumulado puntajes: ", totalPuntajes)