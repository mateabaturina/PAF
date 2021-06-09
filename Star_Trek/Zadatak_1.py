import Enterprise as gr
import matplotlib.pyplot as plt

Earth = {"xz": 1.486*10**11, "yz": 0, "mass":5.9742*10**24, "vxz":0, "vyz": 29783}
Sun = {"xz": 0, "yz": 0, "mass":1.989*10**30, "vxz":0, "vyz": 0}
Mercury = {"xz":1.486*10**11 * 0.466 , "yz": 0, "mass":3.3e24, "vxz":0, "vyz":47632}
Venus = {"xz":1.486*10**11 * 0.723 , "yz": 0, "mass":4.8685e24, "vxz":0, "vyz":35020}
Mars = {"xz":1.486*10**11 * 1.666 , "yz": 0, "mass":6.417e23, "vxz":0, "vyz":24007}
Comet = {"xz":4*1.496e11 , "yz": 4*1.496e11, "mass":1e14, "vxz":-20000, "vyz":-15000}

bodies = [
        gr.Planet( xz = Sun["xz"], yz = Sun["yz"], Mz = Sun["mass"], vxz = Sun["vxz"], vyz = Sun["vyz"], name = "Sun", color = "yellow"),
        gr.Planet( xz = Earth["xz"], yz = Earth["yz"], Mz = Earth["mass"], vxz = Earth["vxz"], vyz = Earth["vyz"], name = "Earth", color = "blue"),
        gr.Planet( xz = Mercury["xz"], yz = Mercury["yz"], Mz = Mercury["mass"], vxz = Mercury["vxz"], vyz = Mercury["vyz"], name = "Mercury", color = "orange"),
        gr.Planet( xz = Venus["xz"], yz = Venus["yz"], Mz = Venus["mass"], vxz = Venus["vxz"], vyz = Venus["vyz"], name = "Venus", color = "red"),
        gr.Planet( xz = Mars["xz"], yz = Mars["yz"], Mz = Mars["mass"], vxz = Mars["vxz"], vyz = Mars["vyz"], name = "Mars", color = "brown"),
        gr.Planet( xz = Comet["xz"], yz = Comet["yz"], Mz = Comet["mass"], vxz = Comet["vxz"], vyz = Comet["vyz"], name = "Comet", color = "white"),
        ]

dt = (60*60*24)/10
dan = 60*60*24
c = dan*365.242

p1 = gr.Gravity(6.67408*10**(-11), dt, c*5)
#p1.Eulerova_metoda(bodies)

p1.Animation(bodies)


