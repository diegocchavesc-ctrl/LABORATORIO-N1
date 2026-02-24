import time
print("A continuacion escoge el robot de tu interes")
time.sleep(2)
print("1. Robot Cilindrico")
print("2. Robot Cartesiano")
print("3. Robot Esferico")
x=int(input("Escribe el numero:"))

if x==1:
    print("\n")
    print(" Escojiste el robot cilindrico:")
    print("\n Es un robot manipulador industrial")
    print("\n El cual cuenta 3 articulaciones")
    print("\n")
elif x==2:
    print("\n")
    print(" Escojiste el robot Cartesiano:")
    print("\n Es un robot con articulaciones prismaticas")
    print("\n El cual cuenta 3 articulaciones")
    print("\n")
elif x==3:
    print("\n")
    print(" Escojiste el robot Esferico:")
    print("\n Es un robot que utiliza una configuración cinemática RRP")
    print("\n El cual cuenta 3 articulaciones")
    print("\n")
else:
    print("\n")
    print(" Escojiste una opcion invalida")
    print("\n")