import numpy as np
import matplotlib.pyplot as plt

# datos
voltaje = float(input("Ingrese el voltaje de la fuente (V): "))
resistencia = float(input("Ingrese la resistencia (Ohmios Ω): "))
cap_micro = float(input("Ingrese la capacitancia (microFaradios μF): "))

capacitancia = cap_micro * 1e-6

tau = resistencia * capacitancia
print(f"\nConstante de tiempo (τ) = {tau:.6f} segundos")

tiempo = np.linspace(0, 5*tau, 1000)

voltaje_carga = voltaje * (1 - np.exp(-tiempo / tau))
voltaje_descarga = voltaje * np.exp(-tiempo / tau)

# 6. Gráfica
plt.figure(figsize=(8,5))
plt.plot(tiempo, voltaje_carga, label="Carga del capacitor")
plt.plot(tiempo, voltaje_descarga, label="Descarga del capacitor")
plt.axvline(tau, linestyle="--", label="Constante de tiempo τ")

plt.title("Circuito RC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.legend()
plt.grid(True)

plt.show()