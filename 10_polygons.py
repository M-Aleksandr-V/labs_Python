
line_length = int(input('Enter the length  : '))
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


draw_polygon()
