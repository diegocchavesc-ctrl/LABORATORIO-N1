import math

def rectangular_cilindrica(x, y, z):
    r = math.sqrt(x*2 + y*2)
    theta = math.atan2(y, x)  
    return r, theta, z
#ingresamos los valores
x = float(3)
y = float(2)
z = float(5)

r, theta, z_cil = rectangular_cilindrica(x, y, z)

print("\nCoordenadas cilíndricas:")
print(f"r = {r}")
print(f"theta (rad) = {theta}")
print(f"theta (grados) = {math.degrees(theta)}")
print(f"z = {z_cil}")

# rectacngular a esferica 

def rectangular_esferica(x1, y1, z1):
    
    re = math.sqrt(x1**2 + y1**2 + z1**2)    
    theta = math.atan2(y1, x1)

    if re == 0:
        phi = 0
    else:
        phi = math.acos(z1 / re)        
    return re, theta, phi

x1, y1, z1 = 1, 1, 1
r1, t, p = rectangular_esferica(x1, y1, z1)
print("\nCoordenadas cilíndricas:")
print(f"Radio (rho): {r1:.2f}")
print(f"Ángulo (theta): {math.degrees(t):.2f}°")
print(f"Ángulo (phi): {math.degrees(p):.2f}°")