from turtle import Turtle, Screen
import random
is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:")
print(user_bet)
colors = ["red", "orange", "purple", "green", "yellow", "blue"]
y_pos = [-120, -80, -40, 0, 40, 80]
all_turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_on = True

while is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won. The {winning_color} turtle is the winner.")
            else:
                print(f"You Lost. The {winning_color} turtle is the winner.")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
