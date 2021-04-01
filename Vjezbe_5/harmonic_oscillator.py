import matplotlib.pyplot as plt 

class HarmonicOscillator:
    def __init__(self, dt, k, m, v0, x0):
        self.dt = dt
        self.k = k 
        self.m = m 
        self.v0 = v0
        self.x0 = x0

    def oscillate(self):
        self.t = []
        self.x = []
        self.a = []
        self.v = []
        t = 0
        for i in range (100000):
            a = (-self.k/self.m)*self.x0
            self.v0 = self.v0 + a*self.dt
            self.x0 = self.x0 + self.v0*self.dt
            t += self.dt
            self.t.append(t)
            self.x.append(self.x0)
            self.a.append(a)
            self.v.append(self.v0)

    def plot_trajectory(self):
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
        ax1.plot(self.t, self.x, 'b')
        ax1.set_title('x-t graf')
        ax2.plot(self.t, self.v, 'b')
        ax2.set_title('v-t graf')
        ax3.plot(self.t, self.a, 'b')
        ax3.set_title('a-t graf')
        plt.pause(5)

