import Gravity as gr
import matplotlib.pyplot as plt

dt = (60*60*24)/10
t = 60*60*24*365.242
p1 = gr.Gravity(1.989*10**30, 5.9742*10**24, 6.67408*10**(-11), 0, 0, 1.486*10**11, 0, 0, 0, 0, 29783, dt, t)
lista1, lista2, lista3, lista4 = p1.Eulerova_metoda()
plt.style.use("dark_background")
plt.plot(lista1, lista2, "gold", linewidth = 4, label = "Sun")
plt.plot(lista3, lista4, "b", label = "Earth")
plt.legend(loc='best')
plt.title("x-y graf")
plt.show()
