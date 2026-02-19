#programa para realizar operaciones con vectores    

# Vectores inicializados
A = [5, 4, 9]
B = [8, 2, 20]

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
division = [A[0]/B[0], A[1]/B[1], A[2]/B[2],]

print("\n-resultados:")
print("\n-Suma:", suma)
print("\n-Resta:", resta)
print("\n-División:", division)
print("\n-Producto punto:", producto_punto)
print("\n-Producto cruz:", producto_cruz)

