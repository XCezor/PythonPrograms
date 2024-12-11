from turtle import Turtle, Screen
import random as r

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "black"]

y_pos = -125
turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos)
    y_pos += 50
    turtles.append(new_turtle)

race_is_going = True
while race_is_going:
    for turtle in turtles:
        random_move = r.randint(1, 15)
        turtle.forward(random_move)
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You lost! The {winner_color} turtle is the winner!")
            race_is_going = False
screen.bye()