'''
Ejercicio 2
Solicita 5 números e imprime la suma total
'''

suma=0
for i in range(5):
    print("Ingrese un numero")
    numero=int(input("-->"))
    suma+=numero

print(f"La suma total es {suma}")