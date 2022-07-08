from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((50, -200))
# l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_left, "a")
screen.onkey(r_paddle.go_right, "d")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    #Detect collision with wall y
    if ball.ycor() > 280:
        ball.bounce_y()

        # Detect collision with wall y
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() < 320:
        ball.bounce_y()

    #Detect R paddle misses
    if ball.ycor() < -250:
        ball.reset_position()


screen.exitonclick()