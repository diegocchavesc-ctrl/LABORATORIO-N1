
# Matrices inicializadas (2x2)
A = [
    [2, 4],
    [6, 8]
]

B = [
    [1, 3],
    [5, 7]
]

# SUMA DE MATRICES


suma = [
    [A[0][0] + B[0][0], A[0][1] + B[0][1]],
    [A[1][0] + B[1][0], A[1][1] + B[1][1]]
]


# RESTA DE MATRICES


resta = [
    [A[0][0] - B[0][0], A[0][1] - B[0][1]],
    [A[1][0] - B[1][0], A[1][1] - B[1][1]]
]


# MULTIPLICACIÓN ELEMENTO A ELEMENTO


multiplicacion = [
    [A[0][0] * B[0][0], A[0][1] * B[0][1]],
    [A[1][0] * B[1][0], A[1][1] * B[1][1]]
]


# DIVISIÓN ELEMENTO A ELEMENTO


division = [
    [A[0][0] / B[0][0], A[0][1] / B[0][1]],
    [A[1][0] / B[1][0], A[1][1] / B[1][1]]
]

# PRODUCTO PUNTO 


producto_punto = [
    [
        (A[0][0] * B[0][0]) + (A[0][1] * B[1][0]),
        (A[0][0] * B[0][1]) + (A[0][1] * B[1][1])
    ],
    [
        (A[1][0] * B[0][0]) + (A[1][1] * B[1][0]),
        (A[1][0] * B[0][1]) + (A[1][1] * B[1][1])
    ]
]


# PRODUCTO CRUZ (Solo aplica para vectores 3D)

V1 = [5, 4, 9]
V2 = [8, 2, 20]

producto_cruz = [
    V1[1]*V2[2] - V1[2]*V2[1],
    V1[2]*V2[0] - V1[0]*V2[2],
    V1[0]*V2[1] - V1[1]*V2[0]
]



print("\n===== RESULTADOS =====")

print("\nMatriz A:", A)
print("Matriz B:", B)

print("\n✅ Suma:", suma)
print("\n✅ Resta:", resta)
print("\n✅ Multiplicación elemento a elemento:", multiplicacion)
print("\n✅ División elemento a elemento:", division)

print("\n✅ Producto punto (A · B):", producto_punto)

print("\n✅ Producto cruz (Vectores):", producto_cruz)
#h
