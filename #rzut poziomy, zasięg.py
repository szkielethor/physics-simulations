#rzut poziomy, zasięg
vx = 5
h = 2
g = 9.81
dt = 0.001
y = h
x = 0
vy = 0

while y >= 0:
	dy = vy*dt + (g*dt**2)/2
	y = y - dy
	dx = vx*dt
	x = x + dx
	dv = g*dt
	v = v + dv
print (x)

