import time
from turtle import Screen
from player import Player,FINISH_LINE_Y,STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("CrossingGame")
screen.bgcolor("white")

cars=CarManager()
player=Player()
scoreboard=Scoreboard()

player.setheading(90)
player.goto(STARTING_POSITION)
screen.tracer(0)
screen.listen()

screen.onkey(player.move_up, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on=False
            scoreboard.game_over()

    if player.ycor() > FINISH_LINE_Y:

        player.level_pass()
        if player.level_pass():
            scoreboard.increase_level()
            cars.move_fast()


screen.exitonclick()