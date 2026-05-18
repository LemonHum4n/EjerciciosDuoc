'''
Ejercicio 9
Pide una palabra al usuario y cuenta cuántas vocales tiene
'''

contadorVocal=0

print("Ingrese una palabra")
palabra=input("-->")

for i in palabra:
    if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
        contadorVocal+=1

print(f"Cantidad de vocales de la palabra '{palabra}' : {contadorVocal}")