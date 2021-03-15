import matplotlib.pyplot as plt
import math

def putanja_gibanja(kut, v0, t):
    kx = math.cos(kut)
    ky = math.sin(kut)
    x_smjer = []
    y_smjer = []

    for t in range(0, 11):
        x = (v0 * kx) * t
        y = v0 * ky - (0.5 * 9.8) * (t**2)
        x_smjer.append(x)
        y_smjer.append(y)
    p = [i for i, j in enumerate(y_smjer) if j < 0]                        
    for i in sorted(p, reverse = True):
        del x_smjer[i]
        del y_smjer[i]
    plt.plot(x_smjer, y_smjer, 'r')
    plt.pause(3) 
    plt.close  
     
def maksimalna_visina(v0, kut):
    ky = math.sin(kut)
    h = (v0**2 * ky**2) / (2 * 9.8)
    print('Maksimalna visina je {}m.'.format(h))

def domet(kut, v0):
    k = math.sin(2*kut)
    d = (v0**2 * k) / 9.8
    print('Domet iznosi: {}m.'.format(d))

def maksimalna_brzina(v0):
    v_max = v0
    print('Maksimalna brzina iznosi {}m/s.'.format(v_max))

def meta(kut, v0, t):
    p = int(input('Unesite p: '))
    q = int(input('Unesite q: '))
    r = int(input('Unesite radijus: '))
    kx = math.cos(kut)
    ky = math.sin(kut)
    x_smjer = []
    y_smjer = []
    lst = []
    
    for t in range(0, 11):
        x = (v0 * kx) * t
        y = v0 * ky - (0.5 * 9.8) * (t**2)
        x_smjer.append(x)
        y_smjer.append(y)
        for i in range(t):
            R = r**2
            d =  ((x_smjer[i]-p)**2 + (y_smjer[i]-q)**2) - R
            lst.append(d) 
    
    def lst1(lst, minimum):
        if min(lst) <= minimum:
            print("Meta je pogodena.")    
        else:
            print("Meta nije pogodena. Najmanja udaljenost iznosi {}.".format(min(lst)))          
    
    lst1(lst, 0)    
    circle=plt.Circle((p, q),r, fill = False )
    plt.figure(figsize=(12,12))
    plt.gca().add_patch(circle)
    plt.plot()
    plt.plot(x_smjer, y_smjer)
    plt.scatter(p, q, s=10)
    plt.show()
    

