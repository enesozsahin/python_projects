from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_speed= STARTING_MOVE_DISTANCE

    def create_car(self):
        chance= random.randint(1,6)
        if chance==1 or chance==4:
            en= Turtle()
            en.shape("square")
            en.penup()
            en.shapesize(stretch_wid=1,stretch_len=2)
            en.setheading(180)
            en.goto(250, 180)
            en.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            en.goto(300,random_y )
            self.all_cars.append(en)

    def move(self):
        for car in self.all_cars:

            car.setx(car.xcor()-self.car_speed)

    def move_fast(self):
        self.car_speed += MOVE_INCREMENT


