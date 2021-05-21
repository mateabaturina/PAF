import calculus
import math
import matplotlib.pyplot as plt

def f1(x):
    return 5*x**3 - 2*x**2 + 2*x -3

def f1_der(x):
    return 15*(x**2) - 4*x + 2

def f2(x):
    return math.sin(x)

def f2_der(x):
    return math.cos(x)

lista1, lista2 = calculus.derivacija(f1, -2, 2, 0.01, 2)
lista3, lista4 = calculus.derivacija(f1, -2, 2, 0.1, 2)
list1, list2 = calculus.derivacija(f2, -2, 2, 0.01, 2)
list3, list4 = calculus.derivacija(f2, -2, 2, 0.1, 2)

lista5 = []
for x in lista2:
    y = f1_der(x)
    lista5.append(y)

list5 = []
for x in list2:
    y = f2_der(x)
    list5.append(y)

s = [2]
plt.scatter(lista2, lista1, s, 'g', label = "dt = 0.01")
plt.scatter(lista4, lista3, s, 'b', label = "dt = 0.1")
plt.plot(lista2, lista5, 'orange', label = "analiticki")
plt.legend(loc = 'best')
plt.title("f(x) = 5x^3 - 2x^2 + 2x - 3")
plt.pause(2)
plt.show

plt.clf()

plt.scatter(list2, list1, s, 'g', label = "dt = 0.01")
plt.scatter(list4, list3, s, 'b', label = "dt = 0.1")
plt.plot(list2, list5, 'orange', label = "analiticki")
plt.legend(loc = 'best')
plt.title("f(x) = sin(x)")
plt.pause(3)
plt.show
