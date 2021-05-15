import matplotlib.pyplot as plt
import math
import numpy as np 

class Projectile:
    def __init__(self, kut, v0, dt, x, y, m, ro, Cd, A):
        self.kut =(kut/180)*math.pi
        self.kx = math.cos(self.kut)
        self.ky = math.sin(self.kut)
        self.v0 = v0
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        self.dt = dt
        self.x = x
        self.y = y
        self.m = m
        self.ro = ro
        self.Cd = Cd
        self.A = A  

    def reset(self):
        dic = vars(self) 
        for i in dic.keys():
            dic[i] = 0
        plt.clf()

    def Eulerova_metoda(self):
        g = 9.8
        t = 0
        self.x_smjer = []
        self.y_smjer = []
        for i in range(1000):
            ax = - np.sign(self.vx) * ((self.ro*self.Cd*self.A)/2*self.m) * (self.vx)**2
            self.vx = self.vx + ax * self.dt 
            self.x = self.x + self.vx * self.dt
            self.x_smjer.append(self.x)
            ay = - g - np.sign(self.vy)*((self.ro*self.Cd*self.A)/2*self.m)*(self.vy)**2
            self.vy = self.vy + ay * self.dt 
            self.y = self.y + self.vy * self.dt
            self.y_smjer.append(self.y)
            if self.y <= 0:
                break
        return(self.x_smjer, self.y_smjer)

    def _ax(self, o):
        return - np.sign(self.vx + o) * ((self.ro*self.Cd*self.A)/2*self.m) * (self.vx + o)**2
       
    def _ay(self, o):
        g = 9.81
        return - g - np.sign(self.vy + o)*((self.ro*self.Cd*self.A)/2*self.m)*(self.vy + o)**2

    def Runge_Kutta(self):
        self.x2_smjer = []
        self.y2_smjer = []
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        self.x = 0
        self.y = 0
        for i in range(1000):
            k1v = self._ax(0) * self.dt
            k1x = self.vx * self.dt 
            k2v = self._ax(k1v/2) * self.dt
            k2x = (self.vx + (k1v/2)) * self.dt 
            k3v = self._ax(k2v/2) * self.dt 
            k3x = (self.vx + (k2v/2)) * self.dt
            k4v = self._ax(k3v) * self.dt 
            k4x = (self.vx + k3v) * self.dt 
            self.vx = self.vx + (1/6) * (k1v + 2*k2v + 2*k3v + k4v)
            self.x = self.x + (1/6) * (k1x + 2*k2x + 2*k3x + k4x)
            self.x2_smjer.append(self.x)
            
            k1vy = self._ay(0) * self.dt
            k1y = self.vy * self.dt 
            k2vy = self._ay(k1vy/2) * self.dt 
            k2y = (self.vy + (k1vy/2)) * self.dt 
            k3vy = self._ay(k2vy/2) * self.dt 
            k3y = (self.vy + (k2vy/2)) * self.dt
            k4vy = self._ay(k3vy) * self.dt 
            k4y = (self.vy + k3vy) * self.dt 
            self.vy = self.vy + (1/6) * (k1vy + 2*k2vy + 2*k3vy + k4vy)
            self.y = self.y + (1/6) * (k1y + 2*k2y + 2*k3y + k4y)
            self.y2_smjer.append(self.y)
            if self.y <= 0:
                break
        return(self.x2_smjer, self.y2_smjer)

    def Range(self): 
        x = self.x
        self.Runge_Kutta()
        d = self.x - x
        return d
    
    def plot_trajectory(self):
        plt.plot(self.x_smjer, self.y_smjer, 'r')
        plt.pause(5)
        plt.close 



   