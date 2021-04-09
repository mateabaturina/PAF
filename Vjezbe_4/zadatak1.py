import calculus
import math
import matplotlib.pyplot as plt

def f1(x):
    return 5*x**3 - 2*x**2 + 2*x -3

def f2(x):
    return 2*x**2 - 3

print(calculus.three_step(f1, 1., 0.1))
calculus.derivacija(f1, -2, 2, 0.01, 2)

lista1, lista2 = calculus.derivacija(f1, -2, 2, 0.01, 2)
lista3, lista4 = calculus.derivacija(f1, -2, 2, 0.1, 2)
lista5, lista6 = calculus.analitic(f1, -2, 2, 0.01)

s = [1]
plt.scatter(lista2, lista1, s, 'g')
plt.scatter(lista4, lista3, s, 'b')
plt.plot(lista6, lista5, 'r')
plt.pause(3)
plt.show
