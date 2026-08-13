import matplotlib.pyplot as plt
import numpy as np

# Importar las librerias para poder hacer las funciones

x = np.arange(0,6,00.1)
y= 120*x+2000

plt.plot(x,y)

plt.axis([0, 6, 0, 2800])

plt.xlabel("Energia utilizada ({kWh})")
plt.ylabel("Costo para usuario ($)")

plt.title("Costo para el usuario segun uso de energia")

plt.grid(True)

