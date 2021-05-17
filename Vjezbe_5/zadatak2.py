import harmonic_oscillator as ho
import numpy as np 

h1 = ho.HarmonicOscillator(0, 0, 0, 0, 0)
h1.__init__(0.1, 10, 5, 0, 0.3)
h1.period_titranja(5)
h1.reset()

h1 = ho.HarmonicOscillator(0, 0, 0, 0, 0)
h1.__init__(0.01, 10, 5, 0, 0.3)
h1.period_titranja(5)
h1.reset()

h1 = ho.HarmonicOscillator(0, 0, 0, 0, 0)
h1.__init__( 0.001,10, 5, 0, 0.3)
h1.period_titranja(5)

h1.analiticki_period()
