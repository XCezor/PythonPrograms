from turtle import Turtle

MOVE_DISTANCE = 20

class PaletteGenerator(Turtle):

    def __init__(self, number):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.left(90)
        self.goto(number, 0)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def palette_move_up(self):
        self.forward(MOVE_DISTANCE)

    def palette_move_down(self):
        self.forward(MOVE_DISTANCE * -1)