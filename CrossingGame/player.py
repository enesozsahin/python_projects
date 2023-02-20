STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()

    def level_pass(self):
        self.goto(STARTING_POSITION)
        return True

    def move_up(self):
        self.fd(MOVE_DISTANCE)



