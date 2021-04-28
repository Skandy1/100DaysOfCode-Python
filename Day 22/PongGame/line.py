from turtle import Turtle
class Line(Turtle):
    def __init__(self):
        super(Line, self).__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,-290)
        self.left(90)
        self.draw_line()
    def draw_line(self):
        while self.ycor()<=290:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
