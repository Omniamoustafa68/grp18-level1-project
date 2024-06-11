import random
from turtle import Turtle, Screen
my_turtle = Turtle()
my_turtle.shape('turtle')
colors_list = ['red', 'blue', 'green', 'yellow', 'pink']
for i in range(3, 11):
    num_of_sides = i
    color_chosen = random.choice(colors_list)
    my_turtle.color(color_chosen)
    angle = 360 / num_of_sides
    for j in range(i):
        my_turtle.forward(100)
        my_turtle.left(angle)








my_screen = Screen()
my_screen.exitonclick()