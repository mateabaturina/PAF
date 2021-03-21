import matplotlib.pyplot as plt
import math

class Particle:
    def __init__(self, v0, kut, x, y):
        self.v0 = v0
        self.Kut = kut
        self.kut = math.radians(self.Kut)
        self.x = x
        self.y = y

    def reset(self):
        dic = vars(self)
        for i in dic.keys():
            dic[i] = 0
        plt.clf()
        
    def __move(self):
        a = 9.81
        dt = 0.01
        self.kx = math.cos(self.kut)
        self.ky = math.sin(self.kut)
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        self.x_smjer = [] 
        self.y_smjer = []

        for i in range(1000):
            self.x = self.x + self.vx * dt
            self.vy = self.vy - a * dt
            self.y = self.y + self.vy * dt
            if self.y <= 0:
                    break  

            self.x_smjer.append(self.x)
            self.y_smjer.append(self.y)

    def Range(self): 
            x = self.x
            v0 = self.v0
            kut = self.Kut
            self.__move()
            
            print("Za v={} i kut {} domet je {:.2f} m.".format(v0, kut, (self.x - x)))
            
    def plot_trajectory(self):
        plt.plot(self.x_smjer, self.y_smjer, 'r')
        plt.pause(3)
        plt.close