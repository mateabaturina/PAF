import particle as prt 

p1 = prt.Particle(0, 0, 0, 0, 0)
p1.__init__(10, 60, 0, 0, 0.01)
print("Ukupno vrijeme gibanja je {} s.".format(p1.total_time()))
p1.max_speed()
p1.reset()

p1.velocity_to_hit_target(27, 5, 5, 3)
p1.reset() 

p1.angle_to_hit_target(31, 10, 10, 3)
p1.reset() 