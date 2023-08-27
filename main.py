from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
score = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")   #onkeypress() for press and hold option
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

speed = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    #detecting collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    #missing right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_score += 1
        score.update_score()
    
    #missing left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_score += 1
        score.update_score()


screen.exitonclick()