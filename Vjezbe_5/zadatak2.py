import harmonic_oscillator as ho
import numpy as np 

h1 = ho.HarmonicOscillator(0, 0, 0, 0, 0)
h1.__init__(0.1, 1, 5, 10, 0)
h1.oscillate(25)
h1.period_titranja(25)
print(h1.x)
#print(h1.t)