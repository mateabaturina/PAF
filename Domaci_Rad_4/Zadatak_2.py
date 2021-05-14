import Projectile as pr

p1 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
p1.__init__(0, 15, 0.01, 0, 0, 1, 1.29, 1, 1, 1)
p1.angle_to_hit_target(1, 1, 1)


p1.reset()

p2 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p2.__init__(0, 15, 0.01, 0, 0, 1, 1.29, 1, 1)
p2.angle_to_hit_target(4, 4, 1)



