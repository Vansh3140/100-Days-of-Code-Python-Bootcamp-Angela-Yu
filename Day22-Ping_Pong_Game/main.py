from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

#Creating Paddles

r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)

#Creating Ball

ball=Ball()

#Creating ScoreBoard

scoreboard=ScoreBoard()

#Main Screen

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ping Pong Game")
screen.tracer(0)

#Movement of Paddles

screen.listen()
screen.onkey(key="Up",fun=r_paddle.move_up)
screen.onkey(key="Down",fun=r_paddle.move_down)
screen.onkey(key="w",fun=l_paddle.move_up)
screen.onkey(key="s",fun=l_paddle.move_down)

is_game_on=True
x=10
y=10
speeds=0.1

while is_game_on:
    time.sleep(speeds)
    screen.update()

    #Detect Collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        y*=-1

    #Detect Collision with right paddle
    if ball.xcor()>330 and r_paddle.distance(ball)<50:
        x*=-1
    elif ball.xcor()>330:
        ball.reset()
        scoreboard.l_score+=1
        x = -abs(x)
        y = -abs(y)
        speeds/=1.2

    # Detect Collision with left paddle
    if ball.xcor()<-330 and l_paddle.distance(ball)<50:
         x*=-1
    elif ball.xcor()<-330:
        ball.reset()
        scoreboard.r_score+=1
        x = abs(x)
        y = abs(y)
        speeds/=1.2

    scoreboard.update_scoreboard()
    ball.move(x,y)

screen.exitonclick()