import calculus
import math
import matplotlib.pyplot as plt

def f1(x):
    return 5*x**3 - 2*x**2 + 2*x -3

def f2(x):
    return 2*x**2 - 3

print(calculus.derivacija(f1, 1., 0.1))
calculus.der_analiticki(f1, -2, 2, 0.01)

lista1, lista2 = calculus.der_analiticki(f1, -2, 2, 0.01)
lista3, lista4 = calculus.der_analiticki(f1, -2, 2, 0.1)
lista5, lista6 = calculus.analitic(f1, -2, 2, 0.01)
s = [1]
plt.scatter(lista2, lista1, s, 'y')
plt.scatter(lista4, lista3, s, 'b')
plt.plot(lista6, lista5, 'r')
plt.pause(3)
plt.show
plt.clf()
lista7, lista8 = calculus.gornja_granica(f2)
s = [1]
plt.scatter(lista7, lista8, s, 'b')
plt.pause(10)
plt.show