import calculus
import math
import matplotlib.pyplot as plt

def f1(x):
    return 5*x**3 - 2*x**2 + 2*x -3

def f2(x):
    return 2*x**2 - 3

lista1, lista2, lista3 = calculus.integracija(f2, 0, 11)
lista4, lista5 = calculus.trapez(f2, 0, 11)

s = [1]
plt.scatter(lista3, lista1, s, 'b')
plt.scatter(lista3, lista2, s, 'r')
plt.scatter(lista5, lista4, s, 'g')
plt.pause(10)
plt.show