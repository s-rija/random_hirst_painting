import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50),
              (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
              (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
              (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185),
              (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83),
              (245, 205, 7), (35, 88, 88), (103, 24, 56)]

ashish = Turtle()

ashish.speed("fastest")
ashish.penup()
ashish.hideturtle()
ashish.pensize(5)
ashish.setheading(225)
ashish.forward(300)
ashish.setheading(0)

for dot_count in range(1, 101):
    ashish.dot(20, random.choice(color_list))
    ashish.forward(50)

    if dot_count % 10 == 0:
        ashish.setheading(90)
        ashish.forward(50)
        ashish.setheading(180)
        ashish.forward(500)
        ashish.setheading(0)

myscreen = Screen()
print(myscreen.canvwidth)
myscreen.exitonclick()
