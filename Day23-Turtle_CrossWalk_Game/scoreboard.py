from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level=1
        self.up()
        self.hideturtle()
        self.goto(-350,260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level {self.level}",False,"center",("Arial",15,"bold"))