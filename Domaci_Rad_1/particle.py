import matplotlib.pyplot as plt
import math

class Particle:
    def __init__(self, v0, kut, x, y, dt):
        self.v0 = v0
        self.Kut = kut
        self.kut = math.radians(self.Kut)
        self.x = x
        self.y = y
        self.dt_ = []
        self.dt = dt
        self.dt_.append(self.dt)

    def reset(self):
        dic = vars(self)
        for i in dic.keys():
            dic[i] = 0
        plt.clf()
        
    def __move(self):
        a = 9.81
        self.kx = math.cos(self.kut)
        self.ky = math.sin(self.kut)
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        self.x_smjer = [] 
        self.y_smjer = []

        for i in range(1000):
            self.x = self.x + self.vx * self.dt
            self.vy = self.vy - a * self.dt
            self.y = self.y + self.vy * self.dt
            if self.y <= 0:
                    break  
            self.x_smjer.append(self.x)
            self.y_smjer.append(self.y)
    
    def Range(self): 
        x = self.x
        v0 = self.v0
        kut = self.Kut
        self.__move()
        self.d = self.x - x
        print("Za v={} i kut {} domet je {:.2f} m.".format(v0, kut, (self.d)))

    def Range_Analitic(self):
        a = 9.81
        self.k = math.sin(self.kut * 2)
        self.X = ((self.v0**2) * self.k) / a

    def Relative_error(self):
        a = 9.81
        self.kx = math.cos(self.kut)
        self.ky = math.sin(self.kut)
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        self.Dt = 0
        self.Range_Analitic()
        self.re = []
        self.T = []
        self.x_ = []
        for i in range(1000):
            self.Dt = self.Dt + self.dt
            self.x = self.x + self.vx * self.Dt
            self.vy = self.vy - a * self.Dt
            self.y = self.y + self.vy * self.Dt
            if self.y <= 0:
                    break  
            self.T.append(self.Dt)
            self.x_.append(self.x)
        a = self.x
        self.__move()
        self.x_ = [x - a for x in self.x_]
        self.x_ = [-x for x in self.x_]
        self.re = list(map(lambda x: x - self.X, self.x_))
        self.re = list(map(lambda x: x/self.X, self.re))
        self.re = [-x for x in self.re]
        self.re = list(map(lambda x: x*100, self.re)) 
    
    def plot_trajectory(self):
        plt.plot(self.x_smjer, self.y_smjer, 'r')
        plt.pause(3)
        plt.close

    def plot_trajectory1(self):
        plt.plot(self.T, self.re, 'b')
        plt.pause(3)
        plt.close

    def total_time(self):
        self.Relative_error()
        self.a = sum(self.T)
        print("Ukupno vrijeme gibanja je {} s.".format(self.a))

    def max_speed(self):
        v_list = []
        for i in range(1000):
            self.vx = self.v0 * self.kx
            self.vy = self.v0 * self.ky
            V = math.sqrt(self.vx**2 + self.vy**2) 
            v_list.append(V)
        print('Maksimalna brzina iznosi {}m/s.'.format(max(v_list)))

    def velocity_to_hit_target(self, kut, p, q, r):
        self.p = p
        self.q = q
        self.r = r
        self.x = 0
        self.y = 0
        self.Kut = math.radians(kut)
        self.kx = math.cos(self.Kut)
        self.ky = math.sin(self.Kut)
        a = 9.81
        self.dt = 0.01
        for self.v0 in range(1, 100):
            self.vx = self.v0 * self.kx
            self.vy = self.v0 * self.ky
            self.x = self.x + self.vx * self.dt
            self.vy = self.vy - a * self.dt
            self.y = self.y + self.vy * self.dt
            D =  math.sqrt((self.p-self.x)**2 + (self.q-self.y)**2) 
            if D <= self.r:
                break
        
        print("Potrebna pocetna brzina za pogoditi metu iznosi {} m/s.".format(self.v0))
    
    def angle_to_hit_target(self, v0, p, q, r):
        self.p = p
        self.q = q
        self.r = r
        self.v = v0
        a = 9.81
        self.x = 0
        self.y = 0
        self.dt = 0.01
        for self.k in range(90):
            self.kut = math.radians(self.k)
            self.vx = self.v * math.cos(self.kut)
            self.vy =self.v * math.cos(self.kut)
            self.x = self.x + self.vx * self.dt
            self.vy = self.vy - a * self.dt
            self.y = self.y + self.vy * self.dt
            D =  math.sqrt((self.p-self.x)**2 + (self.q-self.y)**2) 
            self.K = math.degrees(self.k)
            if D <= self.r:
                break
                
        print("Kut otklona za pogoditi metu iznosi {} stupnjeva.".format(self.k))


