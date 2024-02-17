from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        self.spawn_food()

    def spawn_food(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.goto(x,y)
