#rzut poziomy, zasięg
vx = 5
h = 2
g = 9.81
dt = 0.00001
y = h
x = 0
vy = 0

while y >= 0:
	dy = vy*dt + (g*dt**2)/2
	y = y - dy
	dx = vx*dt
	x = x + dx
	dv = g*dt
	vy = vy + dv
print (x)
zasieg = 2/3 * x
print (zasieg)
