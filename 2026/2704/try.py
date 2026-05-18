try:
    a=int(input("-->"))
    resultado= 10/a
except ZeroDivisionError as nombre_de_excepcion:
    print(f"Se produjo una excepcion: {nombre_de_excepcion}")
except:
    print("Error de tipo")
else:
    print("No se produjo ninguna excepcion")
    print(resultado)
finally:
    print("Este bloque se ejecuta siempre")