import random
import turtle as turtle_module

tim_screen = turtle_module.Screen()

tim_screen.setup(600,600)

user_bet = tim_screen.textinput(title="Place your bet", prompt="which turtle will win the race, enter turtle name")
print(user_bet)
tim1 = turtle_module.Turtle(shape="turtle")
tim2= turtle_module.Turtle(shape="turtle")
tim3 = turtle_module.Turtle(shape="turtle")
tim4 = turtle_module.Turtle(shape="turtle")

tim1.color("green")

tim2.color("yellow")
#
tim3.color("red")

tim4.color("blue")

tim1.hideturtle()
tim2.hideturtle()
tim3.hideturtle()
tim4.hideturtle()

tim1.penup()
tim2.penup()

tim3.penup()
tim4.penup()
tim1.goto(20/2 - (tim_screen.window_width() - 20)/2, tim_screen.window_height()/2 - 20 /2)
tim2.goto(20/2 - (tim_screen.window_width() - 20) /2, tim_screen.window_height()/2.5 - 20 /3)
tim3.goto(20/2 - (tim_screen.window_width() - 20) /2, tim_screen.window_height()/3.5 - 20 /4)
tim4.goto(20/2 - (tim_screen.window_width() - 20) /2, tim_screen.window_height()/4.5 - 20 /5)
tim1.showturtle()
tim2.showturtle()
tim3.showturtle()
tim4.showturtle()


tim1.setheading(0)
tim2.setheading(0)
tim3.setheading(0)
tim4.setheading(0)
speed = [10, 30, 40, 50, 24, 32]

grid_width = 600
cell_size = 40

turtles = ['tim1', 'tim2', ]


def get_name(turtle):
    if turtle == tim1:
        return "tim1"
    elif turtle == tim2:
        return  "tim2"
    elif turtle == tim3:
        return "tim3"
    else:
        return "tim4"

def get_cord(turtle):
    tim_x,tim_y = turtle.position()
    if abs(tim_x) > (grid_width/2 - cell_size/2):
        if turtle == tim1 and user_bet == "tim1":
            print("tim 1 won")
        elif turtle == tim2 and user_bet == "tim2":
            print("tim 2 won")
        elif turtle == tim3 and user_bet == "tim3":
            print("tim 3 won")
        elif turtle == tim4 and user_bet == "tim4":
            print("tim 4 won")
        else:
            new_turtle = get_name(turtle)
            print(f"you loose {new_turtle} won")
        return True
    else:
        return False


for i in range(20):

    if get_cord(tim1) or get_cord(tim2) or get_cord(tim3) or get_cord(tim4):
        break
    tim1.forward(random.choice(speed))
    tim2.forward(random.choice(speed))
    tim3.forward(random.choice(speed))
    tim4.forward(random.choice(speed))


tim_screen.exitonclick()