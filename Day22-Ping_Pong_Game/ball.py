from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.shape("circle")
        self.up()
        self.color("white")

    def move(self,x,y):
        x_cor=self.xcor()+x
        y_cor=self.ycor()+y
        self.goto(x_cor,y_cor)

    def reset(self):
        self.goto(0, 0)