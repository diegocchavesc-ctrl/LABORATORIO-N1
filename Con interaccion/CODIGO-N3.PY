import math
while True:
    print("\nCALCULADORA DE VOLÚMENES")
    print("1. Prisma")
    print("2. Pirámide")
    print("3. Cono truncado")
    print("4. Cilindro")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")


# PRISMA

if opcion == "1":
    area_base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))
    volumen = area_base * altura
    print(f"Volumen del prisma: {volumen:.2f}")



# PIRÁMIDE

elif opcion == "2":

    area_base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))
    volumen = (area_base * altura) / 3
    print(f"Volumen de la pirámide: {volumen:.2f}")



# CONO TRUNCADO

elif opcion == "3":

    R = float(input("Ingrese el radio mayor: "))
    r = float(input("Ingrese el radio menor: "))
    altura = float(input("Ingrese la altura: "))
    volumen = (1/3) * math.pi * altura * (R**2 + r**2 + R*r)
    print(f"Volumen del cono truncado: {volumen:.2f}")



# CILINDRO

elif opcion == "4":
    radio = float(input("Ingrese el radio: "))
    altura = float(input("Ingrese la altura: "))
    volumen = math.pi * (radio**2) * altura
    print(f"Volumen del cilindro: {volumen:.2f}")



# SALIR
elif opcion == "5":
    print("Programa finalizado")
    break
else:
    print("Opción inválida")