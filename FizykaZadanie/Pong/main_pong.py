import time
import threading
import keyboard
from playsound import playsound
from turtle import Screen
from pong_palette import PaletteGenerator
from ball import Ball
from scoreboard import ScoreBoard

sound1_path = "pong1.mp3"
sound2_path = "pong2.mp3"

def play_sound1(sound1_path):
    playsound(sound1_path)
def play_sound2(sound2_path):
    playsound(sound2_path)

screen = Screen()
screen.setup(700, 500)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)


screen.update()
palette1 = PaletteGenerator(-320)
palette2 = PaletteGenerator(312)
ball = Ball()
p1 = ScoreBoard(0, -40)
p1_score = 0
p2 = ScoreBoard(0, 40)
p2_score = 0
x_speed = 5
y_speed = 5

screen.listen()
screen.onkey(palette1.palette_move_up, "w")
screen.onkey(palette1.palette_move_down, "s")
screen.onkey(palette2.palette_move_up, "Up")
screen.onkey(palette2.palette_move_down, "Down")

game_is_running = True
wall_collision = False
palette_collision = False
while game_is_running:
    screen.update()
    time.sleep(0.03)
    ball.ball_move(wall_collision, palette_collision, x_speed, y_speed)

    if ball.ycor() > 234:
        wall_collision = True
        sound_thread = threading.Thread(target=play_sound2, args=(sound2_path,))
        sound_thread.start()
    elif ball.ycor() < -232:
        wall_collision = False
        sound_thread = threading.Thread(target=play_sound2, args=(sound2_path,))
        sound_thread.start()

    if ball.distance(palette2) < 75 and ball.xcor() > 290:
        palette_collision = True
        x_speed += 2
        y_speed += 2
        sound_thread = threading.Thread(target=play_sound1, args=(sound1_path,))
        sound_thread.start()
    elif ball.distance(palette1) < 75 and ball.xcor() < -298:
        palette_collision = False
        sound_thread = threading.Thread(target=play_sound1, args=(sound1_path,))
        sound_thread.start()
        x_speed += 2
        y_speed += 2

    if ball.xcor() > 310:
        ball.goto(0, 0)
        x_speed = 5
        y_speed = 5
        palette_collision = True
        p1_score += 1
        p1.score(p1_score)
    elif ball.xcor() < -318:
        ball.goto(0, 0)
        x_speed = 5
        y_speed = 5
        palette_collision = False
        p2_score += 1
        p2.score(p2_score)
    game_is_running = False if p1_score == 5 or p2_score == 5 else True

if p1_score == 5:
    p1_winner = "Player 1"
    p1.game_over(p1_winner)
elif p2_score == 5:
    p2_winner = "Player 2"
    p2.game_over(p2_winner)

screen.exitonclick()