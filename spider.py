import turtle
turtle.shape('turtle')
turtle.speed(50)
number_of_sides: float = float(input('Enter the number of lines :  '))
counter: int = 1


def line(line_length, angle: object) -> object:
    """Draw the line and sets the angle"""
    turtle.forward(line_length)
    turtle.stamp()
    turtle.goto(0, 0)
    assert isinstance(angle, object)
    turtle.right(angle)
    angle += angle


def draw_spider() -> object:
    """Draw the spider and calculate the angle between lines
    :rtype: object
    """
    global counter
    angle: float = float((360 / number_of_sides))
    while counter <= number_of_sides:
        counter += 1
        line(line_length, angle)
        print(angle)


if number_of_sides >= 1:
    line_length = float(input('Enter the length  : '))
    draw_spider()
else:
    number_of_sides: float = float(input("Enter the number_of_sides > 0 :  "))
    line_length = float(input("Enter the length  : "))
    draw_spider()
