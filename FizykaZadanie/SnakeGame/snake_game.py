from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
difficulty = screen.numinput("Difficulty", "Choose from 1 to 3:", minval=1, maxval=3)

screen.update()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
score = 0

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
if difficulty == 1:
    game_speed = 0.12
elif difficulty == 2:
    game_speed = 0.1
else:
    game_speed = 0.08

while game_is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score = scoreboard.gain_score(score)
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.move()
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()