from turtle import Turtle, Screen, colormode
from random import choice


"""" extract the colors
import colorgram
rgb_colors = []
colors = colorgram.extract('image.jpg', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
"""
colormode(255)
rgb_colors = [(235, 234, 231), (236, 230, 233), (231, 241, 235), (225, 233, 239), (237, 34, 109), (155, 22, 65), (240, 72, 33), (7, 147, 92), (216, 170, 47), (180, 160, 41), (25, 123, 191), (44, 191, 233), (82, 21, 79), (244, 220, 49), (252, 224, 0), (125, 192, 86), (184, 38, 102), (213, 63, 21), (47, 171, 107), (172, 23, 17)]
tim = Turtle()
tim.shape("turtle")
#tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots:
    tim.dot(20, choice(rgb_colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)










screen = Screen()
screen.exitonclick()