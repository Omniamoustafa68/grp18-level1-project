#from turtle import turtle class, screen class
import random
import time
from turtle import Turtle, Screen


def draw_turtle(turtle_name, turtle_color, y_pos):
    turtle_name = Turtle()
    turtle_name.color(turtle_color)
    turtle_name.shape('turtle')
    turtle_name.shapesize(1.5)
    turtle_name.penup()
    turtle_name.goto(x=-300, y=y_pos)
    turtle_name.pendown()
    return turtle_name


game_end= False      #the game is still running
def control_turtle():
    if not game_end:
        g_turtle.forward(10)
#take object from turtle class
my_turtle = Turtle()

#take object from screen class
my_screen = Screen()

#screen setup
my_screen.title(titlestring='race game')
my_screen.setup(height=500, width=800)
my_screen.bgcolor('forestgreen')


#heading
my_turtle.penup()
my_turtle.goto(x=-100, y=205)
my_turtle.color('white')
my_turtle.write('Turtle Race', font=('Arial', 20, 'bold'))



#brown floor
my_turtle.goto(x=-350, y=200)
my_turtle.pendown()
my_turtle.color('black')
my_turtle.fillcolor('chocolate')

my_turtle.begin_fill()
for i in range(2):
    my_turtle.forward(700)
    my_turtle.right(90)
    my_turtle.forward(400)
    my_turtle.right(90)
my_turtle.end_fill()


#finish line
my_turtle.penup()
my_turtle.goto(x=250,y=210)
my_turtle.right(90)
my_turtle.shape('square')
for i in range(10):
    my_turtle.forward(20)
    my_turtle.color('black')
    my_turtle.stamp()
    my_turtle.forward(20)
    my_turtle.color('white')
    my_turtle.stamp()



my_turtle.penup()
my_turtle.goto(x=270,y=210)
my_turtle.shape('square')
for i in range(10):
    my_turtle.forward(20)
    my_turtle.color('white')
    my_turtle.stamp()
    my_turtle.forward(20)
    my_turtle.color('black')
    my_turtle.stamp()




#draw turtles
b_turtle = draw_turtle(turtle_name='blue_turtle', turtle_color='cyan', y_pos=150)
p_turtle = draw_turtle(turtle_name='pink_turtle', turtle_color='pink', y_pos=50)
y_turtle = draw_turtle(turtle_name='yellow_turtle', turtle_color='yellow', y_pos=-50)
g_turtle = draw_turtle(turtle_name='green_turtle', turtle_color='green', y_pos=-150)



#pause for 1 second before start the race
time.sleep(1)

#keyboard listener
my_screen.listen()
my_screen.onkey(control_turtle, 'Right')
#move the turtles
while True:
    b_turtle.forward(random.randint(1,10))
    p_turtle.forward(random.randint(1,10))
    y_turtle.forward(random.randint(1,10))
    #g_turtle.forward(random.randint(1,10))
    if b_turtle.xcor() >230:
        winner = b_turtle
        break
    elif p_turtle.xcor() >230:
        winner = p_turtle
        break
    elif y_turtle.xcor() >230:
        winner = y_turtle
        break
    elif g_turtle.xcor()>230:
        winner = g_turtle
        break

#celebrate winner
game_end = True
winner.shapesize(2.5)
for i in range(1000):
    winner.left(5)

my_screen.exitonclick()