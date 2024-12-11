from turtle import Turtle, Screen
import random as r

def turtle_square(move):
    tim.forward(move)
    tim.right(90)
    tim.forward(move)
    tim.right(90)
    tim.forward(move)
    tim.right(90)
    tim.forward(move)


def dashed_line(move, repeats):
    while repeats > 0:
        tim.forward(move / 2)
        tim.penup()
        tim.forward(move / 2)
        tim.pendown()
        repeats -= 1

def random_walk(move):
    while True:
        tim.forward(move)
        rotate = r.choice([90, 180, 270, 360])
        tim.right(rotate)
        color = r.choice(["white", "green", "blue", "red", "yellow", "pink", "black", "purple"])
        tim.pencolor(color)

tim = Turtle()
#tim.shape("turtle")
tim.color("red")
tim.pensize(20)
tim.speed(15)
#turtle_square(50)
#dashed_line(20, 5)
random_walk(30)

screen = Screen()
screen.exitonclick()
