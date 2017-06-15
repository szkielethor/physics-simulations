#symulacja rzutu z pierwsza predkoscia kosmiczna
from visual import *

G = 6.671e-11 #stala grawitacji to 6,671 x 10^(-11)

earth = sphere(pos=(0,0,0), radius=6.371e6, color=color.blue)
earth.mass = 6e24

satellite = sphere(pos=(6.372e6,0,0), radius=1e3)
satellite.mass = 1e6
# pierwszakosmiczna
velocity = sqrt((G*earth.mass) / (mag(satellite.pos)))
satellite.velocity = vector(0,0,velocity)
dt = 1e2

while True:
    rate(200)
    dist = satellite.pos - earth.pos
    acce = velocity**2 * dist / mag(dist)**3
    satellite.velocity = satellite.velocity + acce*dt
    satellite.pos = satellite.pos + satellite.velocity*dt
