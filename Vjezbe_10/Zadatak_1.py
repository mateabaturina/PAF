import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import Particle as prt

p1 = prt.Particle(1, 1, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.1, 0, 0, 1, 0.01)
p2 = prt.Particle(-1, 1, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.1, 0, 0, 1, 0.01)

lista1, lista2, lista3 = p1.Eulerova_metoda()
lista4, lista5, lista6 = p2.Eulerova_metoda()

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')
ax.plot(lista1, lista2, lista3, label = "Positron")
ax.plot(lista4, lista5, lista6, label = "Electron")
plt.legend(loc='best')
plt.pause(20)
plt.show