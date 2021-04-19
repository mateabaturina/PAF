import matplotlib.pyplot as plt

class Vertikalni_hitac:
    def __init__(self, h0, v0, dt):
        self.h0 = h0
        self.v0 = v0
        self.dt = dt
        #self.h1 = h0
        #self.v1 = v0

    def stvaranje_objekta(self):
        print("Objekt je uspjesno stvoren. Pocetna visina mu je {}, a pocetna brzina {}.".format(self.h0, self.v0))

    def reset(self):
        dic = vars(self)
        for i in dic.keys():
            dic[i] = 0

    def vertik_hitac(self):
        g = 9.81
        self.h = []
        self.T = []
        self.v = []
        t = 0
        for i in range(1000):
            self.v0 = self.v0 - g*self.dt
            self.h0 = self.h0 - self.v0*self.dt
            t += self.dt
            if self.v0 == 0:
                    break
            self.h.append(self.h0)
            self.T.append(t)
            self.v.append(self.v0)

        self.v1 = self.v[-1]
        self.h1 = self.h[-1]
        t = self.T[-1]
        for i in range(1000):
            self.v1 = self.v1 + g*self.dt
            self.h1 = self.h1 + self.v1*self.dt
            t += self.dt
            if self.h1 == 0:
                    break
            self.v.append(self.v1)
            self.h.append(self.h1)
            self.T.append(t)

    def plot_trajectory(self):
        self.vertik_hitac()
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.plot(self.T, self.h, 'b')
        ax1.set_title('h-t graf')
        ax2.plot(self.T, self.v, 'b')
        ax2.set_title('v-t graf')
        plt.pause(5)

    def maks_visina(self):
        self.vertik_hitac()
        a = max(self.h)
        print("Maksimalna visina iznosi {} m.".format(a))

    def vrijeme_trajanja(self):
        self.vertik_hitac()
        b = self.T[-1]
        print("Vrijeme trajanja iznosi {} s.".format(b))


o = Vertikalni_hitac(10, 10, 0.01)
o.maks_visina()

o.reset()

o = Vertikalni_hitac(10, 10, 0.05)
o.vrijeme_trajanja()
