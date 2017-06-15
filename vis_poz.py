# -*- coding: cp1250 -*-
from visual import *

#set up window
scena1 = display(title = "trajektoria wg. szkieleta", x = 100, y = 200, width = 1366,
                 height = 768, background = color.white)
#osie układu współrzędnych
osX = arrow(pos=(0,0,0), axis = vector (5,0,0), color = color.yellow)
osY = arrow(pos=(0,0,0), axis = vector (0,5,0), color = color.orange)
osZ = arrow(pos=(0,0,0), axis = vector (0,0,5), color = color.red)
#obiekty
gleba = box (pos=(0,0,15), length = 30, width = 10, height = 0.5, color = color.green)
obelisk = box (pos=(1,10,1), length = 2, width = 2, height = 20, color = color.cyan)
kula = sphere (pos=(1, 21, 1), radius = 1, color = color.blue)
#v_poz = arrow (pos=(0,0,0), axis = vector(10,10,0), color = color.red)
dt = 0.1

while kula.pos.y > 1:
    rate(30)
    kula.pos = kula.pos + (0.125,-9.81*dt**2,0)
    
