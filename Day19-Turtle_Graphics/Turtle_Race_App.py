from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Who will win the race? type the colour out of VIGBYOR:")
colors=["red","yellow","orange","green","blue","violet","indigo"]
turtles=[]

for x in range(0,7):
    q=Turtle(shape="turtle")
    q.up()
    q.color(colors[x])
    q.goto(x=-230,y=x*30-100)
    turtles.append(q)

if user_bet:
    is_race_on=True

winner="None"

while is_race_on:
    for x in range(0,7):
        num=random.randint(0,10)
        turtles[x].forward(num)
        if turtles[x].xcor()>=250:
            winner=colors[x]
            is_race_on=False
            break

if user_bet==winner:
    print(f"Hurray!! You won and the winner is {user_bet} turtle")
else:
    print(f"Alas!! You lose and the winner is {winner} turtle")

screen.exitonclick()