from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bids", prompt="which turtle will win the race: \n"
                                                           "red/green/yellow/blue/orange/purple")
colors = ["red", "green", "yellow", "blue", "orange", "purple"]
y_coordinate = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtle = []

for index in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-230, y=y_coordinate[index])
    all_turtle.append(turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()