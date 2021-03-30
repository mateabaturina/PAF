import particle as prt
import matplotlib.pyplot as plt

p1 = prt.Particle(0, 0, 0, 0, 0)
p1.__init__(10, 60, 0, 0, 0.01)

def graf_domet_kut():
    kut_ = []
    domet_ = []
    p1 = prt.Particle(0, 0, 0, 0, 0)
    
    for kut in range(90):
        p1.__init__(10, kut, 0, 0, 0.01)
        d = p1.Range()
        domet_.append(d)
        kut_.append(kut)

    plt.plot(kut_, domet_, 'b')
    plt.xlabel("kut")
    plt.ylabel("domet")
    plt.title("Ovisnost dometa o pocetnom kutu otklona")
    plt.pause(3)
    plt.close

def graf_vrijeme_kut():
    kut_ = []
    vrijeme_ = []
    p1 = prt.Particle(0, 0, 0, 0, 0)
    
    for kut in range(90):
        p1.__init__(10, kut, 0, 0, 0.01)
        a = p1.total_time()
        vrijeme_.append(a)
        kut_.append(kut)

    plt.plot(kut_, vrijeme_, 'b')
    plt.xlabel("kut")
    plt.ylabel("vrijeme")
    plt.title("Ovisnost vremena trajanja gibanja o pocetnom kutu otklona")
    plt.pause(5)
    plt.close

graf_domet_kut()
plt.clf()
graf_vrijeme_kut()