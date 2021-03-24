import particle as prt 

p1 = prt.Particle(0, 0, 0, 0, 0)
p1.__init__(10, 60, 0, 0, 0.01)
p1.Relative_error()
p1.plot_trajectory1()
p1.reset() 