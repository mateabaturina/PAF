import Enterprise as gr
import matplotlib.pyplot as plt
import numpy as np

Earth = {"xz": 1.486*10**11, "yz": 0, "mass":5.9742*10**24, "vxz":0, "vyz": 29783, "r": 6.371*1e6}
Sun = {"xz": 0, "yz": 0, "mass":1.989*10**30, "vxz":0, "vyz": 0, "r": 0.696*1e9}
Mercury = {"xz":1.486*10**11 * 0.466 , "yz": 0, "mass":3.3e24, "vxz":0, "vyz":47632, "r": 2.439*1e6}
Venus = {"xz":1.486*10**11 * 0.723 , "yz": 0, "mass":4.8685e24, "vxz":0, "vyz":35020, "r": 6.051*1e6}
Mars = {"xz":1.486*10**11 * 1.666 , "yz": 0, "mass":6.417e23, "vxz":0, "vyz":24007, "r": 3.389*1e6}


bodies = [
        gr.Planet( xz = Sun["xz"], yz = Sun["yz"], Mz = Sun["mass"], vxz = Sun["vxz"], vyz = Sun["vyz"], name = "Sun", color = "yellow", r =Sun["r"]),
        gr.Planet( xz = Earth["xz"], yz = Earth["yz"], Mz = Earth["mass"], vxz = Earth["vxz"], vyz = Earth["vyz"], name = "Earth", color = "blue", r =Earth["r"]),
        gr.Planet( xz = Mercury["xz"], yz = Mercury["yz"], Mz = Mercury["mass"], vxz = Mercury["vxz"], vyz = Mercury["vyz"], name = "Mercury", color = "orange", r =Mercury["r"]),
        gr.Planet( xz = Venus["xz"], yz = Venus["yz"], Mz = Venus["mass"], vxz = Venus["vxz"], vyz = Venus["vyz"], name = "Venus", color = "red", r =Venus["r"]),
        gr.Planet( xz = Mars["xz"], yz = Mars["yz"], Mz = Mars["mass"], vxz = Mars["vxz"], vyz = Mars["vyz"], name = "Mars", color = "brown", r =Mars["r"]),
        ]

for i in range(1000):
        mass = np.random.uniform(1.0*10**13, 9.9*10**13)
        r = np.random.uniform(0.1*10**3, 0.5*10**3)
        vxz = np.random.uniform(-1.0*10**4, -4.0*10**4)
        vyz = np.random.uniform(-1.0*10**4, -4.0*10**4)
        xz = np.random.uniform(1.600*10**11 * 1.666, 4*1.496e11 )
        yz = np.random.uniform(0, 0)
        Comet = {"xz": xz, "yz": yz, "mass":mass, "vxz": vxz, "vyz": vyz, "r": r}
        a = gr.Planet( xz = Comet["xz"], yz = Comet["yz"], Mz = Comet["mass"], vxz = Comet["vxz"], vyz = Comet["vyz"], name = "Comet", color = "white", r = Comet["r"])
        bodies.append(a)

dt = (60*60*24)/10
dan = 60*60*24
c = dan*365.242

p1 = gr.Gravity(6.67408*10**(-11), dt, c*5)
sun, earth, mercury, venus, mars = p1.Eulerova_metoda(bodies)

b = 0.175*1.496e11
bins = [0, b, 2*b, 3*b, 4*b, 5*b, 6*b, 7*b, 8*b, 9*b, 10*b, 11*b, 12*b, 13*b, 14*b, 15*b, 16*b, 17*b, 18*b, 19*b, 20*b]

fig, axs = plt.subplots(1, 5, sharey = True, tight_layout = True)
axs[0].hist(sun, bins = bins, edgecolor="black")
axs[0].set_title("Sun")
axs[0].set_xlabel("Distance [au]")
axs[0].set_ylabel("Number of comets")
axs[1].hist(mercury, bins = bins, edgecolor="black")
axs[1].set_title("Mercury")
axs[1].set_xlabel("Distance [au]")
axs[1].set_ylabel("Number of comets")
axs[2].hist(venus, bins = bins, edgecolor="black")
axs[2].set_title("Venus")
axs[2].set_xlabel("Distance [au]")
axs[2].set_ylabel("Number of comets")
axs[3].hist(earth, bins = bins, edgecolor="black")
axs[3].set_title("Earth")
axs[3].set_xlabel("Distance [au]")
axs[3].set_ylabel("Number of comets")
axs[4].hist(mars, bins = bins, edgecolor="black")
axs[4].set_title("Mars")
axs[4].set_xlabel("Distance [au]")
axs[4].set_ylabel("Number of comets")

plt.show()
#plt.savefig("histogram.jpg")
