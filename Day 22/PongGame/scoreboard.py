from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def add_l(self):
        self.l_score += 1
        self.update()

    def add_r(self):
        self.r_score += 1
        self.update()
    def game_over(self,g_x,g_y):
        self.goto(g_x,g_y)
        self.write("~You Won~", align="center", font=("Courier", 20, "normal"))
