import random

cantidad = int(input("ingrese la cantidad de numeros que desea: "))
limite1 = int(input("\ningrese el limite inferior: "))
limite2 = int(input("\ningrese el limite superior: "))

for i in range (0, cantidad):
    numero = random.randint(limite1, limite2) # Número entero entre 1 y 10
    print(numero)