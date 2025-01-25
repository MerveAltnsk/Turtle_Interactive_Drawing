import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("cornsilk")
drawing_board.title("Python Turtle Drawing")

turtle1 = turtle.Turtle()
turtle1.pencolor("green")
turtle1.speed(0)
turtle1.shape("turtle")


def turtle_forward():
    turtle1.forward(100)

def rotate_angle_right():
    turtle1.setheading(turtle1.heading() - 10)
    #turtle1.right(10)


def rotate_angle_left():
    turtle1.setheading(turtle1.heading() + 10)
    #turtle1.left(10)

def clear_screen():
    turtle1.clear()

def turtle_return_home():
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()

def turtlpen_up():
    turtle1.up()

def turtlpen_down():
    turtle1.down()


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angle_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=turtle_return_home, key="h")
drawing_board.onkey(fun=turtlpen_up, key="w")
drawing_board.onkey(fun=turtlpen_down, key="s")











turtle.mainloop()