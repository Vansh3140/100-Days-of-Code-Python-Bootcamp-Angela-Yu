# import colorgram
#
# colors=colorgram.extract('hirst.jpg',30)
# colors_rgb=[]
#
# for x in range(len(colors)-1):
#     r=colors[x].rgb[0]
#     g=colors[x].rgb[1]
#     b=colors[x].rgb[2]
#     colors_rgb.append((r,g,b))
#
# print(colors_rgb)

from turtle import *
import random

color_list=[(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65)]\

slack=Turtle()
slack.speed("fastest")

def draw_circle():
    colormode(255)
    num=random.randint(0,len(color_list)-1)
    slack.color(color_list[num])
    slack.begin_fill()
    slack.circle(10)
    slack.end_fill()
    slack.up()
    slack.forward(60)
    slack.down()

for x in range(10):
    slack.up()
    slack.sety(-200+x*60)
    slack.setx(-50)
    for y in range(10):
        slack.hideturtle()
        draw_circle()


screen=Screen()
screen.exitonclick()