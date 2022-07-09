from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

main_paddle = Paddle((0, -250))
ball = Ball()
colors = ["yellow", "green", "blue", "red"]

paddles = []
x_cor_paddles = -330
y_cor_paddles = 100
for y_cor in range(4):
    for _ in range(11):
        paddle = Paddle((x_cor_paddles, y_cor_paddles))
        paddle.shapesize(stretch_wid=1, stretch_len=3)
        paddle.color(colors[y_cor])
        x_cor_paddles += 65
        paddles.append(paddle)
    x_cor_paddles = -330
    y_cor_paddles += 30

screen.listen()
screen.onkey(main_paddle.go_left, "a")
screen.onkey(main_paddle.go_right, "d")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    #Detect collision with wall y
    if ball.ycor() > 280:
        ball.bounce_y()

        # Detect collision with wall x
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    #Detect collision with paddle
    if ball.distance(main_paddle) < 40 and ball.xcor() < 320:
        ball.bounce_y()

    #Detect R paddle misses
    if ball.ycor() < -250:
        ball.reset_position()

    for paddle in paddles:
        if ball.distance(paddle) < 40:
            ball.bounce_y()
            paddle.reset()
screen.exitonclick()