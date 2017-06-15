from visual import *
from math import sqrt

G = 6.671e-11
M = 5.98e24
m = 1.0e22
R = 6.4e6
r = 8.0e6

earth = sphere(pos=(0,0,0), radius=R, color=color.blue)

satellite = sphere(pos=(r,0,0), radius=100.0e3, color=color.yellow, 
	make_trail=True, interval=10, retain=200)
#calculating orbital speed
velocity = 8e3#sqrt(G*M / r)

satellite.p = vector(0,0,velocity)*m #satellite's momentum

dt = 1e9

while True:
	rate(200)

	dist = satellite.pos - earth.pos
	force = G*M*m*dist / mag(dist)**3
	satellite.p = satellite.p - force*dt
	satellite.pos = satellite.pos + satellite.pos/m * dt

	

