import matplotlib.pyplot as plt
F = int(input("Unesite iznos sile u N: "))
m = int(input("Unesite masu cestice u kg: "))

akceleracija = []
brzina = []
put = []
for a in range(1, 11):
    a = F / m
    akceleracija.append(a)

for t in range(1, 11):
    v = a * t
    v1 = v + a * 0.01
    x = v * t
    x1 = x + v1 * 0.01
    brzina.append(int(v1))
    put.append(int(x1))


fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.plot(akceleracija, 'r')
ax1.set_title('a-t graf')
ax2.plot(brzina, 'g')
ax2.set_title('v-t graf')
ax3.plot(put, 'b')
ax3.set_title('x-t graf')
plt.pause(25)

