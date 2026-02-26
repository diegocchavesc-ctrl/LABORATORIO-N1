import numpy as np #importar librerías para cálculos numéricos y gráficos
import matplotlib.pyplot as plt #importar librerías para cálculos numéricos y gráficos

# Constantes PT100
R0 = 100
alpha = 0.00385

# Rango de temperatura
temperatura = np.linspace(-200, 200)

# Calcular resistencia
resistencia = R0 * (1 + alpha * temperatura)

# Crear gráfica
plt.figure()
plt.plot(temperatura, resistencia)

plt.title("Comportamiento de la PT100")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ohm)")
plt.grid()

plt.show()