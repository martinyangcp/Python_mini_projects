from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",24,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.write(f"score:{self.score}",align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)




