'''
Ejercicio 5
Pide 10 números y luego pide un número extra para buscar. Indica cuántas veces apareció
ese valor
'''

numeros=""

for i in range(10):
    print("Ingrese un numero")
    numero=int(input("-->"))
    numeros+=str(numero)

print("Ingrese un numero extra a buscar")
numeroBuscar=int(input("-->"))

contadorNumeroBuscar=0

for i in numeros:
    if i == str(numeroBuscar):
        contadorNumeroBuscar+=1

print(numeros)

print(f"Cantidad de veces que aparece el numero {numeroBuscar} : {contadorNumeroBuscar}")