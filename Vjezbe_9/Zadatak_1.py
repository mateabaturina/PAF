import Bungee_Jumping as bj
import matplotlib.pyplot as plt

p1 = bj.Bungee_Jumping(0, 100, 10, 0.01, 60, 25, 1, 1, 1)
p2 = bj.Bungee_Jumping(0, 100, 10, 0.01, 60, 25, 1, 1, 1)

lista1, lista2, lista3, lista4, lista5, lista6 = p1.Eulerova_metoda()
lista7, lista8, lista9, lista10, lista11, lista12 = p2.Eulerova_otpor_zraka()

plt.subplot(2,2,1)
plt.plot(lista1, lista2)
plt.ylabel("x [m]")
plt.title("y-t graf")

plt.subplot(2,2,3)
plt.plot(lista7, lista8)
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("y-t graf")

plt.subplot(2,2,2)
plt.plot(lista1, lista3, 'r',label = "Elastična energija")
plt.plot(lista1, lista4, 'g', label = "Potencijalna energija")
plt.plot(lista1, lista5, 'b', label = "Kinetička energija")
plt.plot(lista1, lista6,  label = "Ukupna energija")
plt.ylabel("E [J]")
plt.legend(loc='upper right')
plt.title("Energy conservation")

plt.subplot(2,2,4)
plt.plot(lista7, lista9, 'r', label = "Elastična energija")
plt.plot(lista7, lista10, 'g', label = "Potencijalna energija")
plt.plot(lista7, lista11, 'b', label = "Kinetička energija")
plt.plot(lista7, lista12, label = "Ukupna energija")
plt.xlabel("t [s]")
plt.ylabel("E [J]")
plt.legend(loc='upper right')
plt.title("Energy conservation")

plt.pause(25)