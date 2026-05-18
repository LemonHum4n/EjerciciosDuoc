'''
Ejercicio 4
Solicita 10 números y suma únicamente los positivos
'''

suma=0

for i in range(10):
    print("Ingrese un numero")
    numero=int(input("-->"))

    if numero >=0:
        suma+=numero

print("Suma total: ", suma)