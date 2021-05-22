import matplotlib.pyplot as plt
import math
import numpy as np 

class Bungee_Jumping:
    def __init__(self, v0, y0, l, dt, m, k, ro, Cd, A):
        self.v0 = v0
        self.y0 = y0
        self.l = l
        self.dt = dt
        self.m = m
        self.k = k
        self.ro = ro
        self.Cd = Cd
        self.A = A

    def __a(self, n, d):
        g = 9.81 
        if n == 1:
            Fe = (self.k / self.m) * d 
            return Fe - g 
        else:
            return -g

    def Eulerova_metoda(self):
        g = 9.81
        t = 0
        d = 0
        y = self.y0
        self.y_smjer = []
        self.tlista = []
        self.Eellista = []
        self.Ulista = []
        self.Klista = []
        self.Elista = []
        for i in range(5000):
            d = y - self.l - self.y0
            if d > 0:
                n = 1
                Eel = (self.k * d**2) / 2
            else:
                n = 2
                Eel = 0
            self.v0 = self.v0 + self.__a(n, d) * self.dt 
            self.y0 = self.y0 + self.v0 * self.dt
            self.y_smjer.append(self.y0)
            t += self.dt
            self.tlista.append(t)
            U = self.m * self.y0 * g
            K = (self.m * self.v0**2) / 2
            E = Eel + U + K
            self.Eellista.append(Eel)
            self.Ulista.append(U)
            self.Klista.append(K)
            self.Elista.append(E)
            
        return(self.tlista, self.y_smjer, self.Eellista, self.Ulista, self.Klista, self.Elista)

    def __aoz(self, n, d):
        g = 9.81
        Foz = - abs(self.v0) * (self.ro*self.Cd*self.A) / (2*self.m) * self.v0
        if n == 1:
            Fe = (self.k / self.m) * d 
            return -g + Fe + Foz
        else:
            return -g + Foz

    def Eulerova_otpor_zraka(self):
        g = 9.81
        t = 0
        d = 0
        y = self.y0
        self.y_smjer2 = []
        self.tlista2 = []
        self.Eellista2 = []
        self.Ulista2 = []
        self.Klista2 = []
        self.Elista2 = []
        for i in range(5000):
            d = y - self.l - self.y0
            if d > 0:
                n = 1
                Eel = (self.k * d**2) / 2
            else:
                n = 2
                Eel = 0
            self.v0 = self.v0 + self.__aoz(n, d) * self.dt 
            self.y0 = self.y0 + self.v0 * self.dt
            self.y_smjer2.append(self.y0)
            t += self.dt
            self.tlista2.append(t)
            U = self.m * self.y0 * g
            K = (self.m * self.v0**2) / 2
            E = Eel + U + K
            self.Eellista2.append(Eel)
            self.Ulista2.append(U)
            self.Klista2.append(K)
            self.Elista2.append(E)
            
        return(self.tlista2, self.y_smjer2, self.Eellista2, self.Ulista2, self.Klista2, self.Elista2)

   