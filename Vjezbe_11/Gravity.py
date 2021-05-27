import numpy as np
import math

class Gravity:
    def __init__(self, Ms, Mz, G, xs, ys, xz, yz, vxs, vys, vxz, vyz, dt, t):
        self.Ms = Ms
        self.Mz = Mz
        self.G = G
        self.rs = np.array([xs, ys])
        self.rz = np.array([xz, yz])
        self.vs = np.array([vxs, vys])
        self.vz = np.array([vxz, vyz])
        self.dt = dt
        self.t = t
    
    def acs(self, rs, rz):
        a = np.power(np.subtract(rs,rz),2)
        b = math.sqrt(a[0] + a[1])
        return -self.G * self.Mz/(b**3) * np.subtract(rs,rz)

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
        while T <= self.t:
            T += self.dt
            self.a = self.acs(self.rs, self.rz)
            self.vs = np.add(self.vs,self.a*self.dt)
            self.rs = np.add(self.rs,self.vs*self.dt)
            self.xslista.append(self.rs[0])
            self.yslista.append(self.rs[1])
            self.az = self.acz(self.rs, self.rz)
            self.vz = np.add(self.vz,self.az*self.dt)
            self.rz = np.add(self.rz,self.vz*self.dt)
            self.xzlista.append(self.rz[0])
            self.yzlista.append(self.rz[1])

        return (self.xslista, self.yslista, self.xzlista , self.yzlista)
