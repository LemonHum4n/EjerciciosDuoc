'''
Ejercicio 8
Solicita 10 números e imprime la suma de los que sean mayores que 100
'''

suma=0

for i in range(10):
    print(f"Ingrese el numero n°{i+1}")
    numero=int(input("-->"))
    if numero>100:
        suma+=numero

print("Suma de los numeros mayores a 100: ", suma)