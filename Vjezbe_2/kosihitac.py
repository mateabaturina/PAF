import matplotlib.pyplot as plt
import math

def putanja_gibanja(kut, v0, t):
    kut = math.radians(kut)
    kx = math.cos(kut)
    ky = math.sin(kut)
    vx = v0 * kx
    vy = v0 * ky

    dt = 0.01
    x = 0
    y = 0
    a = 9.81

    x_smjer = []
    y_smjer = []

    for i in range(1000):
        x = x + vx * dt
        x_smjer.append(x)
        vy = vy - a * dt
        y = y + vy * dt
        y_smjer.append(y)
        if y <= 0:
            break
    
    plt.plot(x_smjer, y_smjer, 'r')
    plt.pause(3)
    plt.close 
     
def maksimalna_visina(v, kut):
    kut = math.radians(kut)
    ky = math.sin(kut)
    v = v**2
    ky = ky**2
    V = v * ky
    a = 2 * 9.8
    h = V / a
    print('Maksimalna visina je {}m.'.format(h))

def domet(kut, v0):
    kut = math.radians(kut)
    kx = math.cos(kut)
    ky = math.sin(kut)
    vx = v0 * kx
    vy = v0 * ky

    dt = 0.01
    x = 0
    y = 0
    a = 9.8

    for i in range(1000):
        x = x + vx * dt
        vy = vy - a * dt
        y = y + vy * dt
        if y <= 0:
            break
    
    print('Domet iznosi: {}m.'.format(x))

def maksimalna_brzina(v):
    v_max = v
    print('Maksimalna brzina iznosi {}m/s.'.format(v_max))

def meta(kut, v0, t):
    p = int(input('Unesite p: '))
    q = int(input('Unesite q: '))
    r = int(input('Unesite radijus: '))
    kut = math.radians(kut)
    kx = math.cos(kut)
    ky = math.sin(kut)
    vx = v0 * kx
    vy = v0 * ky

    dt = 0.01
    x = 0
    y = 0
    a = 9.81

    x_smjer = []
    y_smjer = []
    lst = []
    for i in range(1000):
        x = x + vx * dt
        x_smjer.append(x)
        vy = vy - a * dt
        y = y + vy * dt
        y_smjer.append(y)
        if y <=0:
            break
        for j in range(i):
            R = r**2
            D =  math.sqrt((p-x)**2 + (q-y)**2) 
            d = D - R
            lst.append(d) 
    
    def lst1(lst, minimum):
        if min(lst) <= minimum:
            print("Meta je pogodena.")    
        else:
            print("Meta nije pogodena. Najmanja udaljenost iznosi {}.".format(min(lst)))          
    
    lst1(lst, 0)    
    circle=plt.Circle((p, q),r, fill = False )
    plt.figure(figsize=(6,6))
    plt.gca().add_patch(circle)
    plt.plot()
    plt.plot(x_smjer, y_smjer)
    plt.scatter(p, q, s=2)
    plt.show()