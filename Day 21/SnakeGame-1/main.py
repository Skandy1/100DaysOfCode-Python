from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Mania ")
screen.tracer(0)
screen.listen()
new_snake_obj = Snake()
new_food_obj = Food()
new_scoreboard_obj = ScoreBoard()
screen.onkey(key="Up", fun=new_snake_obj.up)
screen.onkey(key="Down", fun=new_snake_obj.down)
screen.onkey(key="Left", fun=new_snake_obj.left)
screen.onkey(key="Right", fun=new_snake_obj.right)

while is_on:
    screen.update()
    time.sleep(0.1)
    new_snake_obj.move()
    #     collision with food
    if new_snake_obj.head.distance(new_food_obj) < 15:
        new_food_obj.refresh()
        new_scoreboard_obj.collide()
        new_snake_obj.extend()

    # collision with wall
    if new_snake_obj.head.xcor() > 280 or new_snake_obj.head.xcor() < -280 or new_snake_obj.head.ycor() > 280 \
            or new_snake_obj.head.xcor() < -280:
        is_on = False
        new_scoreboard_obj.game_over()
    # collision with tail
    for seg in new_snake_obj.segments[1:]:
        if new_snake_obj.head.distance(seg) < 10:
            is_on = False
            new_scoreboard_obj.game_over()

screen.exitonclick()
