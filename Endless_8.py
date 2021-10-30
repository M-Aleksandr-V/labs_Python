import turtle
turtle.shape('turtle')
turtle.speed(10)
def circle1(step,angle):
    turtle.forward(step)
    turtle.left(angle)
def circle2(step2,angle2):
    turtle.forward(step2)
    turtle.right(angle2)
    
for _ in range(60):
    circle1(4,3)

for _ in range(120):
    circle2(4,3)

for _ in range(60):
    circle1(4,3)
