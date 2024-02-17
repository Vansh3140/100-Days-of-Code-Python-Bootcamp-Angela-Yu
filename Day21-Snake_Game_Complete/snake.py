from turtle import Turtle

class Snake:

    def __init__(self):
        self.turtles=[]
        self.create_snake()

    def create_snake(self):
        for x in range(0, 3):
            new_turtle = Turtle("square")
            new_turtle.up()
            new_turtle.color("white")
            new_turtle.goto(x * -20, 0)
            self.turtles.append(new_turtle)

    def move(self):
        for x in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[x - 1].xcor()
            new_y = self.turtles[x - 1].ycor()
            self.turtles[x].goto(new_x, new_y)
        self.turtles[0].forward(10)

    def up(self):
        if self.turtles[0].heading()!=270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading()!=90:
            self.turtles[0].setheading(270)

    def left(self):
        if self.turtles[0].heading()!=0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading()!=180:
            self.turtles[0].setheading(0)

    def add_new(self):
        new_turtle = Turtle("square")
        new_turtle.up()
        new_turtle.color("white")
        l=len(self.turtles)
        x_cor=self.turtles[l-1].xcor()
        y_cor=self.turtles[l-1].ycor()
        new_turtle.goto(x_cor, y_cor)
        self.turtles.append(new_turtle)