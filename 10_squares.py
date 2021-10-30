import turtle
step = int(input('Введите ширину квадрата  '))

turtle.ht()
turtle.speed(10)
a = 1
counter = 1
x = turtle.xcor()
y = turtle.ycor()

while counter <= 40:
    counter += 1
    turtle.forward(step)
    turtle.left(90)
    a += 1
    if (a % 4) == 1:
        turtle.penup()
        x -= 15
        y -= 15
        turtle.goto(x, y)
        turtle.pendown()
        step += 30
