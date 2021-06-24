import Bullet as bl
import matplotlib.pyplot as plt

m = bl.Bullet(1, 2, 100)

x, y, t = m.move(0, 0, 0.01) # x, kut, dt

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.plot(x, y, 'b')
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title('x-y graf')
ax2.plot(t, x, 'b')
ax2.set_xlabel("t")
ax2.set_ylabel("x")
ax2.set_title('x-t graf')
ax3.plot(t, y, 'b')
ax3.set_xlabel("t")
ax3.set_ylabel("y")
ax3.set_title('y-t graf')
plt.pause(10)