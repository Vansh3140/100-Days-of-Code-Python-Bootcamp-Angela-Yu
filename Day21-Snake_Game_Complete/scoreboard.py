from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-30,270)
        self.color("white")
        self.hideturtle()
        self.change_score(0)

    def change_score(self,score):
        self.clear()
        self.write(f"Score : {score}", move=False, align="center", font=("Arial", 16, "bold"))