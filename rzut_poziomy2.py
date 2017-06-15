import time

vx = 13.0
y = 10.0
g = 9.81
vy = 0.0
x = 0.0
dt = 0.01
t = 0.0

while y > 0.0:
	x = x + vx*dt
	y = y - vy*dt - (g*dt**2)/2
	vy = vy + g*dt
	time.sleep(dt-0.003)
	print (t)
	t = t + dt
	print (x)

print (x)