import Bullet as bl

m1 = bl.Bullet(1, 2, 5) # br. metka, h0, v0

# z==0 za smanjiti, z==1 za povećati
m1.change_h0(1, 1) # z, n
m1.change_v0(1, 1) # z, n
print("Nova visina metka {} je {}.".format(1,m1.h0))
print("Nova brzina metka {} je {}.".format(1, m1.v0))

m2 = bl.Bullet(2, 3, 6)

m2.change_h0(0, 2) # z, n
m2.change_v0(0, 2) # z, n
print("Nova visina metka {} je {}.".format(2, m2.h0))
print("Nova brzina metka {} je {}.".format(2, m2.v0))
