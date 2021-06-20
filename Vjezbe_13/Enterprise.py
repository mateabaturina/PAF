import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
import matplotlib.animation as animation

class Planet:
    def __init__(self, name, Mz, xz, yz, vxz, vyz, color, r):
        self.ime = name
        self.Mz = Mz
        self.rz = np.array([xz, yz])
        self.vz = np.array([vxz, vyz])
        self.color = color
        self.r = r

class Gravity:
    def __init__(self, G, dt, t):
        self.G = G
        self.dt = dt
        self.t = t
        self.sun = []
        self.earth = []
        self.mercury = []
        self.venus = []
        self.mars = []
        self.c = []

    def reset(self):
        self.xzlista = []
        self.yzlista = []

    def acz(self, rz, bodies, body_index, tr):
        tbody = bodies[body_index]
        acz = 0
        n = 0
        c = []
        for index, ebody in enumerate(bodies):
            if index != body_index:
                r = ebody.r
                a = np.power(np.subtract(rz,ebody.rz),2)
                b = math.sqrt(a[0] + a[1])
                acz += -self.G * ebody.Mz/(b**3) * np.subtract(rz,ebody.rz)
                if ebody.ime == "Comet":
                    c.append(b)
                if b <= (tr + r):
                    n == 1
                else :
                    n == 0
        return acz, c, n
    
    def Eulerova_metoda(self, bodies):
        self.xzlista = []
        self.yzlista = []
        for body_index, tbody in enumerate(bodies):
            self.reset()
            T = 0   
            while T <= self.t:
                T += self.dt
                a, c, n = self.acz(tbody.rz, bodies, body_index, tbody.r)
                self.az = a
                tbody.vz = np.add(tbody.vz,self.az*self.dt)
                tbody.rz = np.add(tbody.rz,tbody.vz*self.dt)
                self.xzlista.append(tbody.rz[0])
                self.yzlista.append(tbody.rz[1])
                self.c.append(c)
            if n == 1:
                break
            if tbody.rz[0] <= -350000000000 or tbody.rz[0] >= 450000000000:
                break
            if tbody.rz[1] <= -300000000000 or tbody.rz[1] >=  450000000000:
                break
            if tbody.ime == "Sun":
                self.sun.append(min(self.c))
            if tbody.ime == "Earth":
                self.earth.append(min(self.c))
            if tbody.ime == "Mercury":
                self.mercury.append(min(self.c))
            if tbody.ime == "Venus":
                self.venus.append(min(self.c))
            if tbody.ime == "Mars":
                self.mars.append(min(self.c))
            self.c.clear()
        return (self.sun, self.earth, self.mercury, self.venus, self.mars) 

    def Animation(self, bodies):
        self.xzlista = []
        self.yzlista = []
        handles = []
        plt.style.use("dark_background")
        fig, ax = plt.subplots()
        #ax = plt.axes(xlim=(-350000000000, 300000000000), ylim=(-300000000000, 300000000000))
        def animate(i):
            for body_index, tbody in enumerate(bodies):
                self.reset()
                T = 0  
                while T <= self.t:
                    dt = self.dt
                    T += self.dt
                    self.az, c, n = self.acz(tbody.rz, bodies, body_index, tbody.r)
                    tbody.vz = np.add(tbody.vz,self.az*i)
                    tbody.rz = np.add(tbody.rz,tbody.vz*i)
                    self.xzlista.append(tbody.rz[0])
                    self.yzlista.append(tbody.rz[1])
                line = ax.plot(self.xzlista, self.yzlista, label =tbody.ime, color=tbody.color, lw=2)
            self.reset()
            return line
        for tbody in (bodies):
            handles.append(Line2D([0], [0], color = tbody.color, label = tbody.ime))
        anim = FuncAnimation(fig, animate, interval = 30, frames=(200))
        ax.set_title("Solar system")
        ax.legend(handles = handles, loc = 'lower right')
        #anim.save('solar_system.gif', writer='imagemagick')
        plt.show()

    def Armageddon(self, bodies):
        self.xzlista = []
        self.yzlista = []
        for body_index, tbody in enumerate(bodies):
            self.reset()
            T = 0   
            while T <= self.t:
                T += self.dt
                a, c, n = self.acz(tbody.rz, bodies, body_index, tbody.r)
                self.az = a
                tbody.vz = np.add(tbody.vz,self.az*self.dt)
                tbody.rz = np.add(tbody.rz,tbody.vz*self.dt)
                self.xzlista.append(tbody.rz[0])
                self.yzlista.append(tbody.rz[1])
            if n == 1:
                break
            if tbody.rz[0] <= -350000000000 or tbody.rz[0] >= 450000000000:
                break
            if tbody.rz[1] <= -300000000000 or tbody.rz[1] >=  450000000000:
                break
        return n 
     
