import Projectile as pr
import matplotlib.pyplot as plt

p1 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p1.__init__(60, 15, 0.01, 0, 0, 1, 1.29, 1, 1)
p2 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p2.__init__(60, 15, 0.01, 0, 0, 1, 1.29, 3, 1)
p3 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p3.__init__(60, 15, 0.01, 0, 0, 1, 1.29, 6, 1)
lista1, lista2 = p1.Eulerova_metoda()
lista3, lista4 = p2.Eulerova_metoda()
lista5, lista6 = p3.Eulerova_metoda()

plt.plot(lista1, lista2, 'b', label = "Cd = 1")
plt.plot(lista3, lista4, 'r', label = "Cd = 2")
plt.plot(lista5, lista6, 'g', label = "Cd = 3")
plt.legend(loc='best')
plt.title("Ovisnost dometa o koeficijentu trenja")
plt.pause(2)
plt.show

p1.reset()
p2.reset()
p3.reset()

p1 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p1.__init__(60, 15, 0.01, 0, 0, 1, 1.29, 1, 1)
p2 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p2.__init__(60, 15, 0.01, 0, 0, 2, 1.29, 1, 1)
p3 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p3.__init__(60, 15, 0.01, 0, 0, 3, 1.29, 1, 1) 
lista1, lista2 = p1.Eulerova_metoda()
lista3, lista4 = p2.Eulerova_metoda()
lista5, lista6 = p3.Eulerova_metoda()

plt.plot(lista1, lista2, 'b', label = "m = 1")
plt.plot(lista3, lista4, 'r', label = "m = 2")
plt.plot(lista5, lista6, 'g', label = "m = 3")
plt.legend(loc='best')
plt.title("Ovisnost dometa o masi")
plt.pause(5)
plt.show


