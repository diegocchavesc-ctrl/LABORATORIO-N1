import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread(r"C:\Users\centrodesoluciones\Downloads\Robotica\Graficar\chevrolet.jpg")
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
canon1 = cv2.Canny(gray1, 100, 200)
contornos1, _ = cv2.findContours(canon1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt1 = max(contornos1, key=cv2.contourArea)

x1 = cnt1[:,0,0]
y1 = cnt1[:,0,1]

img2 = cv2.imread(r"C:\Users\centrodesoluciones\Downloads\Robotica\Graficar\mitsubishi.png")
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
canon2 = cv2.Canny(gray2, 100, 200)
contornos2, _ = cv2.findContours(canon2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt2 = max(contornos2, key=cv2.contourArea)

x2 = cnt2[:,0,0] - 500
y2 = cnt2[:,0,1]

plt.plot(x1, y1, 'k', linewidth=2) 
plt.plot(x2, y2, 'r', linewidth=2) 

for i in range(0, len(x1), 200):
    plt.text(x1[i], y1[i], f"({x1[i]},{y1[i]})", fontsize=6)

for i in range(0, len(x2), 200):
    plt.text(x2[i], y2[i], f"({x2[i]},{y2[i]})", fontsize=6)

plt.axis("equal")
plt.ylim(max(max(y1), max(y2)), 0) 
plt.grid()
plt.title("Logos extraidos")
plt.show()