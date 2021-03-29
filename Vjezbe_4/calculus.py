import matplotlib.pyplot as plt
import numpy as np


def derivacija(func, x, h):
    return ((func(x+h) - func(x-h))/(2*h))

def der_analiticki(func, a, b, h):
    list1 = []
    list2 = []
    for x in np.arange(a, b, h):
        y = derivacija(func, x, h)
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

def gornja_granica(func):
    g_meda = 0
    list1 = []
    list2 = []
    n = 100
    h = 1/n
    for x in range(n):
        g_meda += func(x)*h
        list1.append(g_meda)
        list2.append(x)
