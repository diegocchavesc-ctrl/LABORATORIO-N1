
# Vectores inicializados
A = [3, 4, 5]
B = [1, 2, 3]

# Suma
suma = [A[0]+B[0], A[1]+B[1], A[2]+B[2]]

# Resta
resta = [A[0]-B[0], A[1]-B[1], A[2]-B[2]]

# Producto punto
producto_punto = A[0]*B[0] + A[1]*B[1] + A[2]*B[2]

# Producto cruz
producto_cruz = [
    A[1]*B[2] - A[2]*B[1],
    A[2]*B[0] - A[0]*B[2],
    A[0]*B[1] - A[1]*B[0]
]

# División elemento a elemento
division = [A[0]/B[0], A[1]/B[1], A[2]/B[2]]

print("Suma:", suma)
print("Resta:", resta)
print("Producto punto:", producto_punto)
print("Producto cruz:", producto_cruz)
print("División:", division)


# Matrices 2x2 inicializadas
A = [[4, 6],
     [3, 8]]

B = [[2, 1],
     [5, 7]]

# Suma
suma = [[A[0][0]+B[0][0], A[0][1]+B[0][1]],
        [A[1][0]+B[1][0], A[1][1]+B[1][1]]]

# Resta
resta = [[A[0][0]-B[0][0], A[0][1]-B[0][1]],
         [A[1][0]-B[1][0], A[1][1]-B[1][1]]]

# Producto matricial
producto = [[A[0][0]*B[0][0] + A[0][1]*B[1][0],
             A[0][0]*B[0][1] + A[0][1]*B[1][1]],

            [A[1][0]*B[0][0] + A[1][1]*B[1][0],
             A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

# División elemento a elemento
division = [[A[0][0]/B[0][0], A[0][1]/B[0][1]],
            [A[1][0]/B[1][0], A[1][1]/B[1][1]]]

print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print("División:", division)

import math

# Coordenadas rectangulares
x = 3
y = 4
z = 5

# Cilíndricas
r = math.sqrt(x**2 + y**2)
theta = math.atan2(y, x)
z_cil = z

# Esféricas
rho = math.sqrt(x**2 + y**2 + z**2)
theta_esf = math.atan2(y, x)
phi = math.acos(z/rho)

print("Cilíndricas:", (r, theta, z_cil))
print("Esféricas:", (rho, theta_esf, phi))


# Constantes
R0 = 100
A = 3.9083e-3
B = -5.775e-7

# Temperatura inicializada
T = 50

# Cálculo
R = R0 * (1 + A*T + B*T**2)

print("Temperatura:", T, "°C")
print("Resistencia:", R, "ohmios")


import math

def rotacion_x(angulo):
    return [
        [1, 0, 0],
        [0, math.cos(angulo), -math.sin(angulo)],
        [0, math.sin(angulo), math.cos(angulo)]
    ]

def rotacion_y(angulo):
    return [
        [math.cos(angulo), 0, math.sin(angulo)],
        [0, 1, 0],
        [-math.sin(angulo), 0, math.cos(angulo)]
    ]

def rotacion_z(angulo):
    return [
        [math.cos(angulo), -math.sin(angulo), 0],
        [math.sin(angulo), math.cos(angulo), 0],
        [0, 0, 1]
    ]

angulo = math.radians(30)

print("Rotación X:", rotacion_x(angulo))
print("Rotación Y:", rotacion_y(angulo))
print("Rotación Z:", rotacion_z(angulo))




import math

# Valores inicializados
presion = 600000  # Pascales
diametro_piston = 0.1  # metros
diametro_vastago = 0.02  # metros

# Áreas
area_piston = math.pi * (diametro_piston/2)**2
area_vastago = math.pi * (diametro_vastago/2)**2

# Fuerzas
fuerza_avance = presion * area_piston
fuerza_retroceso = presion * (area_piston - area_vastago)

print("Fuerza de avance:", fuerza_avance, "N")
print("Fuerza de retroceso:", fuerza_retroceso, "N")

##holiss