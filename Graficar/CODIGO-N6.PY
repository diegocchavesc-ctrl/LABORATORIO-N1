import cv2
import matplotlib.pyplot as plt
import numpy as np

archivos = [
    (r"C:\Users\User\Downloads\chevrolet.png", 0.01, "Chevrolet"),
    (r"C:\Users\User\Downloads\mitsubishi.png", 0.02, "Mitsubishi")
]

def obtener_puntos(path, sens):
    img = cv2.imread(path)
    if img is None:
        print("No se pudo abrir:", path)
        return None, None    
    # Preprocesado rapido
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    suave = cv2.GaussianBlur(gris, (5, 5), 0)
    # Umbral para separar el logo del fondo
    _, binaria = cv2.threshold(suave, 200, 255, cv2.THRESH_BINARY_INV)
    # Buscar contornos y quedarnos con el mas grande
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contornos:
        return None, None    
    grande = max(contornos, key=cv2.contourArea)
    # Simplificar el contorno para sacar solo las esquinas 
    eps = sens * cv2.arcLength(grande, True)
    puntos = cv2.approxPolyDP(grande, eps, True)
    px = puntos[:, 0, 0]
    py = img.shape[0] - puntos[:, 0, 1]
    return px, py

# --- PROCESAR Y MOSTRAR ---
for ruta, precision, nombre in archivos:
    x, y = obtener_puntos(ruta, precision)
    if x is not None:
        plt.figure(figsize=(9, 6))
        
        # Cerrar el poligono para que la linea de plt no quede abierta
        plt.plot(np.append(x, x[0]), np.append(y, y[0]), 'g-', linewidth=1.5)
        plt.scatter(x, y, color='black', s=25)
        
        # Formatear el texto lateral de coordenadas
        lista_coords = "\n".join([f"P{i}: ({x[i]}, {y[i]})" for i in range(len(x))])
        plt.text(1.05, 0.5, f"Coordenadas:\n{lista_coords}", 
                 transform=plt.gca().transAxes, fontsize=8,
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3),
                 verticalalignment='center')
        plt.title(f"Analisis de Vértices - {nombre}")
        plt.axis("equal")
        plt.grid(True, alpha=0.3)
        plt.legend(loc='upper right')
        plt.tight_layout()
        plt.show()