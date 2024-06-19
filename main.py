from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()

screen.bgcolor("black")
screen.title("The Snake Game")
screen.setup(width=600, height=600)

screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    score_board.write_score()
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.score += 1
        score_board.clear()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score_board.game_over()

    for seg in snake.all_segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score_board.game_over()









screen.exitonclick()
