import turtle
step = int(10)
turtle.ht()
turtle.speed(10)
a = 1
counter = 1


while counter <= 41:
    counter += 1
    turtle.forward(step)
    turtle.left(90)
    a += 1
    if (a % 2) == 1:
        step += 10
