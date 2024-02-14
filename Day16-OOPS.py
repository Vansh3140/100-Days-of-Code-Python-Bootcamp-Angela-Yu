from turtle import Turtle,Screen

timmy=Turtle()
my_screen=Screen()
timmy.shape("turtle")
timmy.forward(100)
timmy.color("cyan")

my_screen.exitonclick()

from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon_Name",["Charlizard","Pikachu","Squirtle"])
table.add_column("Type",["Fire","Electric","Water"])
table.align="r"
print(table)



