'''
Ejercicio 6
Sumar números hasta que el usuario escriba 0
'''

numero=1
suma=0

while numero!=0:
    print("Ingrese un numero")
    numero=int(input("-->"))
    suma+=numero

print(f"Numeros sumados: {suma}")
       