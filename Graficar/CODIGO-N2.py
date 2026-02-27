import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

print("--- Análisis de Sistema de Segundo Orden ---")

# 1. Entrada de datos (según la fórmula G(s) de la imagen)
k = float(input("Ingrese la ganancia (K): "))
wn = float(input("Ingrese la frecuencia natural (wn): "))
zeta = float(input("Ingrese el factor de amortiguamiento (zeta): "))

# 2. Definición de la función de transferencia
# Numerador: K * wn^2
# Denominador: s^2 + 2*zeta*wn*s + wn^2
num = [k * (wn**2)]
den = [1, 2 * zeta * wn, wn**2]

sistema = ctrl.TransferFunction(num, den)

# 3. Lógica para determinar el tipo de sistema
if 0 < zeta < 1:
    tipo = "Subamortiguado"
elif zeta == 1:
    tipo = "Criticamente amortiguado"
elif zeta > 1:
    tipo = "Sobreamortiguado"
elif zeta == 0:
    tipo = "Oscilatorio (Sin amortiguamiento)"
else:
    tipo = "Inestable"

print(f"\nResultado: El sistema es {tipo}")

# 4. Cálculo de la respuesta temporal (Escalón)
tiempo, respuesta = ctrl.step_response(sistema)

# 5. Graficación

plt.figure(figsize=(8, 5))
plt.plot(tiempo, respuesta, 'r-', linewidth=1.5, label=f'zeta = {zeta}')
plt.title(f'Respuesta al Escalón ({tipo})')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.show()