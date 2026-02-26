import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

a = float(input("Coef de s^2: "))
b = float(input("Coef de s: "))
c = float(input("Termino indep: "))
k = float(input("Ganancia K: "))

# Calculos z
w = np.sqrt(c/a)
z = (b/a) / (2 * w)

# Clasificación
if z < 1:
    tipo = "Subamortiguado"
elif z == 1:
    tipo = "Criticamente amortiguado"
else:
    tipo = "Sobreamortiguado"

print(f"\nZeta: {round(z, 3)}")
print(f"Sistema: {tipo}")

# Grafica
tf = ctrl.TransferFunction([k], [a, b, c])
t, y = ctrl.step_response(tf)

plt.plot(t, y)
plt.title("Respuesta sistema")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()