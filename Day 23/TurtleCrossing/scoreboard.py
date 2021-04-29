from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level=0
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.write_on_screen()
    def write_on_screen(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
    def level_up(self):
        self.level+=1
        self.write_on_screen()
    def end_game(self):
        self.goto(0,0)
        self.write("~ Game Over ~",align="center",font=FONT)


