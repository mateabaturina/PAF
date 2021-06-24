import Bullet as bl
import matplotlib.pyplot as plt

m1 = bl.Bullet(1, 2, 0)
m1.meta(50, 1.5, 2, 0.1, 0.01, 0) # l, h, h0, y, dt, kut

m2 = bl.Bullet(1, 2, 0)
m2.meta(50, 1.5, 2, 0.1, 0.05, 0) 

m3 = bl.Bullet(1, 2, 0)
m3.meta(50, 1.5, 2, 0.1, 0.1, 0) 