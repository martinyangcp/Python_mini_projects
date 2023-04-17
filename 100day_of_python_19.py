from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title ="make your bet", prompt = "Which turtle will win the race? enter a color(red/yellow/green/blue) :")
speedlist = [0,0,0,0]
def making_track():
    Trackmaker.speed(100)
    Trackmaker.penup()
    Trackmaker.goto(x=-250,y=125)
    Trackmaker.pendown()
    Trackmaker.forward(400)
    Trackmaker.penup()
    Trackmaker.goto(x=-250,y=75)
    Trackmaker.pendown()
    Trackmaker.forward(400)
    Trackmaker.penup()
    Trackmaker.goto(x=-250,y=25)
    Trackmaker.pendown()
    Trackmaker.forward(400)
    Trackmaker.penup()
    Trackmaker.goto(x=-250,y=-25)
    Trackmaker.pendown()
    Trackmaker.forward(400)
    Trackmaker.penup()
    Trackmaker.goto(x=-250,y=-75)
    Trackmaker.pendown()
    Trackmaker.forward(400)
    Trackmaker.left(90)
    Trackmaker.forward(200)
    Trackmaker.hideturtle()
Trackmaker = Turtle()
making_track()
T1 = Turtle()
T1.shape("turtle")
T1.color("red")
T2 = Turtle()
T2.shape("turtle")
T2.color("blue")
T3 = Turtle()
T3.shape("turtle")
T3.color("green")
T4 = Turtle()
T4.shape("turtle")
T4.color("yellow")
T1.penup()
T2.penup()
T3.penup()
T4.penup()
T1.goto(x=-230,y=100)
T2.goto(x=-230,y=50)
T3.goto(x=-230,y=0)
T4.goto(x=-230,y=-50)
T1.pendown()
T2.pendown()
T3.pendown()
T4.pendown()

for i in range(4):
    speedlist[i] = random.randint(1, 5)
    while speedlist[i] in speedlist[:i]:
        speedlist[i] = random.randint(1,5)
T1.speed(speedlist[0])
T2.speed(speedlist[1])
T3.speed(speedlist[2])
T4.speed(speedlist[3])
if speedlist[0] == max(speedlist):
    winner = "red"
elif speedlist[1] == max(speedlist):
    winner = "blue"
elif speedlist[2] == max(speedlist):
    winner = "green"
elif speedlist[3] == max(speedlist):
    winner = "yellow"
T1.forward(350)
T2.forward(350)
T3.forward(350)
T4.forward(350)
print(speedlist)
if winner == user_bet:
    Trackmaker.write("You win")
else:
    T1.write("you lose ")
screen.exitonclick()