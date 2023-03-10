from turtle import Turtle, Screen

STARTING_POSITIONS= [(0,0) , (-20,0), (-40,0)]
MOVEMENT_DIST= 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segs=[]
        self.create_snake()
        self.head= self.segs[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_seg(position)


    def add_seg(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segs.append(new_segment)

    def extend(self):
        self.add_seg(self.segs[-1].position())

    def move(self):
        for seg_num in range(len(self.segs) - 1, 0, -1):
            newx = self.segs[seg_num - 1].xcor()
            newy = self.segs[seg_num - 1].ycor()
            self.segs[seg_num].goto(newx, newy)
        self.head.fd(MOVEMENT_DIST)


    def up(self):

        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):

        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def left(self):

        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)