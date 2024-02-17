from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.color("white")
        self.up()
        self.goto(x,y)
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)

    def move_up(self):
        y_cor=self.ycor()
        if y_cor+20<260:
            self.goto(self.xcor(),y_cor+20)

    def move_down(self):
        y_cor = self.ycor()
        if y_cor-20>-260:
            self.goto(self.xcor(), y_cor-20)