class Particle:
    def __init__(self, mass, x_0):
        self.mass = mass
        self.x_0 = x_0

    def printInfo(self):
        print("Cestica ima masu {0:.2f} i u pocetnom trenutku nalazi se na polozaju u x={1:.2f}".format(self.mass, self.x_0))

    def printUdaljenost(self):
        print("Udaljenost od ishodista je {}".format(0 - self.x_0))

    def korisnik(self, x):
        print("udaljenodt cestice je {}".format(self.x_0 - x))


p1 = Particle(10, -5)
p2 = Particle(20, -10)
p3 = Particle(10, 5)
p1.printInfo()
p2.printInfo()
p3.korisnik(7)
p1.printUdaljenost()
p2.printUdaljenost()
p3.printUdaljenost()


