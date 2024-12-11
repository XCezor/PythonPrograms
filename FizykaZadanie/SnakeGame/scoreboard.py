import turtle
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.speed("fastest")
        self.clear()
        self.write("Score: 0", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def gain_score(self, score):
        score = score + 1
        self.clear()
        self.write(f"Score: {score}", False, align=ALIGNMENT, font=FONT)
        return score