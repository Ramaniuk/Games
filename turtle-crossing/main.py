import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

score = Scoreboard()
player = Player()
screen.onkey(fun=player.move_up, key="Up")

cars = []

#for car in range (50):
#    car = CarManager()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            score.game_over()
            game_is_on = False

    if player.ycor() == FINISH_LINE_Y:
        player.reset_position()
        car_manager.level_up()
        score.score_up()


screen.exitonclick()
