import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = float(input("Ingrese coordenada X: "))
y = float(input("Ingrese coordenada Y: "))
z = float(input("Ingrese coordenada Z: "))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

lim = max(abs(x), abs(y), abs(z)) + 1

ax.plot([0, lim], [0, 0], [0, 0])  # eje X
ax.plot([0, 0], [0, lim], [0, 0])  # eje Y
ax.plot([0, 0], [0, 0], [0, lim])  # eje Z

#vector
ax.quiver(0, 0, 0, x, y, z)

ax.text(x, y, z, f"({x}, {y}, {z})")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Vector en sistema coordenado 3D")

ax.set_xlim([0, lim])
ax.set_ylim([0, lim])
ax.set_zlim([0, lim])

plt.show()