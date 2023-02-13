from turtle import  Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen= Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=850)
screen.title("Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



iscont= True
while iscont:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     detect collision with food class is 10 by 10
#
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.keep_score()

#         detect collision with wall

    if snake.head.xcor() > 480 or snake.head.xcor() < -480 or snake.head.ycor() > 405 or snake.head.ycor() < -425:
        iscont = False
        scoreboard.game_over()

    # [1:] is called slicing eger [1:3:1] dersen şu olur ikinci elemandan başla (çünkü bu baştaki numaraları listedeki
    # elemanların arasındaymış gibi düşün ve solundaki o numara gibi) dördüncüye elemana kadar git ama 2. elemanı atla
    # misal [::2] dersek listenin başından sonuna kadar git ve hepsini sınıflandır
    # ve 3. elemanları (yani aslında burada 3 ün katı olanlar oluyor) sayma, atla.
    # eger ayrıca [::-1] yaparsan da listeyi ya da tuple ı direkt ters çevirir.
    for segment in snake.segs[1:]:

        if snake.head.distance(segment) < 10:
            iscont =False
            scoreboard.game_over()

# detect collision with tail(if head collides with any segment of our snake, game over.)









# for seg_num in range(start=2 , stop=0 , step=-1):









screen.exitonclick()