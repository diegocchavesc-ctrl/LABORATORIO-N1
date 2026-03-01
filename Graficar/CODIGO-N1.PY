import numpy as np
import matplotlib.pyplot as plt

# Constantes PT100 IEC 60751
R0 = 100

A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

# Rango de temperatura
temperatura = np.linspace(-200, 200, 400)

# Crear array de resistencia vacío
resistencia = np.zeros_like(temperatura)

# Aplicar ecuación correcta según rango
for i, T in enumerate(temperatura):
    if T >= 0:
        resistencia[i] = R0 * (1 + A*T + B*T**2)
    else:
        resistencia[i] = R0 * (1 + A*T + B*T**2 + C*(T-100)*T**3)

# Graficar
plt.figure()
plt.plot(temperatura, resistencia)

plt.title("Comportamiento real de la PT100 (Callendar-Van Dusen)")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ohm)")
plt.grid()

plt.show()