from turtle import Turtle,Screen
from obstacles import Obstacle
from scoreboard import ScoreBoard

#Main Screen
screen=Screen()
screen.setup(width=800,height=600)
screen.title("Turtle_Crossing_Game")

#Tortoise
tortoise=Turtle()
tortoise.hideturtle()
tortoise.up()
tortoise.shape("turtle")
tortoise.setheading(90)
tortoise.goto(0,-280)
tortoise.showturtle()

def move():
    tortoise.forward(10)

screen.listen()
screen.onkey(key="Up",fun=move)

#Obstacles
obstacle = Obstacle()

#ScoreBoard
scoreboard=ScoreBoard()

def reset():

    tortoise.hideturtle()
    tortoise.goto(0, -280)
    tortoise.showturtle()
    for x in obstacle.turtles:
        x.hideturtle()
    obstacle.turtles=[]
    obstacle.step+=10

def hits_obstacle(tortoise,turtles):

    for x in turtles:
        if x.distance(tortoise)<40:
            return True

    return False

is_game_on=True

while is_game_on:
    obstacle.move()
    obstacle.spawn()

    if hits_obstacle(tortoise,obstacle.turtles):
        is_game_on=False
        break

    if tortoise.ycor()>260:
        scoreboard.level+=1
        reset()
        scoreboard.update()

if is_game_on==False:
    new_turtle=Turtle()
    new_turtle.hideturtle()
    new_turtle.write("Game Over!!",False,"center",("Arial",30,"bold"))

screen.exitonclick()