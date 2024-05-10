import turtle


def test_ok_1():
    # Create turtle and draw a square
    my_turtle = turtle.Turtle()
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)

    # Finish drawing
    turtle.done()


def test_violation_1():
    # Create turtle and draw a square
    my_turtle = turtle.Turtle()
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)

    # Finish drawing
    turtle.done()

    # Attempt to change the turtle color and move it again
    my_turtle.color("red")
    my_turtle.forward(200)
