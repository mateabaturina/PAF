import matplotlib.pyplot as plt 
import modul as m


def f1(v, x, t):
    return 5 

def f2(v, x, t):
    k = 2
    return -k*x

h1 = m.Gibanje(0, 0, 0, 0, 0, f1)
h1.__init__(0.001, 1, 5, 10, 0, f1)
h1.move(25)
h1.plot_trajectory()

h2 = m.Gibanje(0, 0, 0, 0, 0, f2)
h2.__init__(0.001, 1, 5, 10, 0, f2)
h2.move(25)
h2.plot_trajectory()
