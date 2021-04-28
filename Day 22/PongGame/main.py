from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from line import Line
import time

# screen
screen_obj = Screen()
screen_obj.setup(width=800, height=600)
screen_obj.bgcolor("black")
screen_obj.title("Pong Game ")
screen_obj.tracer(0)
# line
line=Line()
# paddle
paddle_1 = Paddle(360, 0)
paddle_2 = Paddle(-360, 0)
# ball
ball = Ball()
# scores
score = ScoreBoard()
# screen onkey
screen_obj.listen()
screen_obj.onkeypress(key="Up", fun=paddle_1.move_up)
screen_obj.onkeypress(key="Down", fun=paddle_1.move_down)
screen_obj.onkeypress(key="w", fun=paddle_2.move_up)
screen_obj.onkeypress(key="s", fun=paddle_2.move_down)
# driver code
time.sleep(5)
is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen_obj.update()
    ball.move_fd()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # collision with  paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # out of xcor
    if ball.xcor() > 380:
        ball.reset_position()
        score.add_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.add_r()
    if score.l_score == 5 or score.r_score == 5:
        is_on = False
        if score.l_score == 5:
            score.game_over(100, 0)
        else:
            score.game_over(-100, 0)

screen_obj.exitonclick()
