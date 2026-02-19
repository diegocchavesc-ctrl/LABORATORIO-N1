import math

def convertir(x, y, z):
    # --- Cilíndricas ---
    r = math.sqrt(x**2 + y**2)
    theta_cil = math.degrees(math.atan2(y, x))
    z_cil = z

    # --- Esféricas ---
    rho = math.sqrt(x**2 + y**2 + z**2)
    theta_esf = math.degrees(math.atan2(y, x))
    
    if rho != 0:
        phi = math.degrees(math.acos(z / rho))
    else:
        phi = 0

    return r, theta_cil, z_cil, rho, theta_esf, phi


# Entrada de datos
x = float(input("Ingrese x: "))
y = float(input("Ingrese y: "))
z = float(input("Ingrese z: "))

# Conversión
r, theta_cil, z_cil, rho, theta_esf, phi = convertir(x, y, z)

# Resultados
print("\n--- Coordenadas Cilíndricas ---")
print("r =", round(r, 4))
print("θ =", round(theta_cil, 4), "grados")
print("z =", round(z_cil, 4))

print("\n--- Coordenadas Esféricas ---")
print("ρ =", round(rho, 4))
print("θ =", round(theta_esf, 4), "grados")
print("φ =", round(phi, 4), "grados")
