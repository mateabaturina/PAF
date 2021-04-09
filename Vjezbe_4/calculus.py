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

def analitic(func, a, b, h):
    list5 = []
    list6 = []
    for x in np.arange(a, b, h):
        y = (func(x+h) - func(x))/(h)
        list5.append(y)
        list6.append(x)
    return (list5, list6)

def integracija(func, a, b):
    g_meda = 0
    d_meda = 0
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    n = 100
    h = (b-a)/n
    y = a
    x = a + h
    for i in range(n):
        g_meda += func(x)*h
        d_meda += func(y)*h
        x += h
        y += h
        list1.append(g_meda)
        list2.append(d_meda)
        list3.append(i)
    return (list1, list2, list3)

def trapez(func, a, b):
    list1 = []
    list2 = []
    n = 100
    h = (b-a)/n
    y = a
    x = a + h
    trap = 0
    for i in range(n):
        trap = ((func(y) + func(x))/2)*h
        list1.append(trap)
        list2.append(i)
    return (list1, list2)
