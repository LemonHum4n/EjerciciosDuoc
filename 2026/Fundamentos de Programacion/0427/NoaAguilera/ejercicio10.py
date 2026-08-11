'''
Ejercicio 10
Pide al usuario el valor de productos comprados. El ingreso termina cuando escriba 0.
Muestra el total a pagar
'''

suma=0
ingreso=1

while ingreso!=0:
    print("Ingrese el valor del producto")
    ingreso=int(input("-->"))

    suma+=ingreso

print(f"El total a pagar son de ${suma} pesos.")