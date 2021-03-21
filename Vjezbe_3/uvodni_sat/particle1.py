class Particle:
    def __init__(self, mass, x_0):
        self.mass = mass
        self.x_0 = x_0

    def printInfo(self):
        print("Cestica ima masu {0:.2f} i u pocetnom trenutku nalazi se na polozaju u x={1:.2f}".format(self.mass, self.x_0))

    def printUdaljenost(self):
        print("Udaljenost od ishodista je {}".format(0 - self.x_0))

 
