import turtle
import math
i = float(1)
x = float(1)
y = float(1)

while i < 50:
    
    phi = float(i * 1)
    r = float(2 * i)
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    print(x,y)
    turtle.goto(x,y)
    i+= 0.1
    
    
