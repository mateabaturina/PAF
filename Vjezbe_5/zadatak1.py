import matplotlib.pyplot as plt 
import harmonic_oscillator as ho 

h1 = ho.HarmonicOscillator(0, 0, 0, 0, 0)
h1.__init__(0.001, 1, 5, 10, 0)
h1.oscillate(25)
h1.plot_trajectory()
#print(h1.t)
plt.clf()

h1.__init__(0.001, 1, 5, 10, 0)
h1.oscillate(25)
plt.scatter(h1.t,h1.x, s = 2, c = "b", label = "dt = 0.001")

h1.__init__(0.01, 1, 5, 10, 0)
h1.oscillate(25)
plt.scatter(h1.t,h1.x, s = 4, c = "g", label = "dt = 0.01")

h1.__init__(0.5, 1, 5, 10, 0)
h1.oscillate(25)
plt.scatter(h1.t,h1.x, s = 6, c = "orange", label = "dt = 0.05")

h1.__init__(0.01, 1, 5, 10, 0)
h1.analitic(25)
plt.plot(h1.t, h1.x, c = "r", label = "analitic")

plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("PRECIZNOST")
plt.legend(loc = "lower right")
plt.show()