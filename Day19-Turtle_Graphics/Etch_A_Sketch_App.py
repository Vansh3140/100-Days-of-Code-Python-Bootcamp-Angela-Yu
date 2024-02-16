from turtle import Turtle,Screen

slack=Turtle()

def move_forward():
    slack.forward(20)

def move_backward():
    slack.backward(20)

def move_left():
    slack.lt(20)

def move_right():
    slack.rt(20)

def move_default():
    slack.reset()

screen=Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="c",fun=move_default)
screen.exitonclick()