#
from math import sqrt

#input
m = 6e9    #v gives orbital velocity for satellites, if m is 
M = 6e24   #small
d = 384e6

#gravitational constant
G = 6.671e-11

r = d/(m/M+1) #formula derived using center of mass equation
R = d-r

#velocities (formulas deriver from II Newtons law and
#relation beetwen kinetic and potential energy)
V = sqrt(G*m/d * (1 - r/d))
v = sqrt(G*M/d * (1 - R/d))

P = M*V
p = m*v

print ("r = ", r, "v = ", v)
print ("R = ", R, "V = ", V)
print ("P = ", P, "p = ", p)