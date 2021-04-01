import matplotlib.pyplot as plt 
import harmonic_oscillator as ho 

h1 = ho.HarmonicOscillator(0, 0, 0, 0, 0)
h1.__init__(0.001, 1, 5, 10, 0)
h1.oscillate()
h1.plot_trajectory()

