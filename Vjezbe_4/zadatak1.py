import calculus
import math
import matplotlib.pyplot as plt

def f1(x):
    return 5*x**3 - 2*x**2 + 2*x -3

def f2(x):
    return 15*x**2 - 4*x +2

print(calculus.derivacija(f1, 1., 0.1))
calculus.der_analiticki(f1, -2, 2, 0.01)

lista1, lista2 = calculus.der_analiticki(f1, -2, 2, 0.01)
lista3, lista4 = calculus.der_analiticki(f1, -2, 2, 0.1)
lista5, lista6 = calculus.der_analiticki(f2, -2, 2, 0.01)
s = [1]
plt.scatter(lista2, lista1, s, 'r')
plt.scatter(lista4, lista3, s, 'b')
plt.scatter(lista6, lista5, s, 'g')
plt.pause(5)
plt.show