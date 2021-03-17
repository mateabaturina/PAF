import matplotlib.pyplot as plt
import math
v0 = int(input("Unesite pocetnu brzinu u m/s: "))
kut = int(input("Unesite kut otklona u stupnjevima: "))
kut = math.radians(kut)
kx = math.cos(kut)
ky = math.sin(kut)
vx = v0 * kx
vy = v0 * ky

dt = 0.01
x = 0
y = 0
a = 9.81
t1 = 0

x_smjer = []
y_smjer = []
vrijeme = []

for i in range(1000):
    x = x + vx * dt
    x_smjer.append(x)
    vy = vy - a * dt
    y = y + vy * dt
    y_smjer.append(y)
    t1 = t1 + dt
    vrijeme.append(t1)
    
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.plot(x_smjer, y_smjer, 'r')
ax1.set_title('x-y graf')
ax2.plot(vrijeme, x_smjer, 'g')
ax2.set_title('x-t graf')
ax3.plot(vrijeme, y_smjer, 'b')
ax3.set_title('y-t graf')
plt.pause(25)    
