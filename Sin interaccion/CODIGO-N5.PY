import numpy as np

# Función de rotación en X
def rotacion_x(angulo):
    
    theta = np.radians(angulo)      
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ]) 
    return Rx
# Función de rotación en Y
def rotacion_y(angulo):
    theta = np.radians(angulo)  
    Ry = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return Ry
# Función de rotación en Z
def rotacion_z(angulo):
    theta = np.radians(angulo)
    Rz = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])
    return Rz
# ingrese el anguloo
angulo = 30

print("Rotación en X:\n", rotacion_x(angulo))
print("\nRotación en Y:\n", rotacion_y(angulo))
print("\nRotación en Z:\n", rotacion_z(angulo))