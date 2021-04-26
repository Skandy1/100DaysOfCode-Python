from turtle import Screen, Turtle
from snake import Snake
import time
is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Mania ")
screen.tracer(0)
screen.listen()
new_snake_obj=Snake()
screen.onkey(key="Up",fun=new_snake_obj.up)
screen.onkey(key="Down",fun=new_snake_obj.down)
screen.onkey(key="Left",fun=new_snake_obj.left)
screen.onkey(key="Right",fun=new_snake_obj.right)

while is_on:
    screen.update()
    time.sleep(0.1)
    new_snake_obj.move()


screen.exitonclick()
