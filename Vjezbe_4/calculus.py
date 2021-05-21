import matplotlib.pyplot as plt
import numpy as np


def three_step(func, x, h):
    return ((func(x+h) - func(x-h))/(2*h))

def two_step(func, x, h):
    return ((func(x+h)-func(x))/h)

def derivacija(func, a, b, h, method):
    list1 = []
    list2 = []
    for x in np.arange(a, b, h):
        if method == 3:
            der = three_step(func, x, h)
        else:
            der = two_step(func, x, h)
        y = der
        list1.append(y)
        list2.append(x)
    return (list1, list2)

def integracija(func, a, b, n):
    g_meda = 0
    d_meda = 0
    h = (b-a)/n
    y = a
    x = a + h
    for i in range(n):
        g_meda += func(x)*h
        d_meda += func(y)*h
        x += h
        y += h
    return (g_meda, d_meda)

def trapez(func, a, b, n):
    h = (b-a)/n
    suma = 0
    x = a
    for i in range(n):
        suma += func(x)
        x += h
        trap = suma*h + ((func(b) + func(a))/2)*h
    return (trap)
