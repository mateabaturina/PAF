import Projectile as pr
import matplotlib.pyplot as plt

p1 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
p1.__init__(60, 15, 0.01, 0, 0, 1, 1.29, 1, 0, 1)
lista1, lista2 = p1.Sphere()
lista3, lista4 = p1.Cube() #površina okomita na gibanje jest stranica kocke, P = a**2
lista5, lista6 = p1.Cube2() #povšina okomita na gibanje ovisi o početnome kutu, P = c*a

plt.plot(lista1, lista2, 'b',linewidth=4, label = "Putanja kugle")
plt.plot(lista3, lista4, 'r', label = "Putanja kocke")
plt.plot(lista5, lista6, 'g', label = "Putanja kocke2")
plt.legend(loc='best')
plt.pause(15)
plt.show
