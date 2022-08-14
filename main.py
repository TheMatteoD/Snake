from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


#Creates Screen 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Snake 🐍")
screen.tracer(0)


#Creates Snake, Food, and Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()


#User Controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


#Main Gameplay Loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detects if Food is collected
    if snake.head.distance(food) <15:
        scoreboard.collision()
        food.refresh()
        snake.extend()

    #Detects if Snake Goes Out of Bounds
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.reset()

    #Detects if Snake Hits It's Self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.reset()


screen.exitonclick()

