import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
carManager = CarManager()
player = Player()
screen.listen()
screen.onkeypress(key="Up", fun=player.move)
game_is_on = screen.textinput("input","Game start?")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_car()
    carManager.move()
    if player.isAtFinishLine():
        player.goToStart()
        scoreboard.level_up()
        carManager.move_increment()
    for cars in carManager.all_cars:
        if cars.distance(player) < 27:
            scoreboard.end_game()
            game_is_on = False
    # detect a successful game

screen.exitonclick()
