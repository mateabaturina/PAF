import Projectile as pr
import matplotlib.pyplot as plt

p1 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p1.__init__(60, 15, 0.01, 0, 0, 1, 1.29, 1, 0)
p1.Sphere(1)

plt.clf()

p2 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p2.__init__(60, 15, 0.01, 0, 0, 1, 1.29, 1, 0)
p2.Cube(1)
