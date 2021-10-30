import turtle
turtle.shape('turtle')
#turtle.speed(50)
number_of_sides: float = float(input('Enter the number_of_sides :  '))

counter: int = 1


def line(line_length, angle_between_lines):
    """Draw the line and sets the angle"""
    turtle.forward(line_length)
    turtle.right(angle_between_lines)


def draw_polygon():
    """Draw the polygon and calculate the external angle"""
    global counter
# Формула вычисления внешнего угла правильного многоугольника
    angle: float = float((360 / number_of_sides))
    while counter <= number_of_sides:
        counter += 1
        line(line_length, angle)
        print(angle)


if number_of_sides > 2:
    line_length = float(input('Enter the length  : '))
    draw_polygon()
else:
    number_of_sides: float = float(input('Enter the number_of_sides > 2 :  '))
    line_length = float(input('Enter the length  : '))
    draw_polygon()
