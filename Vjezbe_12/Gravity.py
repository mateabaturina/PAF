import numpy as np
import math

class Planet:
    def __init__(self, name, Mz, xz, yz, vxz, vyz):
        self.ime = name
        self.Mz = Mz
        self.rz = np.array([xz, yz])
        self.vz = np.array([vxz, vyz])
    def name(self):
        a = self.ime
        return a

class Gravity:
    def __init__(self, Ms, G, xs, ys, vxs, vys, dt, t):
        self.Ms = Ms
        self.G = G
        self.rs = np.array([xs, ys])
        self.vs = np.array([vxs, vys])
        self.dt = dt
        self.t = t
        self.planets = []

    def add_planet(self, planet):
        self.planets.append(planet)
    
    def acs(self, rs, rz, m):
        a = np.power(np.subtract(rs,rz),2)
        b = math.sqrt(a[0] + a[1])
        return -self.G * m/(b**3) * np.subtract(rs,rz)

    def acz(self, rs, rz):
        a = np.power(np.subtract(rz,rs),2)
        b = math.sqrt(a[0] + a[1])
        return -self.G * self.Ms/(b**3) * np.subtract(rz,rs)

    def Eulerova_metoda(self):
        self.xslista = []
        self.yslista = []
        self.xzlista = []
        self.yzlista = []
        T = 0
        for p in self.planets:
            while T <= self.t:
                T += self.dt
                self.a = self.acs(self.rs, p.rz, p.Mz)
                self.vs = np.add(self.vs,self.a*self.dt)
                self.rs = np.add(self.rs,self.vs*self.dt)
                self.xslista.append(self.rs[0])
                self.yslista.append(self.rs[1])
                self.az = self.acz(self.rs, p.rz)
                p.vz = np.add(p.vz,self.az*self.dt)
                p.rz = np.add(p.rz,p.vz*self.dt)
                self.xzlista.append(p.rz[0])
                self.yzlista.append(p.rz[1])
            

        return (self.xslista, self.yslista, self.xzlista , self.yzlista)

