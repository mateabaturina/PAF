import matplotlib.pyplot as plt
import numpy as np 

class Particle:
    def __init__(self, q, m, x, y, z, Ex, Ey, Ez, vx, vy, vz, Bx, By, Bz, dt):
        self.q = q
        self.m = m
        self.x = x
        self.y = y
        self.z = z
        self.Bx = Bx
        self.By = By
        self.r = np.array([x, y, z])
        self.E = np.array([Ex, Ey, Ez])
        self.v = np.array([vx, vy, vz])
        self.B = np.array([Bx, By, Bz])
        b = np.cross(self.v,self.B)
        self.dt = dt

    def acc(self, v):
        return self.q/self.m *(np.add(self.E,np.cross(v,self.B)))

    def Eulerova_metoda(self):
        self.xlista = []
        self.ylista = []
        self.zlista = []
        t = 0
        for i in range(2000):
            self.a = self.acc(self.v)
            self.v = np.add(self.v, np.dot(self.a, self.dt))
            self.r = np.add(self.r, np.dot(self.v, self.dt))
            self.xlista.append(self.r[0])
            self.ylista.append(self.r[1])
            self.zlista.append(self.r[2])

        return(self.xlista, self.ylista, self.zlista)

    def acc2(self, v, B):
        self.B = np.array([self.Bx, self.By, B])
        return self.q/self.m *(np.add(self.E,np.cross(v,self.B)))

    def Eulerova_metoda2(self):
        self.xlista3 = []
        self.ylista3= []
        self.zlista3 = []
        n = 0
        for t in range(2000):
            u = 1/2000
            n += u
            self.a = self.acc2(self.v, n)
            self.v = np.add(self.v, np.dot(self.a, self.dt))
            self.r = np.add(self.r, np.dot(self.v, self.dt))
            self.xlista3.append(self.r[0])
            self.ylista3.append(self.r[1])
            self.zlista3.append(self.r[2])

        return(self.xlista3, self.ylista3, self.zlista3)

