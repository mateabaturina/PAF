import matplotlib.pyplot as plt
import math
import numpy as np 

class Projectile:
    def __init__(self, kut, v0, dt, x, y, m, ro, Cd, A, r):
        self.kt = kut
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
        self.r = r

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

    def Sphere(self):
        self.A = math.pi * self.r**2
        lista1, lista2 = self.Eulerova_metoda()
        return(lista1, lista2)

    def Cube(self):
        self.x = 0
        self.y = 0
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        a = math.sqrt(math.pi)*self.r #stranica a je namještena tako da dometi kugle i kocke budu jednaki
        self.A = a**2
        lista3, lista4 = self.Eulerova_metoda()
        return(lista3, lista4)

    def Cube2(self):
        self.x = 0
        self.y = 0
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        a = math.sqrt(math.pi)*self.r
        b = 90 - self.kt
        f = (b/180)*math.pi
        c = a / math.cos(f)
        self.A = a*c
        lista5, lista6 = self.Eulerova_metoda()
        return(lista5, lista6)

    def angle_to_hit_target(self, p, q, r, n):
        self.p = p
        self.q = q
        self.r = r
        self.kx = 0
        self.ky = 0
        self.vx = 0
        self.vy = 0
        self.x = 0
        self.y = 0
        g = 9.8
        self.x1_smjer = []
        self.y1_smjer = []
        for self.k in range(92):
            self.kt =(self.k/180)*math.pi
            self.kx = math.cos(self.kt)
            self.ky = math.sin(self.kt)
            self.vx = self.v0 * self.kx
            self.vy = self.v0 * self.ky
            ax = - np.sign(self.vx) * ((self.ro*self.Cd*self.A)/2*self.m) * (self.vx)**2
            self.vx = self.vx + ax * self.dt 
            self.x = self.x + self.vx * self.dt
            self.x1_smjer.append(self.x)
            ay = - g - np.sign(self.vy)*((self.ro*self.Cd*self.A)/2*self.m)*(self.vy)**2
            self.vy = self.vy + ay * self.dt 
            self.y = self.y + self.vy * self.dt
            self.y1_smjer.append(self.y)
            D =  math.sqrt((self.p-self.x)**2 + (self.q-self.y)**2) 
            if D <= self.r:
                print("Kut otklona cestice {} za pogoditi metu iznosi {} stupnjeva.".format(n, self.k))
                circle=plt.Circle((p, q),r, fill = False )
                plt.figure(figsize=(6,6))
                plt.gca().add_patch(circle)
                plt.plot()
                plt.plot(self.x1_smjer, self.y1_smjer)
                plt.scatter(p, q, s=2)
                plt.show() 
                break
            elif self.k == 91:
                print("Nemoguce je pogoditi metu cesticom {}!".format(n))
                break
        
        

    def plot_trajectory(self):
        plt.plot(self.x_smjer, self.y_smjer, 'r')
        plt.pause(5)
        plt.close 



   