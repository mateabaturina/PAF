import matplotlib.pyplot as plt
import math
def crtez(p, q, r, x, y):
    c = int(input("Unesite 0 za crtez ili 1 za spremiti:"))
    if c == 0:
        circle=plt.Circle((p, q),r, fill = False )
        plt.figure(figsize=(12,12))
        plt.gca().add_patch(circle)
        plt.plot()
        plt.scatter(x, y, s=1000)
        plt.show()
    else:
        b = input("Unesite naziv: ")
        plt.savefig(b)
        
def kruznica():
    p=int(input("Unesite p: "))
    q=int(input("Unesite q: "))
    r=int(input("Unesite r: "))
    x=int(input("Unesite x: "))
    y=int(input("Unesite y: "))
    crtez(p, q, r, x, y)
    d =  (x-p)**2 + (y-q)**2
    R = r**2
    u = math.sqrt((x-p)**2 + (y-q)**2) - r
    if d == R:
        print("Tocka se nalazi na koordinatama ({},{}), te je na kruznici.".format(x, y))

    elif d < R:
        print("Tocka se nalazi unutar kruznice na koordinatama ({},{}), te je udaljena za {}.".format(x, y, -u))
        
    elif d > R:
        print("Tocka se nalazi van kruznice na koordinatama ({},{}), te je udaljena za {}.".format(x, y, u))
        
kruznica()
