import harmonic_oscillator as ho
import numpy as np 

h1 = ho.HarmonicOscillator(0, 0, 0, 0, 0)
h1.__init__(10, 0.1, 5, 0, 0.3)
h1.oscillate(25)
h1.period_titranja(25)
h1.reset()

h1 = ho.HarmonicOscillator(0, 0, 0, 0, 0)
h1.__init__(10, 0.01, 5, 0, 0.3)
h1.oscillate(25)
h1.period_titranja(25)
h1.reset()

h1 = ho.HarmonicOscillator(0, 0, 0, 0, 0)
h1.__init__(10, 0.001, 5, 0, 0.3)
h1.oscillate(25)
h1.period_titranja(25)

h1.analiticki_period()
#print(h1.x)
#print(h1.t) 