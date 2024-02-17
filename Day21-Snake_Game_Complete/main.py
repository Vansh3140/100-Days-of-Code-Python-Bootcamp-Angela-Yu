from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

game_is_on=True
score=0

def Game_Over():
    game_over = Turtle()
    game_over.up()
    game_over.goto(0,0)
    game_over.color("white")
    game_over.write("Game Over !!",False,"center",("Arial",40,"bold"))

def is_not_safe(jimmy):

    if jimmy.xcor()>280 or jimmy.xcor()<-280:
        return False
    elif jimmy.ycor()>280 or jimmy.ycor()<-280:
        return False
    else:
        return True

def tail_collide(snake):
    head=snake.turtles[0]
    for x in range(1,len(snake.turtles)-1):
        if snake.turtles[x].distance(head)<10:
            return True

    return False


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.turtles[0].distance(food)<15:
        score+=1
        food.spawn_food()
        scoreboard.change_score(score)
        snake.add_new()

    if is_not_safe(snake.turtles[0])==False:
        game_is_on=False
        break

    if tail_collide(snake):
        game_is_on = False
        break

Game_Over()

screen.exitonclick()
