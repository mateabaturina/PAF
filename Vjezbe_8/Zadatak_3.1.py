import Projectile as pr
import matplotlib.pyplot as plt
import numpy as np

p1 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p1.__init__(60, 15, 0.01, 0, 0, 1, 1.29, 1, 1)

def graf_domet_koeficijent_trenja():
    kft_ = []
    domet_ = []
    p1 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
    
    for kft in np.arange(0.1, 3.0, 0.1):
        p1.__init__(60, 15, 0.01, 0, 0, 1, 1.29, kft, 1)
        d = p1.Range()
        domet_.append(d)
        kft_.append(kft)

    plt.plot(kft_, domet_, 'b')
    plt.xlabel("koeficijent trenja")
    plt.ylabel("domet")
    plt.title("Ovisnost dometa o koeficijentu trenja")
    plt.pause(3)
    plt.close

def graf_domet_masa():
    m_ = []
    domt_ = []
    p1 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
    
    for m in np.arange(0.1, 11, 0.1):
        p1.__init__(60, 15, 0.01, 0, 0, m, 1.29, 1, 1)
        d = p1.Range()
        domt_.append(d)
        m_.append(m)

    plt.plot(m_, domt_, 'b')
    plt.xlabel("masa")
    plt.ylabel("domet")
    plt.title("Ovisnost dometa o masi cestice")
    plt.pause(5)
    plt.close

graf_domet_koeficijent_trenja()
plt.clf()
graf_domet_masa()