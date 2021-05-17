import matplotlib.pyplot as plt 
import numpy as np
import math

class HarmonicOscillator:
    def __init__(self, dt, k, m, v0, x0):
        self.dt = dt
        self.k = k 
        self.m = m 
        self.v0 = v0
        self.x0 = x0

    def reset(self):
        dic = vars(self) 
        for i in dic.keys():
            dic[i] = 0
        plt.clf()

    def oscillate(self, totalt):
        self.t = []
        self.x = []
        self.a = []
        self.v = []
        t = 0
        
        while t < totalt:
            a = (-self.k*self.x0)/self.m
            self.v0 = self.v0 + a*self.dt
            self.x0 = self.x0 + self.v0*self.dt
            t += self.dt
            self.t.append(t)
            self.x.append(self.x0)
            self.a.append(a)
            self.v.append(self.v0)
        return(self.t, self.x)

    def plot_trajectory(self):
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
        ax1.plot(self.t, self.x, 'b')
        ax1.set_title('x-t graf')
        ax2.plot(self.t, self.v, 'b')
        ax2.set_title('v-t graf')
        ax3.plot(self
        .t, self.a, 'b')
        ax3.set_title('a-t graf')
        plt.pause(10)

    def analitic(self, totalt):
        self.x = []
        self.t = []
        t = 0
        #while t <= totalt:
        for i in range(1000):
            self.x0 = self.x0 * math.sin((math.sqrt(self.k/self.m))*t + math.pi/2)
            t += self.dt
            self.x.append(self.x0)
            self.t.append(t)

    def period_titranja(self, t):
        self.t, self.x = self.oscillate(t)
        g = max(self.x)
        a = self.x.index(g)
        s = min(self.x)
        b = self.x.index(s)
        c = self.t[a]
        d = self.t[b] 
        t = abs(c - d)*2
        print("Numericki period titranja iznosi {}.".format((t)))
        

    def analiticki_period(self):
        T = 2*math.pi*math.sqrt(self.m/self.k)
        print("Analiticki period titranja iznosi {}.".format(T))

         
       

