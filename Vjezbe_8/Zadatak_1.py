import Projectile as pr

p1 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p1.__init__(60, 15, 0.01, 0, 0, 1, 1.29, 1, 1)
p1.Eulerova_metoda()
p1.plot_trajectory()

