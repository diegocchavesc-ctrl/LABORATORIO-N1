# 1. CONSTANTES
R0 = 100.0                 # Resistencia nominal a 0°C
A = 3.9083e-3              # Coeficiente A
B = -5.775e-7              # Coeficiente B
C = -4.183e-12             # Coeficiente C (solo para T < 0°C)

# 2. TEMPERATURA INICIALIZADA
T = -25  
# 3. CÁLCULO DE LA RESISTENCIA

if T >= 0:
    R = R0 * (1 + A*T + B*T**2)
else:
    R = R0 * (1 + A*T + B*T**2 + C*(T - 100)*T**3)
    
# 4. MOSTRAR RESULTADO

print("===== CÁLCULO RTD PT100 =====")
print("Temperatura:", T, "°C")
print("Resistencia calculada:", round(R, 4), "Ω")
