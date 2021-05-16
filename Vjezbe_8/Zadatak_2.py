import Projectile as pr
import matplotlib.pyplot as plt


p1 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p1.__init__(60, 15, 0.01, 0, 0, 1, 1.29, 1, 1)
lista1, lista2 = p1.Eulerova_metoda()
lista3, lista4 = p1.Runge_Kutta()

plt.plot(lista1, lista2, 'b', label = "Eulerova metoda")
plt.plot(lista3, lista4, 'r', label = "Runge-Kutta metoda")
plt.legend(loc='best')
plt.pause(15)
plt.show

