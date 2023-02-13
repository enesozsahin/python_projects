from turtle import Turtle
FONT= ("Courier", 25, "normal")
ALIGNMENT="center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 350)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score} ", align=ALIGNMENT, font=FONT)

    def keep_score(self):
        self.score +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= ALIGNMENT, font=FONT)