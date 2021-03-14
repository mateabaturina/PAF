import matplotlib.pyplot as plt
import math

def jednoliko_gibanje(F, t, m):
    akceleracija = []
    brzina = []
    put = []
    for a in range(1, 11):
        a = F / m
        akceleracija.append(a)

    for t in range(1, 11):
        v = a * t
        v1 = v + a * 1
        x = v * t
        x1 = x + v1 * 1
        brzina.append(int(v1))
        put.append(int(x1))


    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.plot(akceleracija, 'r')
    ax1.set_title('a-t graf')
    ax2.plot(brzina, 'g')
    ax2.set_title('v-t graf')
    ax3.plot(put, 'b')
    ax3.set_title('x-t graf')
    plt.pause(5)
    plt.close



def kosi_hitac(kut, v0, t):
    kx = math.cos(kut)
    ky = math.sin(kut)
    x_smjer = []
    y_smjer = []

    for t in range(1, 11):
        x = (v0 * kx) * t
        x_smjer.append(x)
        y = v0 * ky - (0.5 * 9.8) * (t**2)
        y_smjer.append(y)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.plot(x_smjer, y_smjer, 'r')
    ax1.set_title('x-y graf')
    ax2.plot(x_smjer, 'g')
    ax2.set_title('x-t graf')
    ax3.plot(y_smjer, 'b')
    ax3.set_title('y-t graf')
    plt.pause(25)    