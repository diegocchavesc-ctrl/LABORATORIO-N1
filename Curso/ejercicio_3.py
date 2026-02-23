import math

def rectangular_cilindrica(x, y, z):
    r = math.sqrt(x*2 + y*2)
    theta = math.atan2(y, x)  
    return r, theta, z
x = float(3)
y = float(2)
z = float(5)

r, theta, z_cil = rectangular_cilindrica(x, y, z)

print("\nCoordenadas cilíndricas:")
print(f"r = {r}")
print(f"theta (rad) = {theta}")
print(f"theta (grados) = {math.degrees(theta)}")
print(f"z = {z_cil}")