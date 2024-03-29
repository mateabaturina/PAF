import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
import matplotlib.animation as animation

class Planet:
    def __init__(self, name, Mz, xz, yz, vxz, vyz, color):
        self.ime = name
        self.Mz = Mz
        self.rz = np.array([xz, yz])
        self.vz = np.array([vxz, vyz])
        self.color = color

class Gravity:
    def __init__(self, G, dt, t):
        self.G = G
        self.dt = dt
        self.t = t

    def reset(self):
        self.xzlista = []
        self.yzlista = []

    def acz(self, rz, bodies, body_index):
        tbody = bodies[body_index]
        acz = 0
        for index, ebody in enumerate(bodies):
            if index != body_index:
                a = np.power(np.subtract(rz,ebody.rz),2)
                b = math.sqrt(a[0] + a[1])
                acz += -self.G * ebody.Mz/(b**3) * np.subtract(rz,ebody.rz)
        return acz
    
    def Eulerova_metoda(self, bodies):
        self.xzlista = []
        self.yzlista = []
        for body_index, tbody in enumerate(bodies):
            T = 0   
            while T <= self.t:
                T += self.dt
                self.az = self.acz(tbody.rz, bodies, body_index)
                tbody.vz = np.add(tbody.vz,self.az*self.dt)
                tbody.rz = np.add(tbody.rz,tbody.vz*self.dt)
                self.xzlista.append(tbody.rz[0])
                self.yzlista.append(tbody.rz[1])
            plt.style.use("dark_background")
            plt.plot(self.xzlista, self.yzlista, label = tbody.ime, color = tbody.color)
            plt.plot(self.xzlista[-1], self.yzlista[-1], 'o', color = tbody.color)
            self.reset()
        plt.title("Solar system")
        plt.legend(loc='best')
        plt.show()

    def Animation(self, bodies):
        self.xzlista = []
        self.yzlista = []
        handles = []
        plt.style.use("dark_background")
        fig, ax = plt.subplots()
        ax = plt.axes(xlim=(-350000000000, 300000000000), ylim=(-300000000000, 300000000000))
        def animate(i):
            for body_index, tbody in enumerate(bodies):
                self.reset()
                T = 0  
                while T <= self.t:
                    dt = self.dt
                    T += self.dt
                    self.az = self.acz(tbody.rz, bodies, body_index)
                    tbody.vz = np.add(tbody.vz,self.az*i)
                    tbody.rz = np.add(tbody.rz,tbody.vz*i)
                    self.xzlista.append(tbody.rz[0])
                    self.yzlista.append(tbody.rz[1])
                line = ax.plot(self.xzlista, self.yzlista, label =tbody.ime, color=tbody.color, lw=2)
            self.reset()
            return line
        for tbody in (bodies):
            handles.append(Line2D([0], [0], color = tbody.color, label = tbody.ime))
        anim = FuncAnimation(fig, animate, interval = 10, frames=(200))
        ax.set_title("Solar system")
        ax.legend(handles = handles, loc = 'lower right')
        anim.save('solar_system.gif', writer='imagemagick')
        #plt.show()

     
