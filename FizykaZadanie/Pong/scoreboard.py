from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "bold")
END_FONT = ("Courier", 30, "bold")

class ScoreBoard(Turtle):

    def __init__(self, score, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(position, 160)
        self.speed("fastest")
        self.clear()
        self.write(f"{score}", False, align=ALIGNMENT, font=FONT)

    def score(self, score):
        self.clear()
        self.write(f"{score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"The winner is: {winner}", False, align=ALIGNMENT, font=END_FONT)