from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)   # set start position of paddle without showing
screen.listen()

paddle_l = Paddle(x=-350, y=0)
paddle_r = Paddle(x=350, y=0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(fun=paddle_r.up, key="Up")
screen.onkey(fun=paddle_r.down, key="Down")
screen.onkey(fun=paddle_l.up, key="w")
screen.onkey(fun=paddle_l.down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    #collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    screen.update() # set start position of paddle without showing

    #collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #reset coordinates R paddle:
    if ball.xcor() > 380:
        ball.reset_coordinate()
        scoreboard.l_point()

    #reset coordinates L paddle:
    if ball.xcor() < -380:
        ball.reset_coordinate()
        scoreboard.r_point()

screen.exitonclick()