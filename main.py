from turtle import *
kafil=Turtle()
screen=Screen()
def move_forward():
    kafil.forward(100)
def move_right():
    kafil.right(100)
def move_left():
    kafil.left(100)
def move_backward():
    kafil.backward(100)
def clear_all():
    kafil.speed(1000)
    kafil.home()
    kafil.clear()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.listen()
screen.onkey(key="a",fun=move_left)
screen.listen()
screen.onkey(key="s",fun=move_backward)
screen.listen()
screen.onkey(key="d",fun=move_right)
screen.listen()
screen.onkey(key="c",fun=clear_all)
screen.exitonclick()












