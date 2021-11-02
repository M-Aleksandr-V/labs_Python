import turtle
turtle.ht()
turtle.speed(10)
number_of_sides = 4
step = int(10)
a = 1
counter = 1
x = turtle.xcor()
y = turtle.ycor()
angle: int = int((360 / number_of_sides))
while counter <= number_of_sides*10 :
    counter += 1
    turtle.forward(step)
    turtle.left(angle)
    a += 1
    if (a % number_of_sides) == 1:
        turtle.penup()
        x -= 10
        y -= 10
        turtle.goto(x, y)
        turtle.pendown()
        step += 20
