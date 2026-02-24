import math #Modulo para funciones matemáticas

# caracteristicas del cilindro
presion = 600000  # Pascales
diametro_piston = 0.1  # metros
diametro_vastago = 0.02  # metros

# Áreas
area_pis = math.pi * (diametro_piston/2)**2
area_vas = math.pi * (diametro_vastago/2)**2

# Fuerzas
fuerza_avance = presion * area_pis
fuerza_retroceso = presion * (area_pis - area_vas)
print("\npresion:", presion, "Pa")
print("\ndiametro del piston:", diametro_piston, "m")
print("\ndiametro del vastago:", diametro_vastago, "m")
print("\nFuerza de avance:", f"{fuerza_avance:.2f}", "N")
print("\nFuerza de retroceso:", f"{fuerza_retroceso:.2f}", "N")
