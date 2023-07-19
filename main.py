import turtle
import time
from food import Food
from turtle import exitonclick, getscreen
from snake import Snake
from score_bord import Score

snake = Snake()
food = Food()
score = Score()
turtle.hideturtle()
my_screen = getscreen()
my_screen.setup(width=600, height=600)
my_screen.title("Snake Game")
my_screen.bgcolor("black")
my_screen.tracer(0)
game_over = False
my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")
snake.move()
while not game_over:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        snake.extand()
        score.score_maintain()

    if snake.snakes[0].xcor() > 290 or snake.snakes[0].xcor() < -290 or snake.snakes[0].ycor() < -280 or snake.snakes[
        0].ycor() > 280:
        score.reset_score()
        snake.delet_snake()
        snake.move()

    for segment in (snake.snakes):
        if snake.snakes[0] == segment:
            pass
        elif snake.snakes[0].distance(segment) < 10:
            score.reset_score()
            snake.delet_snake()
            snake.move()

exitonclick()
