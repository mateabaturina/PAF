import matplotlib.pyplot as plt

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
    d = r^2 - ((x-p)^2 + (y-q)^2)
    
    if d >= 0:
        return("Tocka se nalazi na koordinatama ({},{}), te je unutar kruznice za {}.".format(x, y, d))
        
    elif d==0:
        return("Tocka se nalazi na koordinatama ({},{}), te je na kruznici.".format(x, y))
        
    else:
        return("Tocka se nalazi na koordinatama ({},{}), te je van kruznice za {}.".format(x, y, d))
        
kruznica()
