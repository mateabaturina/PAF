import calculus
import math
import matplotlib.pyplot as plt

def f1(x):
    return 5*x**3 - 2*x**2 + 2*x -3

def f2(x):
    return 2*x**2 - 3

def f1_der(x):
    return 15*(x**2) - 4*x + 2

calculus.derivacija(f1, -2, 2, 0.01, 2)

lista1, lista2 = calculus.derivacija(f1, -2, 2, 0.01, 2)
lista3, lista4 = calculus.derivacija(f1, -2, 2, 0.1, 2)

lista5 = []
for x in lista2:
    y = f1_der(x)
    lista5.append(y)

s = [5]
plt.scatter(lista2, lista1, s, 'g', label = "dt = 0.01")
plt.scatter(lista4, lista3, s, 'b', label = "dt = 0.1")
plt.plot(lista2, lista5, 'orange', label = "analiticki")
plt.legend(loc = 'best')
plt.pause(10)
plt.show
