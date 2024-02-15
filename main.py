# The First step in creating Turtle Graphics Window;
from turtle import Screen # Importing Screen Class;
# Import Class Snake from snakeFile;
from snake import Snake
# Import Class Food from foodFile;
from food import Food
# Import Class Scoreboard from scoreboard;
from scoreboard import Scoreboard
# Importing time Module;
import time
# Created a Screen object Named screen;
screen = Screen()
# Method to set the Dimensions of the Window;
screen.setup(width=600, height=600)
# To set the Background color of the Screen;
screen.bgcolor("black") # Set Background Color To Black;
# Screen Title Name;
screen.title("My Snake Game")
# Setting the tracer to 0 turns off Animation;
screen.tracer(0)
# Create Object From The Class;
snake = Snake()
food = Food()
scoreboard = Scoreboard()
"""
You're telling the screen to listen for events such as Key-presses.
"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    """
    It's often used in Combination with turning off 
    The tracer (screen.tracer(0)) to optimize Drawing-Speed.
    """
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
"""
##################################
"""



