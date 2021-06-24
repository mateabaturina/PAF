import math
import numpy as np

from matplotlib.pyplot import xcorr

class Bullet:
    def __init__(self, n, h0, v0):
        self.h0 = h0
        self.v0 = v0
        self.__podaci__(n, h0, v0)

    def __podaci__(self, n, h0, v0):
        print("Metak {} ima pocetnu visinu {} i brzinu {}.".format(n, h0, v0))

    def change_h0(self,z,  n):
        if z == 0:
            self.h0 = self.h0 - n
        else:
            self.h0 = self.h0 + n
        
    def change_v0(self, z, n):
        if z == 0:
            self.v0 = self.v0 - n
        else:
            self.v0 = self.v0 + n

    def move(self, x, kut, dt):
        a = 9.81
        T = 0
        self.kut = kut
        self.dt = dt
        self.kx = math.cos(self.kut)
        self.ky = math.sin(self.kut)
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        self.x = x
        self.y = self.h0
        self.x_smjer = [] 
        self.y_smjer = [] 
        self.t = []
        for i in range(1000):
            self.x = self.x + self.vx * self.dt
            self.vy = self.vy - a * self.dt
            self.y = self.y + self.vy * self.dt
            T += self.dt
            if self.y <= 0:
                    break  
            self.x_smjer.append(self.x)
            self.y_smjer.append(self.y)
            self.t.append(T)
        return (self.x_smjer, self.y_smjer, self.t) 

    def meta(self, l, h, h0, y, dt, kut):
        self.p = l
        self.r = 0
        self.x = 0
        self.y = h0
        self.Kut = math.radians(kut)
        self.kx = math.cos(self.Kut)
        self.ky = math.sin(self.Kut)
        a = 9.81
        self.dt = dt
        for self.v0 in range(1, 100):
            self.vx = self.v0 * self.kx
            self.vy = self.v0 * self.ky
            self.x = self.x + self.vx * self.dt
            self.vy = self.vy - a * self.dt
            self.y = self.y + self.vy * self.dt
            AB = math.sqrt((l-l)*(l-l)+((h+y)-(h-y))*((h+y)-(h-y)))
            AP = math.sqrt((self.x-l)*(self.x-l)+(self.y-(h-y))*(self.y-(h-y)))
            PB = math.sqrt((l-self.x)*(l-self.x)+((h+y)-self.y)*((h+y)-self.y))
            if(AB == AP + PB):
                print("Potrebna pocetna brzina za pogoditi metu iznosi {} m/s.".format(self.v0))
            else:
                print("Nemoguće je pogoditi metu!")

    def meta_oz(self, l, h, h0, y, dt, kut, k, m):
        self.p = l
        self.r = 0
        self.x = 0
        self.y = h0
        self.Kut = math.radians(kut)
        self.kx = math.cos(self.Kut)
        self.ky = math.sin(self.Kut)
        a = 9.81
        self.dt = dt
        for self.v0 in range(1, 100):
            self.vx = self.v0 * self.kx
            self.vy = self.v0 * self.ky
            self.x = self.x + self.vx * self.dt
            self.vy = self.vy - (a +(k*self.v0/m)  )* self.dt
            self.y = self.y + self.vy * self.dt
            AB = math.sqrt((l-l)*(l-l)+((h+y)-(h-y))*((h+y)-(h-y)))
            AP = math.sqrt((self.x-l)*(self.x-l)+(self.y-(h-y))*(self.y-(h-y)))
            PB = math.sqrt((l-self.x)*(l-self.x)+((h+y)-self.y)*((h+y)-self.y))
            if(AB == AP + PB):
                print("Potrebna pocetna brzina za pogoditi metu iznosi {} m/s.".format(self.v0))
            else:
                print("Nemoguće je pogoditi metu!")
        
