
line_length = int(50)
import turtle
turtle.shape('turtle')
beginning_number_of_sides: int = 3
x = turtle.xcor()
y = turtle.ycor()
counter: int = 1


def line(line_length, angle_between_lines):
    """Draw the line and sets the angle"""
    turtle.forward(line_length)
    turtle.right(angle_between_lines)


def draw_polygon():
    """Draw the polygon and calculate the external angle"""
    global counter
# Формула вычисления внешнего угла правильного многоугольника
    angle: int = int((360 / beginning_number_of_sides))
    while counter <= beginning_number_of_sides:
        counter += 1
        line(line_length, angle)

#while counter <= 40:
#    counter += 1
#    turtle.forward(step)
#    turtle.left(90)
#    a += 1
#    if (a % 4) == 1:
#        turtle.penup()
#        x -= 15
#        y -= 15
#        turtle.goto(x, y)
#        turtle.pendown()
#        step += 30
draw_polygon()

