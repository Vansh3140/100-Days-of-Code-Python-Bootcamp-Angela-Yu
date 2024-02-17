from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.up()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,False,"center",("Courier",80,"bold"))
        self.goto(100, 200)
        self.write(self.r_score, False, "center", ("Courier", 80, "bold"))