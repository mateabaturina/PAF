import calculus as clc
import math
import matplotlib.pyplot as plt

def f1(x):
    return 5*x**3 - 2*x**2 + 2*x -3

def f1_int(x):
    return (5/4)*(x**4) - (2/3)*(x**3) + x**2 - 3*x

a = 0
b = 5
dn = 50
n_lista = []
lista_gm = []
lista_dm = []
analiticke = []
trapezne =  []

for i in range(1, 20):
    n_lista.append(i*dn)

for n in n_lista:
    gornja, donja = clc.integracija(f1, a, b, n)
    lista_gm.append(gornja)
    lista_dm.append(donja)
    integral_a = f1_int(b) - f1_int(a)
    trapez = clc.trapez(f1, a, b, n)
    analiticke.append(integral_a)
    trapezne.append(trapez)

s = [1]
plt.scatter(n_lista, lista_gm, s, 'b', label = "gornja meda")
plt.scatter(n_lista, lista_dm, s, 'r', label = "donja meda")
plt.scatter(n_lista, trapezne, s, 'g', label = "trapezna")
plt.plot(n_lista, analiticke, 'orange', label = "analiticki")
plt.legend(loc = 'best')
plt.pause(10)
plt.show