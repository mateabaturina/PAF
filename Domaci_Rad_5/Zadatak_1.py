import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import Particle as prt

p1 = prt.Particle(1, 1, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.1, 0, 0, 1, 0.01)
p2 = prt.Particle(1, 1, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.1, 0, 0, 1, 0.01)

lista1, lista2, lista3 = p1.Eulerova_metoda()
lista4, lista5, lista6 = p2.Eulerova_metoda2()

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')
ax.plot(lista1, lista2, lista3, label = "Konstantno magnetsko polje")
ax.plot(lista4, lista5, lista6, 'r',label = "Vremenski promjenjivo polje" )
ax.view_init(30,120)
plt.legend(loc='best')
plt.pause(2)
plt.show

p1 = prt.Particle(1, 1, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.1, 0, 0, 1, 0.01)
p2 = prt.Particle(-1, 1, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.1, 0, 0, 1, 0.01)

lista1, lista2, lista3 = p1.Eulerova_metoda2()
lista4, lista5, lista6 = p2.Eulerova_metoda2()

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')
ax.plot(lista1, lista2, lista3, label = "Pozitron u vremeski promjenjivom polju")
ax.plot(lista4, lista5, lista6, 'r',label = "Elektron u vremeski promjenjivom polju" )
ax.view_init(30,30)
plt.legend(loc='best')
plt.pause(5)
plt.show