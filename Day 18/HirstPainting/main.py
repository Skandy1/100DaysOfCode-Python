from turtle import Turtle, Screen
import random

rgb_colors = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63),
              (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20),
              (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217),
              (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]
bobby = Turtle()
screen = Screen()
bobby.speed(0)
screen.colormode(255)
bobby.penup()
bobby.hideturtle()
bobby.setheading(225)
bobby.forward(250)
bobby.setheading(0)
bobby.pencolor(random.choice(rgb_colors))
for _ in range(10):
    for _ in range(10):
        bobby.pencolor(random.choice(rgb_colors))
        bobby.dot(20)
        bobby.forward(50)
    bobby.left(90)
    bobby.forward(50)
    bobby.left(90)
    bobby.forward(50*10)
    bobby.right(180)
screen.exitonclick()
