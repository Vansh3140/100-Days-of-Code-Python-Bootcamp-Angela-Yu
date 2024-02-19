from turtle import Turtle,colormode
import random
import time

random_numbers=[]

for x in range(-280,281,50):
    random_numbers.append(x)

class Obstacle(Turtle):

    def __init__(self):
        super().__init__()
        self.turtles=[]
        self.step = 25
        self.spawn()

    def random_color(self):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        return (r,g,b)

    def spawn(self):

        y_cor=random.choice(random_numbers)
        new_turtle=Turtle()
        new_turtle.hideturtle()
        new_turtle.shape("square")
        new_turtle.shapesize(1,3)
        new_turtle.up()
        new_turtle.goto(360,y_cor)
        new_turtle.showturtle()
        colormode(255)
        new_turtle.color(self.random_color())
        self.turtles.append(new_turtle)

    def move(self):

        for x in self.turtles:
            x.backward(self.step)
