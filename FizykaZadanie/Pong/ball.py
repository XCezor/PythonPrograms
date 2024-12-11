from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def ball_move(self, wall_collision, palette_collision, ball_y_speed, ball_x_speed):
        if not wall_collision:
            new_y = self.ycor() + ball_y_speed
        else:
            new_y = self.ycor() - ball_y_speed

        if not palette_collision:
            new_x = self.xcor() + ball_x_speed
        else:
            new_x = self.xcor() - ball_x_speed
        self.goto(new_x, new_y)