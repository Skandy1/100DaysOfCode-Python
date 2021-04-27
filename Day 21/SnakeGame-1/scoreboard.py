from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=280)
        self.update()

    def collide(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=("Arial", 12, "normal"), move=False)

    def game_over(self):
        self.goto(0, 0)
        self.write("~Game Over~", align="center", font=("Arial", 12, "normal"), move=False)
