
# Resistencia nominal a 0°C (PT100 = 100 ohmios)
R0 = 100
# Coeficiente de temperatura del platino
alpha = 0.00385
# 2. TEMPERATURA INICIALIZADA
T = 50


# 3. CÁLCULO DE LA RESISTENCIA
# Fórmula aproximada:
# R(T) = R0 * (1 + alpha * T)

R = R0 * (1 + alpha * T)


# 4. MOSTRAR RESULTADO


print("===== CÁLCULO RTD PT100 =====")
print("Temperatura:", T, "°C")
print("Resistencia calculada:", R, "Ω")

