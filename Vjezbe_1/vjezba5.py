import matplotlib.pyplot as plt

def jednadzba_pravca(x1, y1, x2, y2):
    a = (x2 - x1)/(y2 - y1)
    return a
x1 = int(input("Unesite x1 koordinatu: "))
y1 = int(input("Unesite y1 koordinatu: "))
x2 = int(input("Unesite x2 koordinatu: "))
y2 = int(input("Unesite y2 koordinatu: "))

xpoints = ([x1, x2])
ypoints = ([y1, y2])   
a = jednadzba_pravca(x1, y1, x2, y2)
print("y - {} = {} * x - {}".format(y1, a, x1))
 
while True:
    c = int(input("Odaberite 0 ako zelite nacrtati graf ili 1 ako zelite spremiti graf: "))
    if c == 0:
        plt.plot(xpoints, ypoints)
        plt.scatter(x1, y1, s=100)
        plt.scatter(x2, y2, s=100)
        plt.show()
        break
    else:
        b = input("Unesite naziv: ")
        plt.savefig(b)
        break
