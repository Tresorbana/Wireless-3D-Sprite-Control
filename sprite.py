import utils.session
import serial
import time
from vpython import box, vector, rate, color, cylinder, compound

bluetooth = serial.Serial('COM5', 9600)  
time.sleep(2)
body = box(size=vector(1, 1, 1), color=color.cyan, opacity=0.8)
arm1 = cylinder(pos=vector(-0.5, 0, 0), axis=vector(1, 0, 0), radius=0.05, color=color.yellow)
arm2 = cylinder(pos=vector(0, -0.5, 0), axis=vector(0, 1, 0), radius=0.05, color=color.yellow)
sprite = compound([body, arm1, arm2])

sprite.pos = vector(0, 0, 0)
trail_points = [] 
def draw_trail(pos):
    if len(trail_points) > 15:
        old = trail_points.pop(0)
        old.visible = False
    p = box(pos=pos, size=vector(0.05, 0.05, 0.05), color=color.white, opacity=0.3)
    trail_points.append(p)

while True:
    rate(50)
    data = bluetooth.readline().decode().strip()

    try:
        xVal, yVal, button = map(int, data.split(','))
        
        x = (xVal - 512) / 100
        y = (yVal - 512) / 100

        sprite.pos.x = x
        sprite.pos.y = y

        draw_trail(sprite.pos)

        sprite.color = vector(abs(x)/5, abs(y)/5, 1 - (abs(x+y)/10))

        sprite.rotate(angle=0.05, axis=vector(0, 1, 0))

        if button == 0:
            sprite.size = vector(1.2, 1.2, 1.2) 
        else:
            sprite.size = vector(1, 1, 1)

    except:
        pass
