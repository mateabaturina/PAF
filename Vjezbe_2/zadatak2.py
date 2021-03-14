import matplotlib.pyplot as plt
import math
v0 = int(input("Unesite pocetnu brzinu u m/s: "))
kut = int(input("Unesite kut otklona u stupnjevima: "))
kx = math.cos(kut)
ky = math.sin(kut)
x_smjer = []
y_smjer = []

for t in range(1, 11):
    x = (v0 * kx) * t
    x_smjer.append(x)
    y = v0 * ky - (0.5 * 9.8)*(t**2)
    y_smjer.append(y)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.plot(x_smjer, y_smjer, 'r')
ax1.set_title('x-y graf')
ax2.plot(x_smjer, 'g')
ax2.set_title('x-t graf')
ax3.plot(y_smjer, 'b')
ax3.set_title('y-t graf')
plt.pause(25)