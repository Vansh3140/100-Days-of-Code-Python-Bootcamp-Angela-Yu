import turtle
import pandas as pd

#Creating Screen
screen=turtle.Screen()
screen.title("U.S.A Map Guessing")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#Reading data

data=pd.read_csv("50_states.csv")

#Function to write country name

def write_country(x,y,guess):
    new_turtle = turtle.Turtle()
    new_turtle.up()
    new_turtle.hideturtle()
    new_turtle.goto(x, y)
    new_turtle.write(f"{guess}", move=False, align="center")

score=0

while score!=50:
    guess=screen.textinput(title=f"{score}/50 Points",prompt="Guess a State Name")

    country_data=data[data.state.str.lower()==guess.lower()]
    # print(country_data)
    if len(country_data)>0:
        x_cor=country_data["x"].to_list()[0]
        y_cor=country_data["y"].to_list()[0]
        score+=1
        write_country(x_cor,y_cor,country_data["state"].to_list()[0])

screen.exitonclick()