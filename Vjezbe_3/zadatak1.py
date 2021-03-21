import particle as prt 

p1 = prt.Particle(0, 0, 0, 0)
p1.__init__(25, 60, 0, 0)
p1.Range()
p1.plot_trajectory()
p1.reset()

p1.__init__(10, 60, 0, 0)
p1.Range()
p1.plot_trajectory()
p1.reset()  
