class Vertikalni_hitac:
    def __init__(self, h0, v0):
        self.h0 = h0
        self.v0 = v0

    def stvaranje_objekta(self):
        print("Objekt je uspjesno stvoren. Pocetna visina mu je {}, a pocetna brzina {}.".format(self.h0, self.v0))

    def reset(self):
        dic = vars(self)
        for i in dic.keys():
            dic[i] = 0

o = Vertikalni_hitac(2, 5)
o.stvaranje_objekta()

o.reset()

o = Vertikalni_hitac(3, 6)
o.stvaranje_objekta()