import matplotlib.pyplot as plt
import numpy as np


def derivacija(func, x, h):
    return ((func(x+h)- func(x-h))/(2*h))

def der_analiticki(func, a, b, h):
    list1 = []
    list2 = []
    for x in np.arange(a, b, h):
        y = derivacija(func, x, h)
        list1.append(y)
        list2.append(x)
    return (list1, list2)

def integracija(func, x, h):
    return (func(x))